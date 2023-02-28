
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
import os
from django.conf import settings
from django.utils import timezone
# from registration.models import UserData
from multiselectfield import MultiSelectField

POSITION_CHOICES = (
    ('goalkeeper', 'Вратарь'),
    ('central_defender', 'Центральный защитник'),
    ('left_defender', 'Левый защитник'),
    ('right_defender', 'Правый защитник'),
    ('central_defensive_midfielder', 'Центральный опорный полузащитник'),
    ('central_midfielder', 'Центральный полузащитник'),
    ('left_midfielder', 'Левый полузащитник'),
    ('right_midfielder', 'Правый полузащитник'),
    ('centre forward', 'Центральный нападающий'),
    ('right_winger', 'Правый вингер'),
    ('left_winger', 'Левый вингер'),
    ('insider', 'Инсайдер'),
)


# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     role = models.CharField(max_length=30)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def __str__(self):
#         return self.email

def photo_upload_to(instance, filename):
    return 'photo/{}/{}'.format(instance.user.username, filename)


def video_upload_to(instance, filename):
    return 'video/{}/{}'.format(instance.user.username, filename)


class View(models.Model):
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)


class UserPhoto(models.Model):
    # role = [
    #     ('player', 'Игрок'),
    #     ('agent', 'Агент'),
    #     ('club', 'Клуб'),
    #     ('parent', 'Родитель'),
    #     ('trainer', 'Тренер'),
    #     ('scout', 'Скаут'),
    # ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    photo = models.ImageField(upload_to=photo_upload_to, blank=True)
    # user_role = position = MultiSelectField(verbose_name='Роль', choices=role, blank=True,
    #                                    null=True, default='player')
@receiver(pre_delete, sender=UserPhoto)
def userphoto_delete(sender, instance, **kwargs):
    # Удаляем файл при удалении объекта UserPhoto
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)




class Player(models.Model):
    leg = [
        ('R', 'Правая'),
        ('L', 'Левая'),
        ('B', 'Обе')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    leg = models.TextField('Нога', choices=leg, blank=True, null=True)
    position = MultiSelectField(verbose_name='Позиция', choices=POSITION_CHOICES, blank=True, null=True)
    age = models.CharField("Возраст", max_length=5, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=30, blank=True, null=True)
    second_name = models.CharField("Фамилия", max_length=30, blank=True, null=True)
    patronymic = models.CharField("Отчество", max_length=30, blank=True, null=True)
    height = models.CharField("Рост", max_length=4, blank=True, null=True)
    weight = models.CharField("Вес", max_length=4, blank=True, null=True)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    shengen = models.BooleanField("Шенген", default=False, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    description = models.TextField("Описание", max_length=254, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    views = models.ManyToManyField(View, related_name="player_views", blank=True)

    # photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def total_views(self):
        return self.views.count()

class PlayersVideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField("Видео", upload_to=video_upload_to, null=True, blank=True, max_length=150)
    description = models.TextField(blank=True, null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Заголовок", max_length=255,blank=True)
    def __str__(self):
        return str(self.video.name)

class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20, blank=True,null=True)
    second_name = models.CharField("Фамилия", max_length=30, blank=True,null=True)
    patronymic = models.CharField("Отчество", max_length=30, blank=True,null=True)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    # photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)
    players = models.ManyToManyField(Player, related_name="agent_players", blank=True, verbose_name="Игроки агента")

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")


class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20, blank=True,null=True)
    second_name = models.CharField("Фамилия", max_length=30, blank=True,null=True)
    patronymic = models.CharField("Отчество", max_length=30, blank=True,null=True)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    # passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    players = models.ManyToManyField(Player, related_name="parent_players", blank=True, verbose_name="Игроки родителя")
    views = models.ManyToManyField(View, related_name='players', verbose_name='Просмотры')

    # photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")


class Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20, blank=True,null=True)
    second_name = models.CharField("Фамилия", max_length=30, blank=True,null=True)
    patronymic = models.CharField("Отчество", max_length=30, blank=True,null=True)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    # passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)

    players = models.ManyToManyField(Player, related_name="trainer_players", blank=True, verbose_name="Игроки тренера")
    # photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)
    # school description (ending 's' does meen 'school')

    country_s = models.CharField("Страна, в которой находится школа", max_length=50, blank=True)
    city_s = models.CharField("Город, в котором находится школа", max_length=50, blank=True)
    phone_s = models.CharField("Номер телефона школы", max_length=15, blank=True)
    e_mail_s = models.EmailField("E-Mail школы", blank=True)
    photo_s = models.FileField("Фото школы", upload_to="school_photoes", null=True, blank=True)

    # телефон, e-mail, фото до 10, ссылки на ютуб, и т.п. до 10

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")


class Club(models.Model):
    ages = [
        ('3-4', '3-4'),
        ('5-6', '5-6'),
        ('7-8', '7-8'),
        ('9-10', '9-10'),
        ('11-12', '11-12'),
        ('13-14', '13-14'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    national_name = models.CharField("Национальное название клуба", max_length=20, blank=True,null=True)
    eng_name = models.CharField("Английское название клуба", max_length=30, blank=True,null=True)
    # phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    # passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    # photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)
    players = models.ManyToManyField(Player, related_name="club_players", blank=True, verbose_name="Игроки клуба")
    schools = models.JSONField("Школы", blank=True, null=True)
    school_ages = models.TextField("Возрастная группа школы", choices=ages, default="Возрастная группа", blank=True)

    def __str__(self):
        return str(f"{self.national_name} {self.eng_name} ")


class Scout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20, blank=True,null=True)
    second_name = models.CharField("Фамилия", max_length=30, blank=True,null=True)
    patronymic = models.CharField("Отчество", max_length=30, blank=True,null=True)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    # = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    school = models.TextField("Школы(Название, страна, город)", max_length=250, blank=True)

    # photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")
