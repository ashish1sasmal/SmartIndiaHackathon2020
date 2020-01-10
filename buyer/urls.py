
from django.urls import path
from . import views

app_name="buyer"

urlpatterns = [
    path('home/',views.home,name='home'),
    path('signup/',views.register,name='buyersignup'),
    path('login/',views.user_login,name='buyerlogin'),
]
