from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dz4
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def dz4(request):
    dz = Dz4.objects.all()
    return render(request, 'dz4/dz4.html', {"dz": dz})


def detail(request, dz_id):
    dz = get_object_or_404(Dz4, pk=dz_id)
    return render(request, 'dz4/detail.html', {'dz': dz})


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'dz4/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current')
            except IntegrityError:
                return render(request, 'dz4/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такой юзер уже существует'})
        else:
            return render(request, 'dz4/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def current(request):
    return render(request, 'dz4/current.html')


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('dz4')


def login_user(request):
    if request.method == "GET":
        return render(request, 'dz4/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'dz4/login.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('current')
