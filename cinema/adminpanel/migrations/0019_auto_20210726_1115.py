# Generated by Django 3.2.4 on 2021-07-26 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0018_contactpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('datetime', models.DateTimeField()),
                ('price_ticket', models.IntegerField(verbose_name='Цена билета')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.film')),
            ],
        ),
        migrations.AlterField(
            model_name='cinema_hall',
            name='cinema_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.cinema'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('film', models.CharField(max_length=32, verbose_name='Название фильма')),
                ('datetime', models.CharField(max_length=32, verbose_name='Дата и время сеанса')),
                ('price', models.IntegerField(verbose_name='Цена билета')),
                ('row', models.IntegerField(verbose_name='Ряд')),
                ('seat', models.IntegerField(verbose_name='Место')),
                ('film_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.filmsession')),
            ],
        ),
        migrations.AddField(
            model_name='filmsession',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.cinema_hall'),
        ),
    ]