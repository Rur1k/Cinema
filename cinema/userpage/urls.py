from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('session_film/<int:session_id>', views.session_hall_info, name='session_hall_info'),
    path('poster/', views.poster, name='poster'),
    path('film/<int:film_id>', views.film_details, name='film_details'),
    path('request/', views.save_reserve, name='save_reserve'),
]