from django import forms
from .models import Film, Cinema, Cinema_hall, News, Stock, Page, MainPage


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
                'class': '',
                'id': 'img',
            }),
            'picture_1': forms.ClearableFileInput(),
            'picture_2': forms.ClearableFileInput(),
            'picture_3': forms.ClearableFileInput(),
            'picture_4': forms.ClearableFileInput(),
            'picture_5': forms.ClearableFileInput(),
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
                'class': 'form-control',
                'id': 'format-select',
                'multiple': 'multiple'
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
                'class': '',
                'id': 'img',
            }),
            'top_banner': forms.ClearableFileInput(attrs={
                'class': '',
                'id': 'img',
            })
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
                'class': '',
                'id': 'img',
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
                'class': '',
                'id': 'img',
            }),
            'picture_1': forms.ClearableFileInput(),
            'picture_2': forms.ClearableFileInput(),
            'picture_3': forms.ClearableFileInput(),
            'picture_4': forms.ClearableFileInput(),
            'picture_5': forms.ClearableFileInput(),
            'status_news': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус новости'
            }),
            'pub_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата активации',
                'type': 'date',
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
                'type': 'file',
                'id': 'img',
            }),
            'picture_1': forms.ClearableFileInput(),
            'picture_2': forms.ClearableFileInput(),
            'picture_3': forms.ClearableFileInput(),
            'picture_4': forms.ClearableFileInput(),
            'picture_5': forms.ClearableFileInput(),
            'status_stock': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус новости'
            }),
            'pub_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата активации',
                'type': 'date',
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
                'type': 'file',
                'id': 'img',
            }),
            'picture_1': forms.ClearableFileInput(),
            'picture_2': forms.ClearableFileInput(),
            'picture_3': forms.ClearableFileInput(),
            'picture_4': forms.ClearableFileInput(),
            'picture_5': forms.ClearableFileInput(),
            'status_page': forms.Select(attrs={
                'class': 'form-control',
            }),
        }