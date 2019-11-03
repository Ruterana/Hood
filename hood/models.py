from django.db import models
from django.contrib .auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField(upload_to = 'pictures/')
    bio= models.CharField(max_length=30)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    username= models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    neighbourhood = models.CharField(max_length=32,null= True)
def save_profile(self):
        self.save()
def delete_neighbourhood(self):
        self.delete()  
class post(models.Model):
    name= models.CharField(max_length=30)  
    user= models.ForeignKey(User)
    post = HTMLField()
    image_path = models.ImageField(upload_to = 'pictures/')
def __str__(self):
        return self.name

def save_post(self):
        self.save() 
class NeighbourHood(models.Model):
    image_path = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length=30)
    location= models.CharField(max_length=32)
    count  = models.IntegerField(default=0)
def __str__(self):
        return self.name

def save_neighbourhood(self):
        self.save() 

def delete_neighbourhood(self):
        self.delete()  

class Business(models.Model):
      owner = models.CharField(max_length=30)
      business_name= models.CharField(max_length=32)
      business_email =models.EmailField(max_length=300)
      description= models.TextField(max_length=300)
      location = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE) 
      user = models.ForeignKey(User,on_delete=models.CASCADE) 
    
def create_business(self):
        self.save()
      
def delete_business(self):
        self.delete()
def __str__(self):
    return self.location