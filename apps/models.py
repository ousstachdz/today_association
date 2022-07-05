from importlib.resources import contents
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
    type = models.CharField(max_length=10)
    date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    price = models.PositiveIntegerField( null=True, blank=True)
    img = models.ImageField(upload_to='./media/postes' ,null=True, blank=True)

class Comment(models.Model):
    owner = models.ForeignKey(TodayUser,on_delete=models.CASCADE, default=1)
    post =  models.ForeignKey(Poster,on_delete=models.CASCADE, default=1)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    