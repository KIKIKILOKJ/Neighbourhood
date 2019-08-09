from django import forms
from .models import Neighborhood,Profile,Business

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        exclude=['admin']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']
        
class NewBusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user']