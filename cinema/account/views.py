from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import LoginForm, UserRegistrationForm, UserForm, ProfileForm
from .models import Profile, User


def add_user_in_profile():
    users = User.objects.all()

    for user in users:
        if Profile.objects.filter(user=user.pk):
            print("Пользователь есть")
        else:
            Profile.objects.create(user=user)


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
            add_user_in_profile()
            return redirect('register_done')
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
            add_user_in_profile()
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

    ProfileUser = Profile.objects.all()

    data = {
        'users': ProfileUser
    }
    return render(request, 'adminpanel/users.html', data)


class UserDeleteView(DeleteView):
    model = User
    success_url = '../../admin/users/'
    template_name = 'account/delete_user.html'


def UpdateUserView(request, user_id):
    UserInfo = User.objects.get(id=user_id)
    ProfileInfo = Profile.objects.get(user=user_id)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pseudonym = request.POST.get('pseudonym')
        address = request.POST.get('address')
        card_number = request.POST.get('card_number')
        language = request.POST.get('language')
        male = request.POST.get('male')
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        city = request.POST.get('city')

        User.objects.filter(id=user_id).update(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        Profile.objects.filter(user=user_id).update(
                pseudonym=pseudonym,
                address=address,
                card_number=card_number,
                language=language,
                male=male,
                phone=phone,
                birth_date=birth_date,
                city=city
        )

        return redirect('users')
        # else:
        #     print(user_form.errors)
        #     print(profile_form.errors)

    user_form = UserForm(initial={
        'username': UserInfo.username,
        'email': UserInfo.email,
        'password': UserInfo.password,
        'first_name': UserInfo.first_name,
        'last_name': UserInfo.last_name,
    })
    profile_form = ProfileForm(initial={
        'pseudonym': ProfileInfo.pseudonym,
        'address': ProfileInfo.address,
        'card_number': ProfileInfo.card_number,
        'language': ProfileInfo.language,
        'male': ProfileInfo.male,
        'phone': ProfileInfo.phone,
        'birth_date': ProfileInfo.birth_date,
        'city': ProfileInfo.city,
    })

    data = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'adminpanel/add_user.html', data)
