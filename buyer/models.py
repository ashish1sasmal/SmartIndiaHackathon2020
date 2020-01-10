from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils.crypto import get_random_string

def generateUUID():
    return str(uuid4())
# Create your models here.

class BuyerProfile(models.Model):
    bid=models.CharField(max_length=10, blank=True, unique=True, default='B'+get_random_string(8).upper())
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    gst_no=models.IntegerField()
    company_name=models.CharField(max_length=30)
    is_buyer=models.BooleanField(default=True)
    is_seller=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
