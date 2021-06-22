from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('userpage.urls'), name='mainpage'),
    path('admin/', include('adminpanel.urls')),
    path('account/', include('account.urls')),
    path('admin_test/', admin.site.urls),
]
