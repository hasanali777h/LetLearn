"""letlearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v
from home import views as vh
from parents import views as pv
from teacher import views as tv
# ADMIN HEADER CUSTOMIZATION
admin.site.site_header = "Let's Learn Digitally"
admin.site.title = "Welcome to Let's Learn Digitally"
admin.site.index_title = "Welcome Admin"
# ---------------------------------xxxxxxxxxx----------------------#

urlpatterns = [
    path('learn/', include('learn.urls')),
    path('parents/', pv.parents, name='parents.urls'),
    path('register/', v.register, name='register.urls'),
    path('profile/', v.profile, name='profile.urls'),
    path('home/', vh.home, name='home.urls'),
    path('about/', vh.about, name='about.urls'),
    path('login/', vh.login, name='login.urls'),
    path('register/', vh.register, name='register.urls'),
    path('home/', tv.home, name='home.urls'),
    path('assignment/', tv.assignment, name='assignment.urls'),
    path('deleteAssignment/', tv.deleteAssignment, name='deleteAssignment.urls'),
    path('login_page/', tv.login_page, name='login_page.urls'),
    #path('onlinelecture/', tv.onlinelecture, name='onlinelecture.urls'),
    path('portal/', tv.portal, name='portal.urls'),
    path('uploadedAssignment/', tv.uploadedAssignment, name='uploadedAssignment.urls'),
    #path('user/', vh.user, name='user.urls'),
    path('account_settings/', vh.account_settings, name='account_settings.urls'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
]
