from django.contrib import admin
from .models import *
from userpage.models import StatusSeat, SeatsReserveAndBuy

admin.site.register(Film)
admin.site.register(Format_film)
admin.site.register(Genre_film)
admin.site.register(Status_film)
admin.site.register(Cinema)
admin.site.register(Status_main)
admin.site.register(Page)
admin.site.register(MainPage)
admin.site.register(ContactPage)
admin.site.register(FilmSession)
admin.site.register(Slider)
admin.site.register(BackgroundSetting)

admin.site.register(StatusSeat)
admin.site.register(SeatsReserveAndBuy)


