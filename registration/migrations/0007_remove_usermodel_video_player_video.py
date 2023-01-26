# Generated by Django 4.0.6 on 2022-12-30 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_usermodel_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='video',
        ),
        migrations.AddField(
            model_name='player',
            name='video',
            field=models.FileField(default=1, upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'wav'])], verbose_name='Видео'),
            preserve_default=False,
        ),
    ]
