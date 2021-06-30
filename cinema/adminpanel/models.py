from django.db import models


class Genre_film(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Название жанра', max_length=64)

    def __str__(self):
        return self.name


class Status_film(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Статус фильма', max_length=64)

    def __str__(self):
        return self.name


class Format_film(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Формат фильма', max_length=64)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    cinema_name = models.CharField('Название кинотеатра', max_length=64, null=True)
    description_cinema = models.TextField('Описание зала', null=True)
    conditions = models.TextField('Условия', null=True)
    logo = models.ImageField(upload_to='static/img/cinema', null=True)
    top_banner = models.ImageField(upload_to='static/img/cinema', null=True)

    def __str__(self):
        return self.cinema_name


class Seo_block(models.Model):
    id = models.AutoField(unique=True, primary_key=True)


class Film(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    film_name = models.CharField('Название фильма', max_length=64)
    relese_year = models.CharField('Год выхода', max_length=64)
    country = models.CharField('Страна производитель', max_length=64)
    producer = models.CharField('Продюсер', max_length=255)
    director = models.CharField('Режисер', max_length=255)
    screenwriter = models.CharField('Сценарист', max_length=255)
    composer = models.CharField('Композитор', max_length=255)
    operator = models.CharField('Оператор', max_length=255)
    genre = models.ManyToManyField(Genre_film)
    budget = models.CharField('Бюджет', max_length=64)
    age = models.CharField('Возраст просмотра', max_length=64)
    time_film = models.CharField('Длительность фильма', max_length=64)
    description_film = models.TextField('Описание фильма')
    main_picture = models.ImageField(upload_to='static/img/film')
    status_film = models.ForeignKey(Status_film, on_delete=models.CASCADE)
    date_premiere = models.DateField('Дата примьеры')
    trailer = models.URLField('Трейлер фильма')
    format_film = models.ManyToManyField(Format_film)

    def __str__(self):
        return self.film_name


class Cinema_hall(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    cinema_id = models.IntegerField('Ид зала', null=True)
    number_hall = models.CharField('Номер зала', max_length=16)
    create_date = models.DateTimeField(auto_now_add=True)
    description_hall = models.TextField('Описание зала')
    top_banner = models.ImageField(upload_to='static/img/cinema/hall')
    row = models.IntegerField('Количесво рядов')
    col = models.IntegerField('Количесов мест в ряду')


class ImageFilm(models.Model):
    film = models.ForeignKey(Film, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/film', blank=True)





