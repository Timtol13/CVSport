from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


POSITION_CHOICES = (
    ('1', 'Вратарь'),
    ('2', 'Центральный защитник'),
    ('3', 'Левый защитник'),
    ('4', 'Правый защитник'),
    ('5', 'Центральный опорный полузащитник'),
    ('6', 'Центральный полузащитник'),
    ('7', 'Левый полузащитник'),
    ('8', 'Правый полузащитник'),
    ('9', 'Центральный нападающий'),
    ('10', 'Правый вингер'),
    ('11', 'Левый вингер'),
    ('12', 'Инсайдер'),
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
class Player(models.Model):
    leg = [
        ('R', 'Правая'),
        ('L', 'Левая'),
        ('B', 'Обе')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    leg = models.TextField('Нога', choices=leg)
    position = MultiSelectField(verbose_name='Позиция', choices=POSITION_CHOICES)
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
    photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)
    players = models.ManyToManyField(Player, related_name="agent_players", blank=True, verbose_name="Игроки агента")

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")


class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    # passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    players = models.ManyToManyField(Player, related_name="parent_players", blank=True, verbose_name="Игроки родителя")
    photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")


class Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    # passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)

    players = models.ManyToManyField(Player, related_name="trainer_players", blank=True, verbose_name="Игроки тренера")
    photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)
    # school description (ending 's' does meen 'school')

    country_s = models.CharField("Страна, в которой находится школа", max_length=50)
    city_s = models.CharField("Город, в котором находится школа", max_length=50)
    phone_s = models.CharField("Номер телефона школы", max_length=15)
    e_mail_s = models.EmailField("E-Mail школы")
    photo_s = models.ImageField("Фото школы", upload_to="school_photoes", null=True, blank=True)

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
    national_name = models.CharField("Национальное название клуба", max_length=20, blank=True)
    eng_name = models.CharField("Английское название клуба", max_length=30, blank=True)
    # phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    # passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)
    # players = models.ManyToManyField(Player,related_name="club_players", blank=True,verbose_name="Игроки клуба")
    schools = models.JSONField("Школы", blank=True, null=True)
    school_ages = models.TextField("Возрастная группа школы", choices=ages, default="Возрастная группа")

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")


class Scout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    # = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    school = models.TextField("Школы(Название, страна, город)", max_length=250)
    photo = models.ImageField("Фото в профиле", upload_to="profile_photoes", null=True, blank=True)

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronymic}")


class PlayersVideo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField("Видео", upload_to='video/videos', null=True, blank=True, max_length=150)

    def __str__(self):
        return str(self.file.name)
