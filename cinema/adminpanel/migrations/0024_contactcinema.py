# Generated by Django 3.2.4 on 2021-08-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0023_backgroundsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCinema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=32, verbose_name='Название кинотеатра')),
                ('address', models.CharField(max_length=128, verbose_name='Адресс')),
                ('coordinates', models.CharField(max_length=64, verbose_name='Координаты')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='static/img/contactcinema')),
            ],
        ),
    ]
