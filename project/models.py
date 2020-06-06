from django.db import models

# Create your models here.
class Project(models.Model):
    '''
    Class that defines Project attributes
    '''
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='project/')
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)



class Profile(models.Model):
    '''
    Class that defines Profile attributes
    '''
    user = models.CharField(max_length=50)
    bio  =  models.CharField(max_length=100) 
    contact =  models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='project/')






