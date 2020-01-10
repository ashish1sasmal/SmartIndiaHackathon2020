
from django.urls import path
from . import views

app_name="seller"

urlpatterns = [
    path('signup/',views.register,name='sellersignup'),
    path('login/',views.user_login,name='sellerlogin'),
]
