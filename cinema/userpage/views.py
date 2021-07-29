from django.shortcuts import render
from adminpanel.models import Film, FilmSession, Cinema_hall
from .models import ReserveAndBuySeats


def main_page(request):
    return render(request, 'userpage/base_userpage.html')


def poster(request):
    context = {
        'films_active': Film.objects.filter(status_film=1),
        'films_pending': Film.objects.filter(status_film=2),
    }
    return render(request, 'userpage/poster.html', context)


def film_details(request, film_id):
    SessionList = FilmSession.objects.filter(film=film_id)
    FilmInfo = Film.objects.get(id=film_id)

    context = {
        'SessionList': SessionList,
        'film': FilmInfo,
    }
    return render(request, 'userpage/film.html', context)


def session_hall_info(request, session_id):
    SessionInfo = FilmSession.objects.get(id=session_id)
    HallInfo = SessionInfo.hall
    FilmInfo = SessionInfo.film

    row = HallInfo.row + 1
    col = HallInfo.col + 1

    rows = range(1, row)
    columns = range(1, col)
    data = {
        'SessionInfo': SessionInfo,
        'HallInfo': HallInfo,
        'FilmInfo': FilmInfo,
        'rows': rows,
        'columns': columns,
    }
    return render(request, 'userpage/hall.html', data)


def save_reserve(request):

    JSON = request.POST.get('checkboxes')

    print(JSON)


    return render(request, 'userpage/test.html')
