from django.urls import path
from account import views
from userpage.views import register_done, login_error

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('admin/adduser/', views.add_new_user, name='add_user'),
    path('admin/users/', views.users, name='users'),
    path('admin/deleteuser/<int:pk>', views.UserDeleteView.as_view(), name='delete_user'),
    path('admin/edituser/<int:user_id>', views.UpdateUserView, name='edit_user'),
    path('register/done', register_done, name='register_done'),
    path('login_error/', login_error, name='login_error'),
]