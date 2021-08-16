from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import *
# Create your views here.

def credential(request):
    return render(request, 'daily/credentials/credential.html')
    
def home(request):
    return render(request, 'daily/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, 'daily/credentials/regiter.html', {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'daily/credentials/register', {
                'message': 'Username already taken'
            })

        login(request, user)
        return redirect('home')

    else:
        return render(request, 'daily/credentials/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'daily/credentials/login.html', {
                'message': 'Invalid user and / or password'
            })
    else:
        return render(request, 'daily/credentials/login.html')


def logout_view(request):
    logout(request)
    return redirect('credential')