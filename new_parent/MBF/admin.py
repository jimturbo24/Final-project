from django.contrib import admin
from .models import CareTaker, Family, Baby, BabyEvent, BreastFed, BottleFed, DiaperStatus, Temperature, Sleep, Wake, Test


admin.site.register(Test)
admin.site.register(CareTaker)
admin.site.register(Family)
admin.site.register(Baby)
admin.site.register(BabyEvent)
admin.site.register(BreastFed)
admin.site.register(BottleFed)
admin.site.register(DiaperStatus)
admin.site.register(Temperature)
admin.site.register(Sleep)
admin.site.register(Wake)
