from home.views import account_settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("register/", views.register, name = 'register'),
    path("about/", views.about, name = 'about'),
    path("contact/", views.contact, name = 'contact'),
    path("login/", views.loginPage, name = 'loginPage'),
    path("logout/", views.logoutUser, name = 'logout'),
    path("userpage/", views.userPage, name = 'userpage'),
    path("account_settings/", views.account_settings, name = 'account_settings'),
]
