from django.shortcuts import render, redirect
from .models import Film, Cinema
from .forms import FilmForm, CinemaForm
from django.views.generic import DetailView, UpdateView, DeleteView

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
            form.save()
            return redirect('films')
        else:
            print(form.errors)

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
    context = {
        'cinema': Cinema.objects.get(id=cinema_id)
    }
    return render(request, 'adminpanel/cinema.html', context)

class UpdateCinemaView(UpdateView):
    model = Cinema
    success_url = '../../admin/cinemas'
    template_name = 'adminpanel/add_cinema.html'
    form_class = CinemaForm
