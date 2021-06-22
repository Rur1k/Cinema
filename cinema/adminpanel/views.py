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
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films')

    form = FilmForm()

    data = {
        'form': form,
    }
    return render(request, "adminpanel/add_film.html", data)