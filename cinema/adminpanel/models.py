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

class Status_main(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Статус глобальный', max_length=64)

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
    picture_1 = models.ImageField(upload_to='static/img/film', null=True)
    picture_2 = models.ImageField(upload_to='static/img/film', null=True)
    picture_3 = models.ImageField(upload_to='static/img/film', null=True)
    picture_4 = models.ImageField(upload_to='static/img/film', null=True)
    picture_5 = models.ImageField(upload_to='static/img/film', null=True)
    status_film = models.ForeignKey(Status_film, on_delete=models.CASCADE)
    date_premiere = models.DateField('Дата примьеры')
    trailer = models.URLField('Трейлер фильма')
    format_film = models.ManyToManyField(Format_film)

    def __str__(self):
        return self.film_name


class Cinema_hall(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    number_hall = models.CharField('Номер зала', max_length=16)
    create_date = models.DateTimeField(auto_now_add=True)
    description_hall = models.TextField('Описание зала')
    top_banner = models.ImageField(upload_to='static/img/cinema/hall')
    row = models.IntegerField('Количесво рядов')
    col = models.IntegerField('Количесов мест в ряду')


class News(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name_news = models.CharField('Название новости', max_length=64)
    description_news = models.TextField('Описание новости')
    main_picture = models.ImageField(upload_to='static/img/cinema/news', null=True)
    picture_1 = models.ImageField(upload_to='static/img/cinema/news', null=True)
    picture_2 = models.ImageField(upload_to='static/img/cinema/news', null=True)
    picture_3 = models.ImageField(upload_to='static/img/cinema/news', null=True)
    picture_4 = models.ImageField(upload_to='static/img/cinema/news', null=True)
    picture_5 = models.ImageField(upload_to='static/img/cinema/news', null=True)
    url_youtube = models.URLField('Видео новости', null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateField('Дата активации')
    status_news = models.ForeignKey(Status_main, on_delete=models.CASCADE)


class Stock(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name_stock = models.CharField('Название акции', max_length=64)
    description_stock = models.TextField('Описание акции')
    main_picture = models.ImageField(upload_to='static/img/cinema/stock', null=True)
    picture_1 = models.ImageField(upload_to='static/img/cinema/stock', null=True)
    picture_2 = models.ImageField(upload_to='static/img/cinema/stock', null=True)
    picture_3 = models.ImageField(upload_to='static/img/cinema/stock', null=True)
    picture_4 = models.ImageField(upload_to='static/img/cinema/stock', null=True)
    picture_5 = models.ImageField(upload_to='static/img/cinema/stock', null=True)
    url_youtube = models.URLField('Видео акции', null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateField('Дата активации')
    status_stock = models.ForeignKey(Status_main, on_delete=models.CASCADE)


class Page(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    status_delete = models.IntegerField("Возможность удаления", default=1)
    name_page = models.CharField('Название страницы', max_length=32)
    description_page = models.TextField('Описание')
    main_picture = models.ImageField(upload_to='static/img/cinema/pages', null=True)
    picture_1 = models.ImageField(upload_to='static/img/cinema/pages', null=True)
    picture_2 = models.ImageField(upload_to='static/img/cinema/pages', null=True)
    picture_3 = models.ImageField(upload_to='static/img/cinema/pages', null=True)
    picture_4 = models.ImageField(upload_to='static/img/cinema/pages', null=True)
    picture_5 = models.ImageField(upload_to='static/img/cinema/pages', null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status_page = models.ForeignKey(Status_main, on_delete=models.CASCADE)


class MainPage(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    status_delete = models.IntegerField("Возможность удаления", default=0)
    name_page = models.CharField('Название страницы', max_length=32, default='Главная страница')
    phone_one = models.CharField('Номер телефона 1', max_length=32)
    phone_two = models.CharField('Номер телефона 2', max_length=32)
    seo_text = models.TextField('Описание')
    create_date = models.DateTimeField(auto_now_add=True)
    status_page = models.ForeignKey(Status_main, on_delete=models.CASCADE)


class ContactPage(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    status_delete = models.IntegerField("Возможность удаления", default=0)
    name_page = models.CharField('Название страницы', max_length=32, default='Контакты')
    create_date = models.DateTimeField(auto_now_add=True)
    status_page = models.ForeignKey(Status_main, on_delete=models.CASCADE)


class FilmSession(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    hall = models.ForeignKey(Cinema_hall, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    price_ticket = models.IntegerField('Цена билета')


class Ticket(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    film_session = models.ForeignKey(FilmSession, on_delete=models.CASCADE)
    film = models.CharField('Название фильма', max_length=32)
    datetime = models.CharField('Дата и время сеанса', max_length=32)
    price = models.IntegerField('Цена билета')
    row = models.IntegerField('Ряд')
    seat = models.IntegerField('Место')











