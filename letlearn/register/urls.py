from os import name
from letlearn.register.views import profile
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'register'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile')
] + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
