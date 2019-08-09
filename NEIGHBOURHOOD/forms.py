from django import forms
from .models import Neighborhood,Profile

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        exclude=['admin']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']