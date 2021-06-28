from django.contrib import admin
from .models import Film, Format_film, Genre_film, Status_film, Cinema

admin.site.register(Film)
admin.site.register(Format_film)
admin.site.register(Genre_film)
admin.site.register(Status_film)
admin.site.register(Cinema)


