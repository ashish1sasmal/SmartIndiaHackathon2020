from django.shortcuts import render,redirect
from .forms import UserForm,SellerSignupForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
# Create your views here.

    


def register(request):
    if request.method=="POST":
        form=UserForm(data=request.POST)
        sform=SellerSignupForm(data=request.POST)
        if form.is_valid() and sform.is_valid():
            user=form.save(commit=False)
            user.username=form.cleaned_data['email']
            user.save()
            profile=sform.save(commit=False)
            profile.user=user
            profile.save()
            messages.success(request,'Your account has been created !')
            return redirect('buyer:home')

        else:
            print(form.errors)
            print(sform.errors)
            messages.error(request,'Invalid Input. Kindly Fill again !')
            return redirect('buyer:home')

    else:
        form=UserForm()
        sform=SellerSignupForm()

    return render(request,'seller_signup.html',{'form':form,'sform':sform})


def user_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active and user.sellerprofile.is_seller:
                login(request, user)
                messages.success(request, f'You are logged in successfully!')
                return redirect('buyer:home')
                
        else:
            messages.error(request,'Please Check your username and password !')
    return render(request,'seller_login.html')