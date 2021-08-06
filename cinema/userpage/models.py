from django.db import models
from adminpanel.models import FilmSession


class StatusSeat(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Статус места', max_length=64)

    def __str__(self):
        return self.name


class SeatsReserveAndBuy(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    session = models.ForeignKey(FilmSession, on_delete=models.CASCADE)
    seat = models.CharField('Место', max_length=16)
    status_seat = models.ForeignKey(StatusSeat, on_delete=models.CASCADE)



