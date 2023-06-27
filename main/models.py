from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class customUser(AbstractUser):
    username =models.CharField(max_length=100,unique=True)
    phone_no =models.CharField(max_length=100,unique=True)
    location =models.CharField(max_length=150)
    user_image =models.ImageField(upload_to="userProfile") 
    dob =models.DateField(null=True)
    user_bio=models.CharField(max_length=150)
    type=models.CharField(max_length=100,default='user') 
    address=models.CharField(max_length=300)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS=[]