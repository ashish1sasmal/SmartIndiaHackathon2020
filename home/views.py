from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    print('heom')
    return render(request,'home/home.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
