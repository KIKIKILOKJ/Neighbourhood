from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Profile,Business

# Create your views here.
def index(request):
    neighborhood=Neighborhood.objects.all()
    title='The Neighborhood'
    return render(request,'index.html',{"title":title,"neighborhood":neighborhood})

@login_required(login_url='/accounts/login')
def neighborhood(request,neighborhood_id):
    neighborhood=Neighborhood.objects.filter(id=neighborhood_id)
    results=Business.objects.filter(neighborhood=neighborhood_id)
    return render(request,'neighborhood.html',{"neighborhood":neighborhood,"results":results})

@login_required(login_url='/accounts/login')
def user_profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=current_user)
    return render(request,'profile.html',{"profile":profile})