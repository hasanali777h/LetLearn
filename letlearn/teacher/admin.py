from django.contrib import admin
from teacher.models import schoolTeacher, Assignment, School, RoleName, TblClass, Course, Lecture

# Register your models here.

admin.site.register(schoolTeacher)
admin.site.register(Assignment)
admin.site.register(School)
admin.site.register(TblClass)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(RoleName)
