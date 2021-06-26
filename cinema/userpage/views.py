from django.shortcuts import render
from adminpanel.models import Film


def main_page(request):
    return render(request, 'userpage/base_userpage.html')

def hall(request):
    rows = range(1, 13)
    columns = range(1, 21)
    data = {
        'rows': rows,
        'columns': columns,
    }

    return render(request, 'userpage/hall.html', data)


def poster(request):
    context = {
        'films_active': Film.objects.filter(status_film=1),
        'films_pending': Film.objects.filter(status_film=2),
    }
    return render(request, 'userpage/poster.html', context)


def film_details(request, film_id):
    context = {
        'film': Film.objects.get(id=film_id)
    }
    return render(request, 'userpage/film.html', context)
