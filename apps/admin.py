from django.contrib import admin
from .models import TodayUser, Poster, Comment

admin.site.register(TodayUser)
admin.site.register(Poster)
admin.site.register(Comment)

# Register your models here.
