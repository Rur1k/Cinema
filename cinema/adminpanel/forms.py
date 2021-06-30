from django import forms
from .models import Film, Cinema, Cinema_hall, ImageFilm


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


class ImageFilmForm(forms.ModelForm):
    class Meta:
        model = ImageFilm

        fields = {
            'image'
        }

        image = forms.ImageField()