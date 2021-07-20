from django.contrib import admin
from .models import Film, Format_film, Genre_film, Status_film, Cinema, Status_main, Page, MainPage, ContactPage

admin.site.register(Film)
admin.site.register(Format_film)
admin.site.register(Genre_film)
admin.site.register(Status_film)
admin.site.register(Cinema)
admin.site.register(Status_main)
admin.site.register(Page)
admin.site.register(MainPage)
admin.site.register(ContactPage)


