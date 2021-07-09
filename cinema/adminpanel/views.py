from django.shortcuts import render, redirect
from .models import Film, Cinema, Cinema_hall
from .forms import FilmForm, CinemaForm, CinemaHallForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.forms import formset_factory

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
        form = CinemaHallForm(request.POST, request.FILES)
        if form.is_valid():
            save_to_cinema = form.save(commit=False)
            save_to_cinema.cinema_id = cinema_id
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
    row = hall_info_all.row + 1
    col = hall_info_all.col + 1

    rows = range(1, row)
    columns = range(1, col)

    data = {
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

