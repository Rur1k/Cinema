# Generated by Django 3.2.4 on 2021-06-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_alter_film_main_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='main_picture',
            field=models.ImageField(height_field='295', upload_to='../static/img/film', width_field='200'),
        ),
    ]
