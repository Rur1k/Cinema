# Generated by Django 3.2.4 on 2021-06-30 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0010_alter_cinema_hall_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='static/img/film')),
                ('film', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='adminpanel.film')),
            ],
        ),
    ]