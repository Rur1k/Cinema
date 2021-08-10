from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.forms import formset_factory
from django.core.mail import send_mail, BadHeaderError
from cinema.settings import FROM_EMAIL, EMAIL_ADMIN
from django.http import HttpResponse, HttpResponseRedirect
from account.models import Profile
from django.db.models import Q


def admin(request):
    return render(request, 'adminpanel/statistics.html')


def films(request):
    context = {
        'films_active': Film.objects.filter(status_film=1),
        'films_pending': Film.objects.filter(status_film=2),
    }
    return render(request, 'adminpanel/films.html', context)


def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film_form = form.save(commit=False)
            film_form.save()
            return redirect('films')
        else:
            print(form.errors)
            print(formset.errors)

    form = FilmForm()
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_film.html", data)


class UpdateFilmView(UpdateView):
    model = Film
    success_url = '../../admin/films'
    template_name = 'adminpanel/add_film.html'
    form_class = FilmForm


class FilmDeleteView(DeleteView):
    model = Film
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_film.html'


def cinemas(request):
    context = {
        'cinemas': Cinema.objects.all()
    }
    return render(request, 'adminpanel/cinemas.html', context)


def add_cinema(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cinemas')
        else:
            print(form.errors)

    form = CinemaForm()
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_cinema.html", data)


def cinema_info(request, cinema_id):
    Halls = Cinema_hall.objects.filter(cinema_id=cinema_id)
    if len(Halls) != 0:
        context = {
            'cinema': Cinema.objects.get(id=cinema_id),
            'hall_list': Cinema_hall.objects.filter(cinema_id=cinema_id)
        }
    else:
        context = {
            'cinema': Cinema.objects.get(id=cinema_id),
        }
    return render(request, 'adminpanel/cinema.html', context)


class UpdateCinemaView(UpdateView):
    model = Cinema
    success_url = '../../admin/cinemas'
    template_name = 'adminpanel/add_cinema.html'
    form_class = CinemaForm


def add_cinema_hall(request, cinema_id):
    if request.method == 'POST':
        cinema = Cinema.objects.get(id=cinema_id)
        form = CinemaHallForm(request.POST, request.FILES)
        if form.is_valid():
            save_to_cinema = form.save(commit=False)
            save_to_cinema.cinema_id = cinema
            save_to_cinema.save()
            return redirect('cinema_info', cinema_id)
        else:
            print(form.errors)

    form = CinemaHallForm()
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_hall.html", data)


def hall_info(request, hall_id):
    hall_info_all = Cinema_hall.objects.get(id=hall_id)
    session = FilmSession.objects.filter(hall=hall_id)

    row = hall_info_all.row + 1
    col = hall_info_all.col + 1

    rows = range(1, row)
    columns = range(1, col)

    data = {
        'session': session,
        'hall': hall_info_all,
        'rows': rows,
        'columns': columns,
    }

    return render(request, 'adminpanel/hall.html', data)


class UpdateCinemaHallView(UpdateView):
    model = Cinema_hall
    success_url = '../../admin/cinemas'
    template_name = 'adminpanel/add_hall.html'
    form_class = CinemaHallForm


def news_list(request):
    context = {
        'news_list': News.objects.all()
    }
    return render(request, 'adminpanel/news.html', context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            print(form.errors)

    form = NewsForm()
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_news.html", data)


class UpdateNewsView(UpdateView):
    model = News
    success_url = '../../admin/news'
    template_name = 'adminpanel/add_news.html'
    form_class = NewsForm


def stocks(request):
    context = {
        'stocks': Stock.objects.all()
    }
    return render(request, 'adminpanel/stocks.html', context)


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stocks')
        else:
            print(form.errors)

    form = StockForm()
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_stock.html", data)


class UpdateStockView(UpdateView):
    model = Stock
    success_url = '../../admin/stocks'
    template_name = 'adminpanel/add_stock.html'
    form_class = StockForm


def delete_done(request):
    return render(request, 'adminpanel/delete_done.html')


class HallDeleteView(DeleteView):
    model = Cinema_hall
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_hall.html'


class NewsDeleteView(DeleteView):
    model = News
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_news.html'


class StockDeleteView(DeleteView):
    model = Stock
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_stock.html'


def pages(request):
    context = {
        'contact_page': ContactPage.objects.all(),
        'main_page': MainPage.objects.all(),
        'pages': Page.objects.all().order_by("id"),
    }
    return render(request, 'adminpanel/pages.html', context)


def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pages')
        else:
            print(form.errors)

    form = PageForm()
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_page.html", data)


class UpdatePageView(UpdateView):
    model = Page
    success_url = '../../admin/pages'
    template_name = 'adminpanel/add_page.html'
    form_class = PageForm


class UpdateMainPageView(UpdateView):
    model = MainPage
    success_url = '../../admin/pages'
    template_name = 'adminpanel/edit_main_page.html'
    form_class = MainPageForm


def ContactCinemaList(request):
    data = {
        'contact_cinema': ContactCinema.objects.all()
    }
    return render(request, 'adminpanel/contact.html', data)


def add_film_session(request, hall_id):
    if request.method == 'POST':
        cinema_hall = Cinema_hall.objects.get(id=hall_id)
        form = FilmSessionForm(request.POST)
        if form.is_valid():
            save_to_hall = form.save(commit=False)
            save_to_hall.hall = cinema_hall
            save_to_hall.save()
            return redirect('hall_info', hall_id)
        else:
            print(form.errors)

    form = FilmSessionForm
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_sessionfilm.html", data)


def banners_and_sliders(request):
    Sliders = Slider.objects.all()
    NewsAndStocks = NewsAndStocksBanners.objects.all()
    BackSetting = BackgroundSetting.load()
    Background = BackgroundSetting.objects.get(id=1)

    if request.method == 'POST' and 'add-slider' in request.POST:
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Данные слайдеров сохранены')
        else:
            print('Хьюстон у нас проблемы!!!')
            print(form.errors)
    elif request.method == 'POST' and 'add-news-stock' in request.POST:
        form = NewsAndStocksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Данные новостей и акций сохранены')
        else:
            print('Хьюстон у нас проблемы!!!')
            print(form.errors)
    elif request.method == 'POST' and 'update-background' in request.POST:
        form = BackgroundSettingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Данные фона сохранены')
        else:
            print('Хьюстон у нас проблемы!!!')
            print(form.errors)

    data = {
        'Background': Background,
        'Sliders': Sliders,
        'formSlider': SliderForm(),
        'NewsAndStocks': NewsAndStocks,
        'formNewsAndStock': NewsAndStocksForm(),
        'formBackground': BackgroundSettingForm(),

    }
    return render(request, 'adminpanel/banners_and_sliders.html', data)


def mailing(request):
    return render(request, 'adminpanel/mailing.html')


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email})', message, FROM_EMAIL, EMAIL_ADMIN, fail_silently=False
                          )
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос')
    return render(request, 'adminpanel/email.html', {'form': form})


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')


