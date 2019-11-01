from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http  import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to  the neiborhood app')
def home(request):
    return render(request, 'home.html')
# @login_required(login_url='/accounts/login/')