from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import *
from django.urls import reverse

# Create your views here.


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')

    else:
        redirect('login/')


def client(request):
    if request.user.is_authenticated:
        return render(request, 'clientprof.html')

    else:
        redirect('login/')


def teacher(request):
    if request.user.is_authenticated:
        return render(request, 'teacherprof.html')

    else:
        redirect('login/')


def studentpro(request):
    if request.user.is_authenticated:
        return render(request, 'studentprof.html')

    else:
        redirect('login/')


def principal(request):
    if request.user.is_authenticated:
        return render(request, 'principalprof.html')

    else:
        redirect('login/')


def parents(request):
    if request.user.is_authenticated:
        return render(request, 'parentsprof.html')

    else:
        redirect('login/')
