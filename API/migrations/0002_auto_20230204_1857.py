# Generated by Django 3.2.12 on 2023-02-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='club',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='club',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='club',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='club',
            name='players',
        ),
        migrations.RemoveField(
            model_name='club',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='scout',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='passport',
        ),
        migrations.AddField(
            model_name='agent',
            name='is_show',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Отображать_всем'),
        ),
        migrations.AddField(
            model_name='club',
            name='eng_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Английское название клуба'),
        ),
        migrations.AddField(
            model_name='club',
            name='is_show',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Отображать_всем'),
        ),
        migrations.AddField(
            model_name='club',
            name='national_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Национальное название клуба'),
        ),
        migrations.AddField(
            model_name='parent',
            name='is_show',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Отображать_всем'),
        ),
        migrations.AddField(
            model_name='scout',
            name='is_show',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Отображать_всем'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='is_show',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Отображать_всем'),
        ),
    ]
