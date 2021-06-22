from django.shortcuts import render, redirect
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