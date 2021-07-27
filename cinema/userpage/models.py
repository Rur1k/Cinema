from django.db import models


class StatusSeat(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Статус места', max_length=64)

    def __str__(self):
        return self.name



