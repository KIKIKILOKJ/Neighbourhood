from django.test import TestCase
from .models import Neighborhood,Profile,Business
# Create your tests here.

class HoodTestClass(TestCase):
    def setUp(self):    
        #Neighborhood
        self.japan = Neighborhood(name='japan',neighborhood_image='japan.jpg',members='150')
        self.japan.save()
        #Neighbor
        self.peter = Profile(name='Peter',email='petermax2004@gmail.com',profile_picture='wamlambez.jpeg',user=self.peter,neighborhood=self.japan)
        self.peter.save()
        #Business
        self.mutura = Business(description ='Spacious and well aerated',name='Check',business_mail='check@gym.com',user=self.peter,neighborhood=self.japan)
        self.mutura.save()
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gym,Business))
        self.assertTrue(isinstance(self.jem,NeighborProfile))
        self.assertTrue(isinstance(self.parklands,Neighborhood))

    #Destroying the instance after test
    def tearDown(self):
        Business.object.all().delete()
        NeighborProfile.object.all().delete()
        Neighborhood.object.all().delete()