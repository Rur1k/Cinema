from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, UserForm, ProfileForm
from .models import Profile


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        return redirect('admin')
                    else:
                        return redirect('mainpage')
            else:
                return render(request, 'account/login_error.html')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def logout_user(request):
    if request.user.is_superuser:
        logout(request)
        return redirect('login')
    else:
        logout(request)
        return redirect('mainpage')


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def add_new_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            save_user_profile = profile_form.save(commit=False)
            save_user_profile.user = user_form.save(commit=False)
            save_user_profile.save()
            return redirect('users')
        else:
            print(user_form.errors)
            print(profile_form.errors)

    user_form = UserForm
    profile_form = ProfileForm

    data = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'adminpanel/add_user.html', data)


def users(request):
    data = {
        'users': Profile.objects.all()
    }
    return render(request, 'adminpanel/users.html', data)
