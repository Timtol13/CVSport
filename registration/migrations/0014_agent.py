# Generated by Django 4.0.6 on 2023-01-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_alter_player_user_alter_usermodel_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('patronimyc', models.CharField(max_length=30, verbose_name='Отчество')),
                ('passport', models.ImageField(blank=True, upload_to='documents/photo/', verbose_name='Фото паспорта')),
                ('players', models.JSONField(verbose_name='Игроки')),
            ],
        ),
    ]
