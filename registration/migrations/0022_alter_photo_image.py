# Generated by Django 3.2.12 on 2023-01-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_trainer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(blank=True, upload_to='photo/', verbose_name='Фото'),
        ),
    ]
