# Generated by Django 5.1.1 on 2024-09-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_alter_works_duration_alter_works_image_after_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Задвние'),
        ),
        migrations.AlterField(
            model_name='works',
            name='target',
            field=models.CharField(max_length=250, verbose_name='Цель задания'),
        ),
    ]
