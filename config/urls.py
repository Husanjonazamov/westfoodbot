from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payments.urls')),
    path('', include('bot.urls')),
    path('', include('foods.urls')),
    re_path(r"media/(.*)", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"static/(.*)", serve, {"document_root": settings.STATIC_ROOT}),
]
# https://my.click.uz/services/pay?service_id=35502&merchant_id=26598&amount=1000&transaction_param=6415392394&return_url=https://t.me/testuchforbot