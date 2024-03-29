from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http  import HttpResponse
from .forms import NewProfileForm,NewbusinessForm
from  .models import Profile,NeighbourHood,Business

# Create your views here.

def home(request):
    hoods = NeighbourHood.objects.all()
    return render(request,'home.html',{"hoods":hoods})
    
@login_required(login_url='/accounts/login/')
@login_required(login_url='/accounts/login/')
def addprofile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            
            profile.save()
        return redirect('viewprofile')

    else:
        form = NewProfileForm
    return render(request, 'profile.html', {"form": form})
@login_required(login_url='/accounts/login/')
def viewprofile(request,profile_id):
    current_user = request.user
    profile = Profile.objects.filter(user = current_user).first()
    
    return render(request,'viewprofile.html',{'profile':profile})
    return redirect('profile:viewprofile',pk=pk)

@login_required(login_url='/accounts/login/')
def edit_profile(request):
   current_user=request.user
   if request.method =='POST':
       if Profile.objects.filter(user_id=current_user).exists():
           form = NewProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
       else:
           form=NewProfileForm(request.POST,request.FILES)
       if form.is_valid():
           profile=form.save(commit=False)
           profile.username=current_user
           profile.save()
           return redirect('viewprofile', current_user.id)
   else:
       if Profile.objects.filter(user_id = current_user).exists():
           form=NewProfileForm(instance =Profile.objects.get(user_id=current_user))
       else:
           form=NewProfileForm()
   return render(request,'edit_profile.html',{"form":form})   
@login_required(login_url='/accounts/login/')
def business(request):
    
    current_user = request.user
    if request.method == 'POST':
        form = NewbusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            
            business.save()
        return redirect('home')

    else:
        form = NewbusinessForm()
    return render(request, 'business.html', {"form": form})
@login_required(login_url='/accounts/login/')
def viewbusiness(request,location_id):
    bb = Business.objects.all()
    b = Business.objects.filter(location = location.id).first()
    return render(request,'viewbusiness.html',{"bb":bb})
    
    
    