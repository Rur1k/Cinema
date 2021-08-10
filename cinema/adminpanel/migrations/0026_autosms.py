# Generated by Django 3.2.4 on 2021-08-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0025_auto_20210809_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoSMS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('id_group', models.IntegerField(verbose_name='Ид группы рассылки')),
                ('phone', models.CharField(max_length=10, verbose_name='Номер отправки смс')),
                ('sms', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст смс-рассылки')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]