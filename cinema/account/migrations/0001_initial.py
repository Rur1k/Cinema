# Generated by Django 3.2.4 on 2021-07-27 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32, verbose_name='Язык')),
            ],
        ),
        migrations.CreateModel(
            name='UserMale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=16, verbose_name='Пол')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudonym', models.CharField(blank=True, max_length=16, verbose_name='Псевдоним')),
                ('address', models.CharField(blank=True, max_length=64, verbose_name='Адрес')),
                ('card_number', models.CharField(blank=True, max_length=64, verbose_name='Номер карты')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Номер телефона')),
                ('birth_date', models.DateField(blank=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(blank=True, max_length=16, verbose_name=' Город')),
                ('language', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='account.userlanguage')),
                ('male', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='account.usermale')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]