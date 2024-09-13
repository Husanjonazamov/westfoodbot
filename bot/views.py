from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . import serializers
from foods.models import Food
from bot.models import User, Basket, UserPhones

# Create your views here.


class GetBotUsersPhoneView(generics.ListCreateAPIView):
    queryset = UserPhones.objects.all()
    serializer_class = serializers.UserPhoneSerializer

class GetBotUsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.GetBotUserSerializer


class GetBotUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.GetBotUserSerializer

    def get_object(self):
        return get_object_or_404(User, user_id=self.kwargs.get('pk'))

class AddBacketItemView(APIView):

    def post(self, request):
        user_id = request.data.get('user_id')
        food_name = request.data.get('food_name')
        count = request.data.get('count')

        food = Food.objects.filter(
                Q(name_uz__icontains=food_name) |
                Q(name_ru__icontains=food_name) |
                Q(name_en__icontains=food_name)
            ).first()


        user = get_object_or_404(User, user_id=user_id)

        try:
            old_basket_item = Basket.objects.get(user=user, food=food)
            old_basket_item.count = count
            old_basket_item.save()
        except:
            Basket.objects.create(user=user, food=food, count=count)

        return Response({
            'status': 'success',
        })

@api_view(['GET'])
def GetUserBasketItems(request):
    # get query params
    user_id = request.GET.get('user_id')

    if not user_id:
        basket = Basket.objects.all()
    else:
        basket = get_list_or_404(Basket, user__user_id=user_id)
    serializer = serializers.BasketSerializer(basket, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def GetUserBasketItem(request):
    # get query params
    basket_id = request.GET.get('basket_id')

    if not basket_id:
        return Response({
            'status': 'error',
        }, status=400)

    basket = get_object_or_404(Basket, pk=basket_id)

    if request.method == 'GET':
        serializer = serializers.BasketSerializer(basket)
        return Response(serializer.data)


@api_view(['GET'])
def ChangeBasketItem(request):
    basket_id = request.GET.get('basket_id')
    action = request.GET.get('action')

    basket = get_object_or_404(Basket, pk=basket_id)

    if request.method == 'GET':
        if action == "incr":
            basket.count = basket.count + 1
        if action == "decr":
            basket.count = basket.count - 1
        basket.save()
        serializer = serializers.BasketSerializer(basket)
        return Response(serializer.data)


@api_view(['GET'])
def ClearUserBasketAndSetRating(request):
    user_id = request.GET.get('user_id')

    if not user_id:
        return Response({
            "status": False,
            "user_id": "user_id is required"
        })

    basket = Basket.objects.filter(user__user_id=user_id)

    for i in basket:
        food_id = i.food.pk
        food = Food.objects.get(pk=food_id)
        food.shop_rating += i.count
        food.save()

    basket.delete()

    return Response({
        "status": True,
        "message": "Basket succes delete"
    })


@api_view(['GET'])
def DeleteBasket(request):

    food_name = request.GET.get('food_name')
    user_id = request.GET.get('user_id')

    food = Food.objects.filter(
                Q(name_uz__icontains=food_name) |
                Q(name_ru__icontains=food_name) |
                Q(name_en__icontains=food_name)
            ).first()

    try:
        basket = Basket.objects.get(user__user_id=user_id, food__name_uz=food)
    except:
        return Response({
            "status": False,
            "message": "Basket not found"
        })

    basket.delete()

    return Response({
        "status": True,
        "message": "Basket succes delete"
    })


# Admin Views
def dashboard(request):
    return render(request, 'admin/dashboard.html')