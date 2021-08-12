from django.shortcuts import render, redirect
from adminpanel.models import Film, FilmSession, Cinema_hall, BackgroundSetting, Slider, NewsAndStocksBanners, MainPage, Cinema
from adminpanel.models import Page, Stock, News, ContactCinema, Ticket
from account.models import Profile, User
from .models import SeatsReserveAndBuy, StatusSeat
from account.forms import UserForm, ProfileForm
import datetime
import random


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
    randon_number = random.randint(1, 999999999999999)
    SeatList = []
    TicketList = []

    print('Зашли в представление')

    if request.method == 'POST':
        print('прошли проверу на пост запрос')
        status = 0
        CheckSeat = request.POST.getlist('SeatList')
        print(CheckSeat)

        if request.POST.get('save') == 'reserve':
            status = StatusSeat.objects.get(id=1)
        elif request.POST.get('save') == 'buy':
            status = StatusSeat.objects.get(id=2)
        else:
            print('Не определенно')

        for seat in Seats:
            SeatList.append(seat.seat)

        for seat in CheckSeat:
            if seat in SeatList:
                print('Уже забронировано/куплено')
            else:
                print('Места нет, можно бронировать')
                saveSeat = SeatsReserveAndBuy.objects.create(session=session, seat=seat, status_seat=status)
                saveSeat.save()

                rowAndSet = seat.split('-')
                row = rowAndSet[0]
                seat = rowAndSet[1]
                if request.user.is_authenticated:
                    user = request.user.pk
                else:
                    user = 1
                saveTicket = Ticket.objects.create(film_session=session, row=row, seat=seat, status=status.id, user_id=user)
                TicketList.append(saveTicket)
                saveTicket.save()
                print(TicketList)

    else:
        print('НЕ прошли проверку пост')

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'tickets': TicketList,
        'random': randon_number,
    }

    if request.POST.get('save') == 'reserve':
        return render(request, 'userpage/reserve.html', data)
    elif request.POST.get('save') == 'buy':
        return render(request, 'userpage/buy_ticket.html', data)
    else:
        return render(request, 'userpage/test.html', data)



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
    contacts_list = ContactCinema.objects.all()

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),
        'contacts': contacts_list,
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


def user_account(request, user_id):
    ProfileInfo = Profile.objects.get(user=user_id)
    TicketList = Ticket.objects.filter(user_id=user_id)

    for ticket in TicketList:
        print(ticket.status)

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),

        'profile': ProfileInfo,
        'tickets': TicketList,
    }
    return render(request, 'userpage/user_account.html', data)


def UpdateUserViewUserPage(request, user_id):
    UserInfo = User.objects.get(id=user_id)
    ProfileInfo = Profile.objects.get(user=user_id)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pseudonym = request.POST.get('pseudonym')
        address = request.POST.get('address')
        card_number = request.POST.get('card_number')
        language = request.POST.get('language')
        male = request.POST.get('male')
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        city = request.POST.get('city')

        User.objects.filter(id=user_id).update(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        Profile.objects.filter(user=user_id).update(
                pseudonym=pseudonym,
                address=address,
                card_number=card_number,
                language=language,
                male=male,
                phone=phone,
                birth_date=birth_date,
                city=city
        )

        return redirect('user_account', user_id=user_id)

    user_form = UserForm(initial={
        'username': UserInfo.username,
        'email': UserInfo.email,
        'password': UserInfo.password,
        'first_name': UserInfo.first_name,
        'last_name': UserInfo.last_name,
    })
    profile_form = ProfileForm(initial={
        'pseudonym': ProfileInfo.pseudonym,
        'address': ProfileInfo.address,
        'card_number': ProfileInfo.card_number,
        'language': ProfileInfo.language,
        'male': ProfileInfo.male,
        'phone': ProfileInfo.phone,
        # 'birth_date': ProfileInfo.birth_date,
        'city': ProfileInfo.city,
    })

    data = {
        'pages': Page.objects.filter(status_page=1),
        'MainInfo': MainPage.objects.get(id=1),
        'backgroundSite': backSetting(),

        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'userpage/edit_user.html', data)




