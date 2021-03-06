# Generated by Django 3.2.4 on 2021-07-10 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0012_auto_20210709_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status_main',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='Статус глобальный')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name_news', models.CharField(max_length=64, verbose_name='Название новости')),
                ('description_news', models.TextField(verbose_name='Описание новости')),
                ('main_picture', models.ImageField(null=True, upload_to='static/img/cinema/news')),
                ('picture_1', models.ImageField(null=True, upload_to='static/img/cinema/news')),
                ('picture_2', models.ImageField(null=True, upload_to='static/img/cinema/news')),
                ('picture_3', models.ImageField(null=True, upload_to='static/img/cinema/news')),
                ('picture_4', models.ImageField(null=True, upload_to='static/img/cinema/news')),
                ('picture_5', models.ImageField(null=True, upload_to='static/img/cinema/news')),
                ('url_youtube', models.URLField(null=True, verbose_name='Видео новости')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateField(verbose_name='Дата активации')),
                ('status_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.status_main')),
            ],
        ),
    ]
