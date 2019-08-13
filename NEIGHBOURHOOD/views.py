from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Profile,Business
from .forms import NewNeighborhoodForm,EditProfileForm,NewBusinessForm

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
def profile(request):
    user = User.objects.all()
    for user in user:
        profile=Profile.objects.all()
        neighborhood=Neighborhood.objects.all()
        print (user)
    return render(request,'profile.html',{ "user": user,"profile":profile,"neighborhood":neighborhood})

@login_required(login_url='/accounts/login')
def search_business(request):
    if 'biz_name' in request.GET and request.GET['biz_name']:
        search_biz_name = request.GET.get['biz_name']
        business_found=Business.search_business(search_biz_name)
        
        message=f'{search_biz_name}'
        return render(request,'search.html',{"message":message,"bussiness":business_found})
    
    else:
        message="There is no bussines by that term in the neighborhood"
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
        form=NewNeighborhoodForm()
        return render(request,'new_neighborhood.html',{"form":form})

@login_required(login_url='/accounts/login')
def edit_profile(request):
    current_user =  request.user 
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile_picture=form.cleaned_data['profile_picture']
            name=form.cleaned_data['name']
            email= form.cleaned_data['email']
            Profile.objects.filter(user=current_user).update(profile_picture=profile_picture,name=name,email=email)

            profile.save()
            return redirect('user_profile')
    else:
        form = EditProfileForm()
            
    return render(request,'edit_profile.html',{'form':form})

@login_required(login_url='/accounts/login')
def new_business(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect ('index')
    else:
        form = NewBusinessForm()
        return render(request,'new_business.html',{"form":form})