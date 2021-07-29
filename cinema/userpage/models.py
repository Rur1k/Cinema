from django.db import models
from adminpanel.models import FilmSession


class StatusSeat(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Статус места', max_length=64)

    def __str__(self):
        return self.name


class ReserveAndBuySeats(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    session = models.ForeignKey(FilmSession, on_delete=models.CASCADE)
    reserve_seats = models.JSONField('Зарезервированые места', null=True)
    buy_seats = models.JSONField('Купленные места', null=True)


