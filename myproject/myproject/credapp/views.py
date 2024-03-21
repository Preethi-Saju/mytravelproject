from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials.")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        email=request.POST['email']
        last_name = request.POST['last_name']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exists.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exists.")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"Both password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')