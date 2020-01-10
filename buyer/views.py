from django.shortcuts import render,redirect
from .forms import UserForm,BuyerSignupForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('buyer:home')

def register(request):
    if request.method=="POST":
        form=UserForm(data=request.POST)
        bform=BuyerSignupForm(data=request.POST)
        if form.is_valid() and bform.is_valid():
            user=form.save(commit=False)
            user.username=form.cleaned_data['email']
            user.save()
            profile=bform.save(commit=False)
            profile.user=user
            profile.save()
            messages.success(request,'Your account has been created !')
            return redirect('home')

        else:
            messages.error(request,'Invalid Input. Kindly Fill again !')
            return redirect('home')

    else:
        form=UserForm()
        bform=BuyerSignupForm()

    return render(request,'buyer_signup.html',{'form':form,'bform':bform})


def user_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active and user.buyerprofile.is_buyer:
                login(request, user)
                messages.success(request, f'You are logged in successfully!')
                return redirect('buyer:home')
                
        else:
            messages.error(request,'Please Check your username and password !')
    return render(request,'buyer_login.html')