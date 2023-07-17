from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.



class Moderator(AbstractBaseUser):
    #Moderator_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    location = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    email=models.EmailField()


    # Other fields specific to Moderator model

    def __str__(self):
        return self.username

class User(AbstractBaseUser):
    #User_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    username =models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=128)
    phone_no =models.CharField(max_length=100,unique=True) 
    location =models.CharField(max_length=150)
    user_image =models.ImageField(upload_to="userProfile") 
    dob =models.DateField(null=True)
    user_bio=models.CharField(max_length=150)
    type=models.CharField(max_length=100,default='user') 
    address=models.CharField(max_length=300)

    def __str__(self):
        return self.username

class Worker(AbstractBaseUser):
    #Worker_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    username =models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=128)
    phone_no =models.CharField(max_length=100,unique=True)
    location =models.CharField(max_length=150)
    user_image =models.ImageField(upload_to="workerProfile") 
    dob =models.DateField(null=True)
    user_bio=models.CharField(max_length=150)
    type=models.CharField(max_length=100,default='worker') 
    address=models.CharField(max_length=300)
    
    job_title=models.CharField(max_length=150,null= True)
    catagory=models.CharField(max_length=150,null= True)
    experience=models.CharField(max_length=150,null= True)
    skill_1 =models.CharField(max_length=150,null= True)
    skill_2 =models.CharField(max_length=150,null= True)
    skill_3 =models.CharField(max_length=150,null= True)
    id_proof=models.ImageField(upload_to="workerProfile")
    exp_proof=models.ImageField(upload_to="workerProfile")
    cv=models.ImageField(upload_to="workerProfile")

    is_approved=models.BooleanField(null= True)
    status=models.BooleanField(null= True)
    report=models.BooleanField(null= True)

    def __str__(self):
        return self.username

class login(models.Model):
    username =models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.username



 #class job_post(models.Model):
    #post_id=models.CharField(max_length=200,primary_key=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)