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
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
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
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'card_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номера карты',
            }),
            'language': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Язык',
            }),
            'male': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Пол',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'type': 'date',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город',
            }),
        }