def select_user_contact(request):
    Users = Profile.objects.filter(~Q(phone=None))

    data = {
        'users': Users
    }

    return render(request, 'adminpanel/select_user_contact.html', data)


class SliderDeleteView(DeleteView):
    model = Slider
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_slider.html'


class BackgroundDeleteView(DeleteView):
    model = BackgroundSetting
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_background.html'


class NewsSliderDeleteView(DeleteView):
    model = NewsAndStocksBanners
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_newsslider.html'


def add_contact_cinema(request):
    if request.method == 'POST':
        form = ContactCinemaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)

    form = ContactCinemaForm()
    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_contact_cinema.html", data)


class UpdateContactCinemaView(UpdateView):
    model = ContactCinema
    success_url = '../../admin/contact'
    template_name = 'adminpanel/add_contact_cinema.html'
    form_class = ContactCinemaForm


class ContactCinemaDeleteView(DeleteView):
    model = ContactCinema
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_contact_cinema.html'


class PageDeleteView(DeleteView):
    model = Page
    success_url = '../../admin/deletedone/'
    template_name = 'adminpanel/delete_page.html'


def save_phone_sms(request):
    print('Зашли в представление')
    if request.method == 'POST':
        print('ПРошли проверу на пост')
        phone_list = request.POST.getlist('phone-list')
        print(phone_list)



    return redirect('mailing')






