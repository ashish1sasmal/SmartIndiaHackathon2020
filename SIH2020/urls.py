"""SIH2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from buyer import views as bv
from django.conf import settings
from django.conf.urls.static import static

from home import views as hv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyer/',include(('buyer.urls','buyer'),namespace='buyer')),
    path('seller/',include('seller.urls')),
    path('',include('home.urls')),
    path('logout/',hv.user_logout,name='logout'),
    # path('logistic/',include('logistic.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
