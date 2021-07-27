# Generated by Django 3.2.4 on 2021-07-26 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeslotSeatRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('row', models.IntegerField(verbose_name='Ряд')),
                ('seat', models.IntegerField(verbose_name='Место')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userpage.statusseat')),
            ],
        ),
    ]
