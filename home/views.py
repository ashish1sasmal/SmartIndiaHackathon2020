from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.

def home(request):
    print('heom')
    return render(request,'home/home.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001ccc5a88319d2459f7a6636ac3d094690&format=json&offset=0&limit=10000"

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


def checkprice(request):
    if request.method=="POST":
        loc=request.POST.get('state')
        l=price(loc)
        print(loc)
        return render(request,'home/result.html',{'price':l[0],'date':l[1]})
    else:
        return render(request,'home/checkprice.html')
