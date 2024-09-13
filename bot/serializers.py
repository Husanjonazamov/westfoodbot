from rest_framework.serializers import ModelSerializer

from .models import User, Basket, UserPhones


class UserPhoneSerializer(ModelSerializer):
    class Meta:
        model = UserPhones
        fields = '__all__'


class   GetBotUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        # fields = ('id', 'count', 'food', )
        fields = "__all__"
        depth = 2