from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('films/', views.films, name='films'),
    path('addfilm/', views.add_film, name='add_film'),
    path('edit/<int:pk>', views.UpdateFilmView.as_view(), name='editfilm'),
    path('delete_film/<int:pk>', views.FilmDeleteView.as_view(), name='delete_film'),
    path('cinemas/', views.cinemas, name='cinemas'),
    path('addcinema/', views.add_cinema, name='add_cinema'),
    path('cinema/<int:cinema_id>', views.cinema_info, name='cinema_info'),
    path('editcinema/<int:pk>', views.UpdateCinemaView.as_view(), name='edit_cinema'),
    path('cinema/<int:cinema_id>/addhall', views.add_cinema_hall, name='add_hall'),
    path('cinema/hall/<int:hall_id>', views.hall_info, name='hall_info'),
    path('edit_hall/<int:pk>', views.UpdateCinemaHallView.as_view(), name='edit_hall'),
    path('news/', views.news_list, name='news'),
    path('addnews/', views.add_news, name='add_news'),
    path('editnews/<int:pk>', views.UpdateNewsView.as_view(), name='edit_news'),
    path('stocks/', views.stocks, name='stocks'),
    path('addstock/', views.add_stock, name='add_stock'),
    path('editstock/<int:pk>', views.UpdateStockView.as_view(), name='edit_stock'),
    path('deletedone/', views.delete_done, name='delete_done'),
    path('delete_hall/<int:pk>', views.HallDeleteView.as_view(), name='delete_hall'),
    path('delete_news/<int:pk>', views.NewsDeleteView.as_view(), name='delete_news'),
    path('delete_stock/<int:pk>', views.StockDeleteView.as_view(), name='delete_stock'),
    path('pages/', views.pages, name='pages'),
]