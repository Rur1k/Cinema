from django.contrib.auth.models import User
from .models import Profile
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Електронная почта',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль',
    }))

    class Meta:
        model = User
        fields = ('username', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Логин',
                'class': 'form-control',
                'name': 'username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email',
                'name': 'email',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'name': 'password',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'name': 'first_name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'name': 'last_name',
            }),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [
            'pseudonym',
            'address',
            'card_number',
            'language',
            'male',
            'phone',
            'birth_date',
            'city',
        ]

        widgets = {
            'pseudonym': forms.TextInput(attrs={
                'placeholder': 'Псевдоним',
                'class': 'form-control',
                'name': 'pseudonym',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес',
                'name': 'address',
            }),
            'card_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номера карты',
                'name': 'card_number',
            }),
            'language': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Язык',
                'name': 'language',
            }),
            'male': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Пол',
                'name': 'male',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'name': 'phone',
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'type': 'date',
                'name': 'birth_date',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город',
                'name': 'city',
            }),
        }

