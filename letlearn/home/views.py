from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, StudentForm 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,student_only
from django.contrib.auth.models import Group, User


# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    return render(request,'home.html')

@unauthenticated_user
def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name = 'student')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)          
            return redirect('loginPage')
                        
    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('loginPage')


@login_required(login_url='loginPage')
def about(request):
    return render(request,'about.html')

@login_required(login_url='loginPage')
def contact(request):
    return render(request,'home.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def userPage(request):
    return render(request, 'user.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['student'])
def account_settings(request):
    student = request.user.student
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            
            
    context = {'form':form}
    return render(request, 'account_settings.html', context)

