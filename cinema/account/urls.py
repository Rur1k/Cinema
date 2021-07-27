from django.urls import path
from account import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('admin/adduser/', views.add_new_user, name='add_user'),
    path('admin/users/', views.users, name='users'),
]