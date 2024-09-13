from django.db.models import Q

from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from . import serializers
from . import models

# Create your views here.

class CategoryListApiView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class FoodsListApiView(APIView):

    def get(self, request, category_name):
        foods = models.Food.objects.filter(
            Q(category__name_uz__icontains=category_name) |
            Q(category__name_ru__icontains=category_name) |
            Q(category__name_en__icontains=category_name)
        )

        serializer = serializers.FoodListSerializer(foods, many=True)

        return Response(serializer.data)

class FoodApiView(generics.RetrieveAPIView):
    serializer_class = serializers.FoodSerializer
    
    def get_object(self):
        name = self.kwargs.get('food_name')
        food = models.Food.objects.filter(
                    Q(name_uz__icontains=name) |
                    Q(name_ru__icontains=name) |
                    Q(name_en__icontains=name)
                ).first()
        return food