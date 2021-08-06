from django import forms

from django.contrib.auth import models
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import widgets,fields
from  .models import ContactUs

 
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password(Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username',widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels= {'first_name':'First Name','last_name':'Last Name','email':'Email'}

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
       
class LogInForm(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'})) 

class ContactForm(forms.Form):
    model = ContactUs
    fields=['Name','Email','Address','Message','Timestamp']
    labels = {'Name':'Name','Email':'Email','Address':'Address','Message':'Message'}
       
class PostForm(forms.Form):
    fields=['Strength','Weakness','Timestamp']
    

