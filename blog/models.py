from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статьи")
    focus = models.CharField(max_length=250, blank=True, verbose_name="Напрпвленность статьи")
    description = models.TextField(verbose_name="Содержание статьи")
    video = models.FileField(upload_to='blogs/videos', blank=True, verbose_name="Видео по статье")
    labor_protection = models.TextField(blank=True, verbose_name="Охрана труда(связанная со статьей)")
    data = models.DateField()

    def __str__(self):
        return self.title + ": " + self.focus
