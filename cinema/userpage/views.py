from django.shortcuts import render
from adminpanel.models import Film, FilmSession, Cinema_hall, BackgroundSetting, Slider, NewsAndStocksBanners, MainPage, Cinema
from adminpanel.models import Page, Stock, News
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
    Stock_list = Stock.objects.filter(status_stock=1)

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'stocks': Stock_list,
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
    news_list = News.objects.filter(status_news=1)

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'news_list': news_list,
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


def cinema_info(request, cinema_id):
    CinemaInfo = Cinema.objects.get(id=cinema_id)
    HallInfo = Cinema_hall.objects.filter(cinema_id=cinema_id)
    FilmSessionList = []

    for session in HallInfo:
        FilmSessionList.extend(FilmSession.objects.filter(hall=session.id))

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'cinema': CinemaInfo,
        'halls': HallInfo,
        'session_list': FilmSessionList,
    }

    return render(request, 'userpage/cinema.html', data)


def hall_info(request, hall_id):
    hall_info_all = Cinema_hall.objects.get(id=hall_id)
    session = FilmSession.objects.filter(hall=hall_id)

    row = hall_info_all.row + 1
    col = hall_info_all.col + 1

    rows = range(1, row)
    columns = range(1, col)

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'session': session,
        'hall': hall_info_all,
        'rows': rows,
        'columns': columns,
    }

    return render(request, 'userpage/hall_info.html', data)


def stock_info(request, stock_id):
    stock_info = Stock.objects.get(id=stock_id)

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'stock': stock_info,
    }
    return render(request, 'userpage/stock_info.html', data)


def news_info(request, news_id):
    news_info = News.objects.get(id=news_id)

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'news': news_info,
    }
    return render(request, 'userpage/news_info.html', data)

