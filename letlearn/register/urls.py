from os import name
from letlearn.register.views import profile, Client
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'register'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('clientprof/', views.client, name='client'),
    path('teacherprof/', views.teacher, name='teacher'),
    path('studentprof/', views.studentpro, name='studentpro'),
    path('principalprof/', views.principal, name='principal'),
    path('parentsprof/', views.parents, name='parents')
] + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
