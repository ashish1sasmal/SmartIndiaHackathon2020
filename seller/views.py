from django.shortcuts import render,redirect
from .forms import UserForm,SellerSignupForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import requests
import json
from buyer.models import BuyerProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001ccc5a88319d2459f7a6636ac3d094690&format=json&offset=0&limit=10000"
l=0


def price(loc):
    r = requests.request("GET", url)
    data=r.json()
    l={}
    f=9
    for i in range(int(data['count'])):
        if data['records'][i]['state']==loc:
                l[str(i)]=data['records'][i]
                f=1

    return([l,data['updated_date']])


def dashboard(request):
    return render(request,'seller/seller_dashboard.html')

def sell(request):
    state=None
    district=None
    commodity=None
    seller=None
    d=None
    s=None
    if request.method=='POST':
        commodity=request.POST.get('commodity')
        district=request.POST.get('district')
        state=request.POST.get('state')


        if district==None:
            district=BuyerProfile.objects.filter(state=state,commodity=commodity).values_list('district',flat=True)
        else:
            d='true'
            seller=BuyerProfile.objects.filter(state=state,commodity=commodity,district=district)


    print(commodity,state,district)
    return render(request,'seller/sell.html',{'commodity':commodity,'state':state,'districts':district,'sellers':seller,'d':d,'s':s})



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
            return redirect('home')

        else:
            print(form.errors)
            print(sform.errors)
            messages.error(request,'Invalid Input. Kindly Fill again !')
            return redirect('home')

    else:
        form=UserForm()
        sform=SellerSignupForm()

    return render(request,'seller/seller_signup.html',{'form':form,'sform':sform})


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
                return redirect('home')

        else:
            messages.error(request,'Please Check your username and password !')
    return render(request,'seller/seller_login.html')
