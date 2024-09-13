from django.db import models



class Category(models.Model):
    name_uz = models.CharField('Categorya', max_length=50)
    name_ru = models.CharField("Категория", max_length=50)
    name_en = models.CharField("Categorya", max_length=50)

    def __str__(self) -> str:
        return self.name_uz

class Food(models.Model):
    img = models.ImageField(upload_to='foods/')
    img_file_id = models.CharField(max_length=255, null=True, blank=True)  # Yangi maydon
    name_uz = models.CharField("Taom nomi", max_length=255, unique=True)
    name_ru = models.CharField("Название блюда", max_length=255, unique=True)
    name_en = models.CharField("Name of the dish", max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description_uz = models.TextField("Tavsifi", null=True, blank=True)
    description_ru = models.TextField("Описание", null=True, blank=True)
    description_en = models.TextField("Description", null=True, blank=True)
    shop_rating = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name_uz
