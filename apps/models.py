from django.db import models
from django.contrib.auth.models import  AbstractUser


class TodayUser(AbstractUser):
    is_admin = models.BooleanField(name='today_admin',default=False)
    is_active_number = models.BooleanField(default=False)
    is_number = models.BooleanField(default=True)
    img = models.ImageField(blank=True)

    REQUIRED_FIELDS = ["email","first_name","last_name","today_admin","is_active_number","is_number"]

class Poster(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(TodayUser,on_delete=models.CASCADE)
    
class Event(Poster):
    start_date = models.DateField()
    end_date = models.DateField()

class Trip(Poster):
    date = models.DateField()
    price = models.PositiveIntegerField()
    
class Picture(models.Model):
    img = models.ImageField()
    poster = models.ForeignKey(Poster,on_delete= models.CASCADE)

