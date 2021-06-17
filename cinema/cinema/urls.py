from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('userpage.urls')),
    path('admin/', include('adminpanel.urls')),
    path('account/', include('account.urls')),
]
