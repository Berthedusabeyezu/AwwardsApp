from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(upload_to = 'images/')
    bio = models.TextField()
    project = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length =60)

    def __str__(self):
        return self.image 
   
    def save_profile(self):
        self.save()  
      
    def delete_profile(self):  
        self.delete()
           
    def update_profile(self, update):
        self.image = update  
        self.save()
    


class Project(models.Model):
    title = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.project

    
    def save_project(self):
        self.save()  

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_project(cls,search_term):
        project = cls.objects.filter(project_title__icontains = search_term)
        return project
    
