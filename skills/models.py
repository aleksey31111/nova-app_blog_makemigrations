from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название навыка")
    fio = models.CharField(max_length=50, verbose_name="Имя подсобного рабочего")
    description = models.CharField(max_length=250, verbose_name="Описание навыка")
    image = models.ImageField(upload_to='skills/images', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title