from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.dashboard),

    path('bot/users/', views.GetBotUsersView.as_view()),
    path('bot/users_phone/', views.GetBotUsersPhoneView.as_view()),
    path('bot/users/<int:pk>', views.GetBotUserView.as_view()),

    path('busket/create', views.AddBacketItemView.as_view()),
    path('busket/list', views.GetUserBasketItems),
    path('busket/item', views.ChangeBasketItem),
    path('busket/change', views.ChangeBasketItem),
    path('busket/clear-and-rating', views.ClearUserBasketAndSetRating),
    path('busket/delete', views.DeleteBasket),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
