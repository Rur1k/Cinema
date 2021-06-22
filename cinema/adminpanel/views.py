from django.shortcuts import render
from .models import Film
from .forms import FilmForm

def admin(request):
    return render(request, 'adminpanel/statistics.html')

def films(request):
    context = {
       'films': Film.objects.all()
    }
    return render(request, 'adminpanel/films.html', context)

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            new_film = form.save(commit=False)
            new_film.save()
            return redirect('films')
        else:
            return render(request, "adminpanel/add_film.html")
    else:
        form = FilmForm()
        data = {
            'form': form,
        }
        return render(request, "adminpanel/add_film.html", data)