from django.contrib import admin
from .models import Profile, Client, Teacher, StudentPro, Principal, Parents

# Register your models here.
admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Teacher)
admin.site.register(StudentPro)
admin.site.register(Principal)
admin.site.register(Parents)
