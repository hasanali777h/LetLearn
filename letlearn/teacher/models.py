from django.db import models
from learn.models import *


class School(models.Model):
    schoolid = models.IntegerField(primary_key=True)
    schoolname = models.CharField(max_length=50)
    schoolimage = models.ImageField(default='default.jpg')
    schoolcontactno = models.IntegerField()
    schooladdress = models.CharField(max_length=500)
    createddate = models.DateTimeField()
    schoolemail = models.EmailField()
    password = models.CharField(max_length=13)

    def __str__(self):
        return self.schoolname


class RoleName(models.Model):
    roleid = models.IntegerField(primary_key=True)
    rolename = models.CharField(max_length=50)

    def __str__(self):
        return self.rolename


class TblClass(models.Model):
    classid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    schoolid = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursedescription = models.CharField(max_length=500)
    coursename = models.CharField(max_length=50)
    userid = models.IntegerField()
    code = models.CharField(max_length=50)
    videolink = models.FileField()
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    imagelink = models.URLField()
    duration = models.DateTimeField()
    longdes = models.TextField()
    coursetype = models.CharField(max_length=50)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    assignto = models.CharField(max_length=200)
    status = models.BinaryField()

    def __str__(self):
        return self.coursename


class Lecture(models.Model):
    lectureid = models.IntegerField(primary_key=True)
    lecturename = models.CharField(max_length=150)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    lectureurl = models.URLField(max_length=500)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    videolink = models.FileField()
    lecturedescription = models.TextField(max_length=500)
    userid = models.IntegerField()

    def __str__(self):
        return self.lecturename


class schoolTeacher(models.Model):
    teacherid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.IntegerField()
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    passowrd = models.CharField(max_length=13)
    image = models.ImageField(default='default.jpg')
    regno = models.CharField(max_length=20)
    joiningdate = models.DateTimeField()

    def __str__(self):
        return self.name


class Assignment(models.Model):
    assignmentid = models.IntegerField(primary_key=True)
    assignmentname = models.CharField(max_length=50)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignmenturl = models.URLField()
    duedate = models.DateTimeField()
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    userid = models.IntegerField()

    def __str__(self):
        return self.assignmentname
