from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Profile,Business

# Create your views here.
def index(request):
    neighborhood=Neighborhood.objects.all()
    title='The Neighborhood'
    return render(request,'index.html',{"title":title,"neighborhood":neighborhood})