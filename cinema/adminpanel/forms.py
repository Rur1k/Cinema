from django import forms
from .models import Film

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
                'placeholder': 'Название фильма'
            }),
            'relese_year': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год выхода',
                'type': 'date',
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
                'class': 'form-control',
                'placeholder': 'Жанр'
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
                'placeholder': 'Формат фильма'
            }),
        }