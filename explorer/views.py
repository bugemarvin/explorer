from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
        return render(request, 'explorer/index.html', {})
@login_required(login_url='/login_users')
def dashboard_users(request):
        if request.user.is_authenticated:
                return render(request, 'dashboard/index.html', {})
@login_required(login_url='/login_users')
def maps_users(request):
        if request.user.is_authenticated:
                return render(request, 'dashboard/maps.html', {})
@login_required(login_url='/login_users')
def inbox_users(request):
        if request.user.is_authenticated:
                return render(request, 'dashboard/messages.html', {})
@login_required(login_url='/login_users')
def notification_users(request):
        if request.user.is_authenticated:
                return render(request, 'dashboard/notification.html', {})
@login_required(login_url='/login_users')
def settings_users(request):
        if request.user.is_authenticated:
                return render(request, 'dashboard/settings.html', {})
@login_required(login_url='/login_users')
def profile_users(request):
        if request.user.is_authenticated:
                return render(request, 'dashboard/profile.html', {})

def login_users(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        return render(request, 'dashboard/index.html', {})
                else:
                        messages.success(request, ('! Incorrect Username and Password'))
                        return render(request, 'authentication/index.html', {})
        else:
                return render(request, 'authentication/index.html', {})
def logout_users(request):
        logout(request)
        return render(request, 'explorer/index.html', {})

def signup_users(request):
        return render(request, 'authentication/register.html', {})

def resets_users(request):
        return render(request, 'authentication/reset.html', {})

def forgot_users(request):
        return render(request, 'authentication/forgot.html', {})