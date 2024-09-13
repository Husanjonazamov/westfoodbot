from django.db import models
from foods.models import Food



class UserPhones(models.Model):
    user_id = models.IntegerField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.phone


class User(models.Model):
    user_id = models.IntegerField(unique=True)
    lang = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)  # Yangi maydon
    fullname = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:

        return self.fullname


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
