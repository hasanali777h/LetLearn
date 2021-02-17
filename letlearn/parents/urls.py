from django.urls import path
#from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static
from . import views

app_name = 'parents'

urlpatterns = [
    path('parents/', views.parents, name='parents')
]
