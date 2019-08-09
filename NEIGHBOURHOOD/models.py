from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name=models.Charfield(max_length=30)
    location=models.CharField(max_length=30)
    neighborhood_image=models.ImageField(upload_to='neighborhood/')
    occupants=models.IntegerField()
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    
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