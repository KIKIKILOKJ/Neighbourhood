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

@login_required(login_url='/accounts/login')
def search_business(request):
    if 'biz_name' in request.GET and request.GET['biz_name']:
        search_biz_name = request.GET.get['biz_name']
        business_found=Business.search_business(search_biz_name)
        
        message=f'{search_biz_name}'
        return render(request,'search.html',{"message":message,"bussiness":business_found})
    
    else:
        message="There are no bussinesses by that term in the neighborhood"
        return render(request,'search.html',{"message":message})
    
@login_required(login_url='/accounts/login')
def new_neighborhood(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST,request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.user = current_user
            neighborhood.save()
            return redirect('index')
    else:
        form=NewNeighboroodForm()
        return render(request,'new_neighborhood.html',{"form":form})