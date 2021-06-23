from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm
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