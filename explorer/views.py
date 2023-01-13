from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
        return render(request, 'explorer/index.html', {})

def dashboard_users(request):
        return render(request, 'dashboard/index.html', {})

def maps_users(request):
        return render(request, 'dashboard/maps.html', {})

def messages_users(request):
        return render(request, 'dashboard/messages.html', {})

def notification_users(request):
        return render(request, 'dashboard/notification.html', {})

def settings_users(request):
        return render(request, 'dashboard/settings.html', {})

def login_users(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return render(request, 'dashboard/index.html', {})
                else:
                        return render(request, 'authentication/index.html', {})
        else:
                return render(request, 'authentication/index.html', {})

def signup_users(request):
        return render(request, 'authentication/register.html', {})

def resets_users(request):
        return render(request, 'authentication/reset.html', {})

def forgot_users(request):
        return render(request, 'authentication/forgot.html', {})