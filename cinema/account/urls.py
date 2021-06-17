from django.urls import path
from account import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
]