from django.db import models

class Works(models.Model):
    name = models.CharField(max_length=250, verbose_name="Задвние")
    target = models.CharField(max_length=250, verbose_name="Цель задания")
    numbers_of_workers = models.IntegerField(blank=True, verbose_name="Количество человек на задание")
    start_time = models.DateTimeField(auto_now_add=True, verbose_name="Время начала работы")
    image_previous = models.ImageField(upload_to='works/previous/', blank=True, verbose_name="Фото работы")
    duration = models.TimeField(blank=True, verbose_name="Продолжительность работы")
    image_after = models.ImageField(upload_to='works/after', blank=True, verbose_name="Фото выполненной работы")

    def __str__(self):
        return self.name + ": " + self.target + \
        ": " + str(self.numbers_of_workers) + ": " + str(self.start_time) + \
            ": " + str(self.duration)