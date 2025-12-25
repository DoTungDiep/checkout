from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')

        if pw1 != pw2:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=pw1
        )
        return redirect('login1')
    return render(request, "register.html")

def login1(request):
    if request.method == 'POST':
        u_name = request.POST.get('user_name')
        pw = request.POST.get('password')
        user = authenticate(request, username=u_name, password=pw)
        if user:
            login(request, user)
            return redirect('home')      
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')
@login_required
def mamnon(request):
    return render(request, 'mamnon.html')

def tieuhoc(request):
    return render(request, 'tieuhoc.html')

def thcs(request):
    return render(request, 'thcs.html')

def thpt(request):
    return render(request, 'thpt.html')