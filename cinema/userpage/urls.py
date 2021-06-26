from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='mainpage'),
    path('hall/', views.hall, name='hall'),
    path('poster/', views.poster, name='poster'),
    path('film/<int:film_id>', views.film_details, name='film_details'),
]