# Generated by Django 4.0.6 on 2023-01-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_alter_agent_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='players',
            field=models.JSONField(blank=True, null=True, verbose_name='Игроки'),
        ),
    ]
