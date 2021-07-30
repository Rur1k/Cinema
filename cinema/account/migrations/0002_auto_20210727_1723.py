# Generated by Django 3.2.4 on 2021-07-27 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='register_date',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_number',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Номер карты'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name=' Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userlanguage'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='male',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.usermale'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pseudonym',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Псевдоним'),
        ),
    ]