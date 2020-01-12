from django import forms
from .models import SellerProfile
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

class SellerSignupForm(forms.ModelForm):
    class Meta:
        model=SellerProfile
        fields=['first_name','last_name','phone','district','aadhar','state']

    def __init__(self, *args, **kwargs):
        super(SellerSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget=forms.TextInput(attrs={'id':'firstname','placeholder':'First Name','required':'required'})
        self.fields['last_name'].widget=forms.TextInput(attrs={'id':'lastname','placeholder':'Last Name','required':'required'})
        self.fields['phone'].widget=forms.TextInput(attrs={'id':'contact','placeholder':'Contact No.','required':'required'})
        self.fields['district'].widget=forms.TextInput(attrs={'id':'district','placeholder':'District','required':'required'})
        self.fields['aadhar'].widget=forms.TextInput(attrs={'id':'aadhar','placeholder':'Aadhar','required':'required'})
        self.fields['state'].widget=forms.TextInput(attrs={'id':'state','placeholder':'State','required':'required'})
