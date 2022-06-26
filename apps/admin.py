from django.contrib import admin
from .models import TodayUser, Poster, Event, Trip, Picture

admin.site.register(TodayUser)
admin.site.register(Poster)
admin.site.register(Event)
admin.site.register(Trip)
admin.site.register(Picture)

# Register your models here.
