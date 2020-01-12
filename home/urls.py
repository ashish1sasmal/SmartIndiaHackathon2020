
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('aboutus/',views.about,name='about'),
    path('checkprice/',views.checkprice,name='check'),
]


#AIzaSyCQvKXOnYbsExXlMe-TnudIwupJeejmE8o
