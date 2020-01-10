from django import forms
from .models import BuyerProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email=forms.EmailField()
    class meta:
        model=User
        fields=['email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={ 'placeholder': 'Email Address '})
        self.fields['password1'].widget = forms.PasswordInput(attrs={ 'placeholder': 'Enter Password '})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password confirmation'})
        self.fields.pop('username')

class BuyerSignupForm(forms.ModelForm):
    class Meta:
        model=BuyerProfile
        fields=['first_name','last_name','phone','gst_no','company_name']

    def __init__(self, *args, **kwargs):
        super(BuyerSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget=forms.TextInput(attrs={'id':'firstname','placeholder':'First Name','required':'required'})
        self.fields['last_name'].widget=forms.TextInput(attrs={'id':'lastname','placeholder':'Last Name','required':'required'})
        self.fields['phone'].widget=forms.TextInput(attrs={'id':'phone','placeholder':'Phone No.','required':'required'})
        self.fields['gst_no'].widget=forms.TextInput(attrs={'id':'gst','required':'required'})
        self.fields['company_name'].widget=forms.TextInput(attrs={'id':'company','placeholder':'Enter','required':'required'})
