from django.shortcuts import render
from adminpanel.models import Film, FilmSession, Cinema_hall, BackgroundSetting, Slider, NewsAndStocksBanners, MainPage, Cinema
from adminpanel.models import Page
from .models import SeatsReserveAndBuy, StatusSeat
import datetime


def backSetting():
    background = BackgroundSetting.objects.get(pk=1)
    if background.backgroundOn == 1:
        return background.backgroundImg
    else:
        return background.backgroundDefault


def main_page(request):
    Sliders = Slider.objects.all()
    SliderOne = Slider.objects.all()[:1]
    now = datetime.datetime.now()

    NewsAndStocks = NewsAndStocksBanners.objects.all()
    NewsAndStocksOne = NewsAndStocksBanners.objects.all()[:1]

    context = {
        'pages': Page.objects.filter(status_page=1),
        'date': now.strftime("%d.%m"),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'Sliders': Sliders,
        'SliderOne': SliderOne,
        'NewsAndStocks': NewsAndStocks,
        'NewsAndStocksOne': NewsAndStocksOne,
        'films_active': Film.objects.filter(status_film=1),
        'films_pending': Film.objects.filter(status_film=2),
    }
    return render(request, 'userpage/mainpage.html', context)


def poster(request):
    context = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'films_active': Film.objects.filter(status_film=1),
        'films_pending': Film.objects.filter(status_film=2),
        'backgroundSite': backSetting()
    }
    return render(request, 'userpage/poster.html', context)


def film_details(request, film_id):
    SessionList = FilmSession.objects.filter(film=film_id)
    FilmInfo = Film.objects.get(id=film_id)

    context = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'SessionList': SessionList,
        'film': FilmInfo,
        'backgroundSite': backSetting()
    }
    return render(request, 'userpage/film.html', context)


def session_hall_info(request, session_id):
    SessionInfo = FilmSession.objects.get(id=session_id)
    SessionID = FilmSession.objects.filter(id=session_id)
    HallInfo = SessionInfo.hall
    FilmInfo = SessionInfo.film
    BusySeats = SeatsReserveAndBuy.objects.filter(session=session_id)

    BusySeatsList = []

    for seat in BusySeats:
        BusySeatsList.append(seat.seat)

    row = HallInfo.row + 1
    col = HallInfo.col + 1

    rows = range(1, row)
    columns = range(1, col)
    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'BusySeats': BusySeatsList,
        'sessionId': SessionID,
        'SessionInfo': SessionInfo,
        'HallInfo': HallInfo,
        'FilmInfo': FilmInfo,
        'rows': rows,
        'columns': columns,
        'backgroundSite': backSetting()
    }
    return render(request, 'userpage/hall.html', data)


def save_reserve(request, session_id):
    Seats = SeatsReserveAndBuy.objects.filter(session=session_id)
    session = FilmSession.objects.get(id=session_id)
    status = StatusSeat.objects.get(id=1)
    SeatList = []

    print('Зашли в представление')

    if request.method == 'POST':
        print('прошли проверу на пост запрос')
        CheckSeat = request.POST.getlist('SeatList')
        print(CheckSeat)

        for seat in Seats:
            SeatList.append(seat.seat)

        for seat in CheckSeat:
            if seat in SeatList:
                print('Уже забронировано/куплено')
            else:
                print('Места нет, можно бронировать')
                saveSeat = SeatsReserveAndBuy.objects.create(session=session, seat=seat, status_seat=status)
                saveSeat.save()

    else:
        print('НЕ прошли проверку пост')

    return render(request, 'userpage/test.html')


def timetable(request):
    Session = FilmSession.objects.all()

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'session_list': Session,
    }

    return render(request, 'userpage/timetable.html', data)


def soon(request):
    context = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'films_pending': Film.objects.filter(status_film=2),
        'backgroundSite': backSetting()
    }
    return render(request, 'userpage/soon.html', context)


def cinemas(request):
    context = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'cinemas': Cinema.objects.all(),
    }
    return render(request, 'userpage/cinemas.html', context)


def stocks(request):

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
    }
    return render(request, 'userpage/stocks.html', data)


def contacts(request):

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
    }
    return render(request, 'userpage/contact.html', data)


def news(request):

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
    }
    return render(request, 'userpage/news.html', data)


def our_page(request, page_id):
    PageInfo = Page.objects.get(id=page_id)

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'page': PageInfo,
    }
    return render(request, 'userpage/page.html', data)

