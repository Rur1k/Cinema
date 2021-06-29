from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('films/', views.films, name='films'),
    path('addfilm/', views.add_film, name='add_film'),
    path('edit/<int:pk>', views.UpdateFilmView.as_view(), name='editfilm'),
    path('cinemas/', views.cinemas, name='cinemas'),
    path('addcinema/', views.add_cinema, name='add_cinema'),
    path('cinema/<int:cinema_id>', views.cinema_info, name='cinema_info'),
    path('editcinema/<int:pk>', views.UpdateCinemaView.as_view(), name='edit_cinema'),
    path('cinema/<int:cinema_id>/addhall', views.add_cinema_hall, name='add_hall'),
    path('cinema/hall/<int:hall_id>', views.hall_info, name='hall_info'),
    path('edit_hall/<int:pk>', views.UpdateCinemaHallView.as_view(), name='edit_hall'),
]