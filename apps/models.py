from datetime import date
from turtle import title
from django.db import models
from django.contrib.auth.models import  AbstractUser


class TodayUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True )
    is_admin = models.BooleanField(default=False ,blank=False)
    is_active_number = models.BooleanField(default=False ,blank=False)
    is_number = models.BooleanField(default=True ,blank=False)
    date_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True,default='here')
    img = models.ImageField(blank=True,upload_to='./media')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","username"]

class Poster(models.Model):
    title = models.CharField(max_length=200)
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
    img = models.ImageField(upload_to='./media/postes')
    poster = models.ForeignKey(Poster,on_delete= models.CASCADE)

