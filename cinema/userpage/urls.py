from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('session_film/<int:session_id>', views.session_hall_info, name='session_hall_info'),
    path('poster/', views.poster, name='poster'),
    path('film/<int:film_id>', views.film_details, name='film_details'),
    path('request/<int:session_id>', views.save_reserve, name='save_reserve'),
    path('timetable/', views.timetable, name='timetable'),
    path('soon/', views.soon, name='soon'),
    path('cinemas/', views.cinemas, name='our_cinemas'),
    path('stocks/', views.stocks, name='our_stocks'),
    path('contacts/', views.contacts, name='our_contacts'),
    path('news/', views.news, name='our_news'),
    path('page/<int:page_id>', views.our_page, name='our_page'),
    path('cinema/<int:cinema_id>', views.cinema_info, name='cinema_userpage'),
    path('cinema/hall/<int:hall_id>', views.hall_info, name='hall_info_userpage'),
    path('stock/<int:stock_id>', views.stock_info, name='stock_info_userpage'),
    path('news_info/<int:news_id>', views.news_info, name='news_info_userpage'),
]