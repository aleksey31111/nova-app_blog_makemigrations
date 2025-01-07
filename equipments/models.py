from django.db import models


class Equipments(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название оборудования")
    description = models.CharField(max_length=100, verbose_name="Назначение")
    image = models.ImageField(upload_to='equipments/images/', blank=True, verbose_name="Изображение оборудования")
    manual = models.TextField(blank=True, verbose_name="Инструкция")
    url = models.URLField(blank=True, verbose_name="Страница в интернете")
    servicebility = models.BooleanField(verbose_name="Работоспособность")
    defect = models.CharField(max_length=100, verbose_name="Неполадки")

    def __str__(self):
        return self.name
