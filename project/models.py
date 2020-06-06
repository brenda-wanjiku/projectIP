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





class Profile(models.Model):
    '''
    Class that defines Profile attributes
    '''
    user = models.CharField(max_length=50)
    bio  =  models.CharField(max_length=100) 
    contact =  models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='project/')


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


