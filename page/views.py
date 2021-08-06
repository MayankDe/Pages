from django.db.models.fields.json import DataContains
from .models import ContactUs, Post
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from . forms import SignUpForm,LogInForm,PostForm
from django.contrib import messages


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def dashboard(request):
    return render(request,'dashboard.html')

def about(request):

    return render(request,'about.html')


def contact(request):
   
    if request.method =="POST":

        name = request.POST['Name']
        email = request.POST['Email']
        address = request.POST['Address']
        message = request.POST['Message']
        ct = ContactUs(Name=name,Email=email,Address=address,Message=message)
        
        messages.success(request,"Thanks for Contact!......................")
        ct.save()
    return render(request,'contact.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LogInForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                
                upass=form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully !!....')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LogInForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
def user_signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation! You are Registered Here.')
            form.save()
    else:
        form=SignUpForm() 
    return render(request,'signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
       
        return render(request,'dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')