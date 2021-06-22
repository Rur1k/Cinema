from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('films/', views.films, name='films'),
    path('addfilm/', views.add_film, name='add_film'),
]