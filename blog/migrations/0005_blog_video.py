# Generated by Django 5.1.1 on 2024-10-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, upload_to='blogs/videos', verbose_name='Видео по статье'),
        ),
    ]
