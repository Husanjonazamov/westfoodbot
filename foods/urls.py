from django.urls import path

from . import views 

urlpatterns = [
    path('foods/category/', views.CategoryListApiView.as_view()),
    path('foods/category/<str:category_name>/', views.FoodsListApiView.as_view()),
    path('foods/<str:food_name>/', views.FoodApiView.as_view()),
]
