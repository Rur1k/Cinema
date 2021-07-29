from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from adminpanel.models import FilmSession


class UserLanguage(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Язык', max_length=32)

    def __str__(self):
        return self.name


class UserMale(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Пол', max_length=16)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pseudonym = models.CharField('Псевдоним', max_length=16, blank=True, null=True)
    address = models.CharField('Адрес', max_length=64, blank=True, null=True)
    card_number = models.CharField('Номер карты', max_length=64, blank=True, null=True)
    language = models.ForeignKey(UserLanguage, on_delete=models.CASCADE, blank=True, null=True)
    male = models.ForeignKey(UserMale, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=16, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    city = models.CharField(' Город', max_length=16, blank=True, null=True)

    def __str__(self):
        return self.user.username






