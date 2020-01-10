from django.shortcuts import render

# Create your views here.

def hom(request):
    print('heom')
    return render(request,'hom.html')
