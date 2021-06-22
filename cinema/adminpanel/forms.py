from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Film
from django import forms

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

        film_name = forms.CharField()
        relese_year = forms.DateField()
        country = forms.CharField()
        producer = forms.CharField()
        director = forms.CharField()
        screenwriter = forms.CharField()
        composer = forms.CharField()
        operator = forms.CharField()
        genre = forms.MultipleChoiceField()
        budget = forms.CharField()
        age = forms.CharField()
        time_film = forms.CharField()
        description_film = forms.CharField(widget=forms.Textarea)
        main_picture = forms.ImageField()
        status_film = forms.ChoiceField()
        date_premiere = forms.DateField()
        trailer = forms.URLField()
        format_film = forms.MultipleChoiceField()

