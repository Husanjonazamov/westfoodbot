from django.urls import path
from . import views

urlpatterns = [
    path('click/transaction/', views.OrderTestView.as_view()),
]