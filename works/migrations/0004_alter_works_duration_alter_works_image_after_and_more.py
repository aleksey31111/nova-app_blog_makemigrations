# Generated by Django 5.1.1 on 2024-09-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_alter_works_numbers_of_workers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='duration',
            field=models.TimeField(blank=True, verbose_name='Продолжительность работы'),
        ),
        migrations.AlterField(
            model_name='works',
            name='image_after',
            field=models.ImageField(blank=True, upload_to='works/after', verbose_name='Фото выполненной работы'),
        ),
        migrations.AlterField(
            model_name='works',
            name='image_previous',
            field=models.ImageField(blank=True, upload_to='works/previous/', verbose_name='Фото работы'),
        ),
        migrations.AlterField(
            model_name='works',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время начала работы'),
        ),
    ]
