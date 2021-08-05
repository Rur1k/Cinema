from django import forms
from .models import *


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['film_name',
                  'relese_year',
                  'country',
                  'producer',
                  'director',
                  'screenwriter',
                  'composer',
                  'operator',
                  'genre',
                  'budget',
                  'age',
                  'time_film',
                  'description_film',
                  'main_picture',
                  'picture_1',
                  'picture_2',
                  'picture_3',
                  'picture_4',
                  'picture_5',
                  'status_film',
                  'date_premiere',
                  'trailer',
                  'format_film',
                  ]

        widgets = {
            'film_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма',
            }),
            'relese_year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год выхода'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна производсва'
            }),
            'producer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Продюсер',
            }),
            'director': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Режисер',
            }),
            'screenwriter': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сценарист'
            }),
            'composer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Композитор'
            }),
            'operator': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оператор'
            }),
            'genre': forms.SelectMultiple(attrs={
                'class': 'select',
                'id': 'genre-select',
                'multiple': 'multiple',
                'v-model': 'selected'
            }),
            'budget': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Бюджет'
            }),
            'age': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст просмотра'
            }),
            'time_film': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длительность фильма'
            }),
            'description_film': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание фильма'
            }),
            'main_picture': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
            'picture_1': forms.ClearableFileInput(attrs={
                'class id': 'picture_1',
            }),
            'picture_2': forms.ClearableFileInput(attrs={
                'class id': 'picture_2',
            }),
            'picture_3': forms.ClearableFileInput(attrs={
                'class id': 'picture_3',
            }),
            'picture_4': forms.ClearableFileInput(attrs={
                'class id': 'picture_4',
            }),
            'picture_5': forms.ClearableFileInput(attrs={
                'class id': 'picture_5',
            }),
            'status_film': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус фильма'
            }),
            'date_premiere': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата примьеры',
                'type': 'date',
            }),
            'trailer': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на трейлер youtube'
            }),
            'format_film': forms.SelectMultiple(attrs={
                'id': 'format-select',
                'class': 'form-select',
                'multiple': 'multiple',
            }),
        }


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = [
            'cinema_name',
            'description_cinema',
            'conditions',
            'logo',
            'top_banner',
        ]

        widgets = {
            'cinema_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название кинотеатра',
            }),
            'description_cinema': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание кинотеатра'
            }),
            'conditions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Условия'
            }),
            'logo': forms.ClearableFileInput(attrs={
                'class id': 'picture_1',
            }),
            'top_banner': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
        }


class CinemaHallForm(forms.ModelForm):
    class Meta:
        model = Cinema_hall
        fields = [
            'number_hall',
            'description_hall',
            'top_banner',
            'row',
            'col',
        ]

        widgets = {
            'number_hall': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номера зала',
            }),
            'description_hall': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание зала'
            }),
            'top_banner': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
            'row': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количесов рядов'
            }),
            'col': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количестов мест в ряду'
            }),

        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'name_news',
            'description_news',
            'main_picture',
            'picture_1',
            'picture_2',
            'picture_3',
            'picture_4',
            'picture_5',
            'url_youtube',
            'pub_date',
            'status_news',
        ]

        widgets = {
            'name_news': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости',
            }),
            'description_news': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание новости'
            }),
            'main_picture': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
            'picture_1': forms.ClearableFileInput(attrs={
                'class id': 'picture_1',
            }),
            'picture_2': forms.ClearableFileInput(attrs={
                'class id': 'picture_2',
            }),
            'picture_3': forms.ClearableFileInput(attrs={
                'class id': 'picture_3',
            }),
            'picture_4': forms.ClearableFileInput(attrs={
                'class id': 'picture_4',
            }),
            'picture_5': forms.ClearableFileInput(attrs={
                'class id': 'picture_5',
            }),
            'status_news': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус новости'
            }),
            'pub_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата активации',
                'type': 'date',
            }),
            'url_youtube': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на новость в youtube'
            }),

        }


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            'name_stock',
            'description_stock',
            'main_picture',
            'picture_1',
            'picture_2',
            'picture_3',
            'picture_4',
            'picture_5',
            'url_youtube',
            'pub_date',
            'status_stock',
        ]

        widgets = {
            'name_stock': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название акции',
            }),
            'description_stock': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание акции'
            }),
            'main_picture': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
            'picture_1': forms.ClearableFileInput(attrs={
                'class id': 'picture_1',
            }),
            'picture_2': forms.ClearableFileInput(attrs={
                'class id': 'picture_2',
            }),
            'picture_3': forms.ClearableFileInput(attrs={
                'class id': 'picture_3',
            }),
            'picture_4': forms.ClearableFileInput(attrs={
                'class id': 'picture_4',
            }),
            'picture_5': forms.ClearableFileInput(attrs={
                'class id': 'picture_5',
            }),
            'status_stock': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус новости'
            }),
            'pub_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата активации',
                'type': 'date',
            }),
            'url_youtube': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на акцию в youtube'
            }),

        }


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'name_page',
            'description_page',
            'main_picture',
            'picture_1',
            'picture_2',
            'picture_3',
            'picture_4',
            'picture_5',
            'status_page',
        ]

        widgets = {
            'name_page': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'description_page': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'main_picture': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
            'picture_1': forms.ClearableFileInput(attrs={
                'class id': 'picture_1',
            }),
            'picture_2': forms.ClearableFileInput(attrs={
                'class id': 'picture_2',
            }),
            'picture_3': forms.ClearableFileInput(attrs={
                'class id': 'picture_3',
            }),
            'picture_4': forms.ClearableFileInput(attrs={
                'class id': 'picture_4',
            }),
            'picture_5': forms.ClearableFileInput(attrs={
                'class id': 'picture_5',
            }),
            'status_page': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        fields = [
            'phone_one',
            'phone_two',
            'seo_text',
            'status_page',
        ]

        widgets = {
            'phone_one': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон 1',
            }),
            'phone_two': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон 2',
            }),
            'seo_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст'
            }),
            'status_page': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class FilmSessionForm(forms.ModelForm):
    class Meta:
        model = FilmSession
        fields = [
            'datetime',
            'film',
            'price_ticket',
        ]

        widgets = {
            'datetime': forms.DateTimeInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'Дата сеанса',
                'type': 'datetime-local',
            }),
            'film': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Фильм'
            }),
            'price_ticket': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена билета',
            }),
        }


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [
            'picture',
            'url',
            'description',
        ]

        widgets = {
            'picture': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'текс',
            }),
        }


class NewsAndStocksForm(forms.ModelForm):
    class Meta:
        model = NewsAndStocksBanners
        fields = [
            'picture',
            'url',
            'description',
        ]

        widgets = {
            'picture': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'текс',
            }),
        }


class BackgroundSettingForm(forms.ModelForm):
    class Meta:
        model = BackgroundSetting

        fields = [
            'backgroundOn',
            'backgroundImg',
        ]

        widgets = {
            'backgroundOn': forms.RadioSelect(choices=[
                ('1', 'Фото на фон'),
                ('0', 'Просто фон')
            ], attrs={

            }),
            'backgroundImg': forms.ClearableFileInput(attrs={
                'class id': 'main_img',
            }),
        }


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)
