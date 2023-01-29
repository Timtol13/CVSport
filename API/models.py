from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


class Player(models.Model):
    leg = [
        ('R', 'Правая'),
        ('L', 'Левая'),
    ]
    position = [
        ('1', 'Вратарь'),
        ('2', 'Центральный защитник'),
        ('3', 'Левый и правый защитник'),
        ('4', 'Левый и правый фланговый защитник'),
        ('5', 'Лентральный опорный полузащитник'),
        ('6', 'Центральный полузащитник'),
        ('7', 'Левый/правый полузащитник'),
        ('8', 'Центральный атакующий полузащитник')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    leg = models.TextField('Нога', choices=leg)
    position = models.TextField('Позиция', choices=position, default='Позиция')
    age = models.CharField("Возраст", max_length=5, blank=True, null=True)
    first_name = models.CharField("Имя", max_length=30, blank=True, null=True)
    second_name = models.CharField("Фамилия", max_length=30, blank=True, null=True)
    patronimyc = models.CharField("Отчество", max_length=30, blank=True, null=True)
    height = models.CharField("Рост", max_length=4, blank=True, null=True)
    weight = models.CharField("Вес", max_length=4, blank=True, null=True)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    shengen = models.BooleanField("Шенген", default=False, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    description = models.TextField("Описание", max_length=254, blank=True, null=True)
    is_show = models.BooleanField("Отображать_всем", default=True, blank=True, null=True)
    photo = FilerImageField(verbose_name="Фото в профиле", related_name="photo_in_profile_player",
                            null=True, blank=True,
                            on_delete=models.CASCADE)
    video = FilerFileField(verbose_name="Видео", related_name="video",
                            null=True, blank=True,
                            on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Agent(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronimyc = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    photo = FilerImageField(verbose_name="Фото в профиле", related_name="photo_in_profile_agent",
                            null=True, blank=True,
                            on_delete=models.CASCADE)
    players = models.JSONField("Игроки", null=True, blank=True)

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronimyc}")


class Parent(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronimyc = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    players = models.JSONField("Игроки", blank=True, null=True)
    photo = FilerImageField(verbose_name="Фото в профиле", related_name="photo_in_profile_parent",
                            null=True, blank=True,
                            on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronimyc}")


class Trainer(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronimyc = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    players = models.JSONField("Игроки", blank=True, null=True)
    photo = FilerImageField(verbose_name="Фото в профиле", related_name="photo_in_profile_trainer",
                            null=True, blank=True,
                            on_delete=models.CASCADE)
    #school description (ending 's' does meen 'school')

    country_s = models.CharField("Страна, в которой находится школа", max_length=50)
    city_s = models.CharField("Город, в котором находится школа", max_length=50)
    phone_s = models.CharField("Номер телефона школы", max_length=15)
    e_mail_s = models.EmailField("E-Mail школы")
    photo = FilerImageField(verbose_name="Фото школы", related_name="photo_of_school",
                            null=True, blank=True,
                            on_delete=models.CASCADE)
    #телефон, e-mail, фото до 10, ссылки на ютуб, и т.п. до 10

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronimyc}")


class Club(models.Model):
    ages = [
        ('3-4', '3-4'),
        ('5-6', '5-6'),
        ('7-8', '7-8'),
        ('9-10', '9-10'),
        ('11-12', '11-12'),
        ('13-14', '13-14'),
    ]
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronimyc = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    photo = FilerImageField(verbose_name="Фото в профиле", related_name="photo_in_profile_club",
                            null=True, blank=True,
                            on_delete=models.CASCADE)
    players = models.JSONField("Игроки", blank=True, null=True)
    schools = models.JSONField("Школы", blank=True, null=True)
    school_ages = models.TextField("Возрастная группа школы", choices=ages, default="Возрастная группа")

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronimyc}")


class Scout(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    second_name = models.CharField("Фамилия", max_length=30)
    patronimyc = models.CharField("Отчество", max_length=30)
    phone = models.CharField("Номер Телефона", max_length=30, blank=True, null=True)
    email = models.EmailField("Почта", max_length=100, blank=True, null=True)
    country = models.CharField("Страна", max_length=40, blank=True, null=True)
    city = models.CharField("Город", max_length=40, blank=True, null=True)
    passport = models.ImageField("Фото паспорта", upload_to='documents/', blank=True)
    school = models.TextField("Школы(Название, страна, город)", max_length=250)
    photo = FilerImageField(verbose_name="Фото в профиле", related_name="photo_in_profile_school",
                            null=True, blank=True,
                            on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.first_name} {self.second_name} {self.patronimyc}")

