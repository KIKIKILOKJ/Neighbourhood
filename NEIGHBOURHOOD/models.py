from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Neighborhood(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    neighborhood_image=models.ImageField(upload_to='neighborhood/')
    occupants=models.IntegerField()
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    
    @classmethod
    def view_neighborhood(cls,neighborhood_id):
        neighborhood=cls.objects.filter(id=neighborhood_id)
        return neighborhood
    
    def __str__(self):
        return self.name
    
    def create_neighborhood(self):
        self.create()
        
    def delete_neighborhood(self):
        self.delete()
        
    def find_neighborhood(self):
        self.find()
        
    def update_neighborhood(self):
        self.update()
        
    def update_occupants(self):
        self.update()
        
    
    
class Business(models.Model):
    biz_name=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    description=HTMLField
    biz_email=models.EmailField(max_length=300)
    
    @classmethod
    def search_business(cls,search_biz_name):
        results = cls.objects.filter(name__icontains=search_biz_name)
        return results
    
    def __str__(self):
        return self.biz_name
    
    def create_business(self):
        self.create()
        
    def delete_business(self):
        self.delete()
    
    def find_business(self):
        self.find()
        
    def update_business(self):
        self.update()
        
class Profile(models.Model):
    name=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profiles/')
    email=models.EmailField(max_length=300)
    
    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()