from teacher.models import *
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

# Create your views here.


def home(request):
    return render(request, 'home.html')


def portal(request):
    portal = portal.objects.all()
    return render(request, 'portal.html', {'portal': portal})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('portal')
        else:
            # No backend authenticated the credentials
            return render(request, 'home.html')
    return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return render(request, 'home.html')


def assignment(request):
    assignment = assignment.objects.all()
    return render(request, 'assignment.html', {'assignment': assignment})


def addAssignment(request):
    addAssignment = addAssignment.objects.all()
    return redirect('/admin/teacher/assignment/add/', {'addAssignment': addAssignment})


def uploadedAssignment(request):
    queryset = uploadedAssignment.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'uploaded.html', context)


def deleteAssignment(request):

    deleteAssignment = deleteAssignment.objects.all()

    if request.method == "POST":
        assignmentid = request.POST.get("assignmentid")
        assignmentname = request.POST.get("assignmentname")
        SchoolAssignment.objects.filter(
            assignmentid=assignmentid, assignmentname=assignmentname).delete()

    return render(request, 'delete.html', {'deleteAssignment': deleteAssignment})
