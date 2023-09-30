
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from ip_project import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def Landing_page(request):
    return render(request,'Landing_page.html')

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')

def index(request):
    data={
        'clist' :["apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry","apple", "banana", "cherry",],
    }
    return render(request,'index.html',data)

def recommend(request):
    data={
        
        'mlist':["apple", "banana", "cherry","apple",]
    }
    return render(request,'recommend.html',data)

def contacts(request):
    return render(request,'contacts.html')

def about_us(request):
    return render(request,'about_us.html')

def novels(request):
    
    data={
        
        'mlist':["apple", "banana", "cherry","apple",]
    }
    return render(request,'novels.html',data)

def scifi(request):
    
    data={
        
        'mlist':["apple", "banana", "cherry","apple",]
    }
    return render(request,'scifi.html',data)


def login(request):
    
    if request.method == "POST":
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        username1 = User.objects.get(email=email).username
        
        if username1 != "":
            messages.success(request, "Logged In Sucessfully!!")
            return redirect('/home2')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/login')
    else:
        email="#"
        pass1="#"
    print(email)
    print(pass1)
        

    return render(request,'login.html')

def registration(request):
    
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
       
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/registration')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('/registration')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('/login')

        
    else:
        username="#"
        email="#"
        pass1="#"
        
    return render(request,'registration.html')