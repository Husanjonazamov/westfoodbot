from rest_framework.serializers import ModelSerializer
from .models import Category, Food

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FoodListSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = [
            'id',
            'img',
            'price',
            'name_uz',
            'name_ru',
            'name_en',
            'shop_rating',
            'category'
        ]

class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'