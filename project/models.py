from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField



# Create your models here.
class Project(models.Model):
    '''
    Class that defines Project attributes
    '''
    title = models.CharField(max_length=50)
    image = CloudinaryField('image')
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,default="" )

    def __str__(self):
        return self.title

    def save_project(self):
        return self.save()

    def delete_project(self):
        return self.delete()

    @classmethod
    def update_title(cls,id,title):
        cls.objects.filter(id=id).update(title=title)
        updated_title = cls.objects.filter(id=id)
        return updated_title

    @classmethod
    def update_description(cls,id,description):
        cls.objects.filter(id=id).update(description=description)
        updated_description = cls.objects.filter(id=id)
        return updated_description

    @classmethod
    def update_link(cls,id,link):
        cls.objects.filter(id=id).update(link=link)
        updated_link = cls.objects.filter(id=id)
        return updated_link

    @classmethod
    def search_project(cls,search_term):
        return Project.objects.filter(title__icontains=search_term)

    @classmethod
    def get_project_by_id(cls,id):
        project = cls.objects.filter(id=id)
        return project
    





class Profile(models.Model):
    '''
    Class that defines Profile attributes
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    bio  =  models.CharField(max_length=100) 
    contact =  models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')


    def __str__(self):
        return self.user

    def save_profile(self):
        return self.save()

    def delete_profile(self):
        return self.delete()

    @classmethod
    def update_bio(cls,id,bio):
        cls.objects.filter(id=id).update(bio=bio)
        updated_bio = cls.objects.filter(id=id)
        return updated_bio


    @classmethod
    def update_contact(cls,id,contact):
        cls.objects.filter(id=id).update(contact=contact)
        updated_contact = cls.objects.filter(id=id)
        return updated_contact

    @classmethod
    def update_profile_pic(cls,id,bio):
        cls.objects.filter(id=id).update(profile_pic=profile_pic)
        updated_profile_pic = cls.objects.filter(id=id)
        return updated_profile_pic

    @receiver(post_save, sender=User)
    def create_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save,sender=User)
    def save_profile(sender,instance, **kwargs):
        instance.profile.save()

class Rating(models.Model):
    design = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    usability =models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    content = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    average = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.design

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    
    def average(self):
        avg = (self.design+ self.usability+ self.content)/3
        return avg
