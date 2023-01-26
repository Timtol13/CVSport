# Generated by Django 3.2.12 on 2023-01-05 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0025_auto_20230104_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='photo',
        ),
        migrations.AlterField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.usermodel'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.usermodel'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.usermodel'),
        ),
    ]
