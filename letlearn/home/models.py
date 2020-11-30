from django.db import models
from django.db.models.query_utils import select_related_descend
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    schoolid = models.AutoField(primary_key=True)
    schoolname = models.CharField(max_length=50, null= True)
    schoolimage = models.ImageField(null=True)
    schoolcontactno = models.CharField(max_length=13, null= True)
    schooladdress = models.CharField(max_length=500)
    createddate = models.DateTimeField(null= True)
    schoolemail = models.EmailField(null= True)
    password = models.CharField(max_length=13,null= True)

    def __str__(self):
        return self.schoolname

class Section(models.Model):
    sectionid = models.AutoField(primary_key=True)
    sectionname = models.CharField(max_length=500,null= True)
    schoolid = models.ForeignKey(School,null= True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.sectionname



class Status(models.Model):
    statusid = models.AutoField(primary_key=True)
    statustype = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.statustype

class Client(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null = True)
    ceratedon = models.DateTimeField(null = True)
    email = models.CharField(max_length=50,null = True)
    password = models.CharField(max_length=13)
    certificatetypename = models.CharField(max_length=100,null = True)
    cnic = models.CharField(max_length=50,null = True)
    contactnumber = models.CharField(max_length=13,null = True)
    image = models.ImageField(default='default.jpg')
    status = models.ForeignKey(Status, null=True,on_delete=models.DO_NOTHING)
    confirmpassword = models.CharField(max_length=13,null = True)

    def __str__(self):
        return self.username

class TblClass(models.Model):
    classid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null= True)
    schoolid = models.ForeignKey(School,null= True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class RoleName(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.rolename

class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursedescription = models.CharField(max_length=500,null= True)
    coursename = models.CharField(max_length=50,null= True)
    userid = models.ForeignKey(Client,null= True,on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=50,null= True)
    videolink = models.CharField(max_length=500 ,null= True)
    roleid = models.ForeignKey(RoleName,null=True,on_delete=models.DO_NOTHING)
    createddate = models.DateTimeField()
    imagelink = models.ImageField(null=True)
    duration = models.DateTimeField()
    longdes = models.TextField(null=True)
    coursetype = models.CharField(max_length=50)
    classid = models.ForeignKey(TblClass,null=True,on_delete=models.DO_NOTHING)
    assignto = models.CharField(max_length=200, null=True)
    status = models.BinaryField(null = True)

    def __str__(self):
        return self.coursename

class Day(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null =True)

    def __str__(self):
        return self.name

class Exam(models.Model):
    
    examid = models.AutoField(primary_key=True)
    examname = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.examname

class SchoolAssignment(models.Model):
    assignmentid = models.AutoField(primary_key=True)
    assignmentname = models.CharField(max_length=50,null=True)
    classid = models.ForeignKey(TblClass,null=True,on_delete=models.SET_NULL)
    courseid = models.ForeignKey(Course, null=True,on_delete=models.SET_NULL)
    assignmenturl = models.CharField(max_length=500,null=True)
    duration = models.DateTimeField(null=True)
    schoolid = models.ForeignKey(School,null=True,on_delete=models.SET_NULL)
    createddate = models.DateTimeField(null=True)
    userid = models.ForeignKey(Client,null=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.assignmentname

class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    classid = models.ForeignKey(TblClass,null=True,on_delete=models.DO_NOTHING)
    courseid = models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)
    sectionid = models.ForeignKey(Section,null=True,on_delete=models.DO_NOTHING)
    starttime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
    allocationstatus = models.CharField(max_length=100,null=True)
    dayid = models.ForeignKey(Day,null=True,on_delete=models.DO_NOTHING)
    schoolid = models.ForeignKey(School,null=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)


class Student(models.Model):
    user = models.OneToOneField(User,null =True,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    regno = models.CharField(max_length=20,null=True)
    registrationdate = models.DateTimeField(null =True)
    address = models.CharField(max_length=100,null =True)
    classid = models.ForeignKey(TblClass,null=True, on_delete=models.SET_NULL)
    schoolid = models.ForeignKey(School,null=True, on_delete=models.SET_NULL)
    sectionid = models.ForeignKey(Section,null=True, on_delete=models.SET_NULL)
    std_profile = models.ImageField(default="download.png", null = True,blank = True)

    
    def __str__(self):
        return self.sname


class StudentResult(models.Model):
    studentresultid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student,null =True,on_delete=models.DO_NOTHING)
    courseid = models.ForeignKey(Course,null=True,on_delete=models.DO_NOTHING)
    totalmarks = models.IntegerField(null = True)
    marksobtained = models.IntegerField(null = True)
    percentage = models.DecimalField(max_digits=2, decimal_places=2,null = True)
    schoolid = models.ForeignKey(School,null = True,on_delete=models.DO_NOTHING)
    classid = models.ForeignKey(TblClass,null = True,on_delete=models.DO_NOTHING)
    createddate = models.DateTimeField(null = True)
    sectionid = models.ForeignKey(Section,null=True,on_delete=models.DO_NOTHING)
    examid = models.ForeignKey(Exam,on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.studentresultid)

class SubmitAssignment(models.Model):
    uploadid = models.AutoField(primary_key=True)
    assignmentid = models.ForeignKey(SchoolAssignment, on_delete=models.DO_NOTHING)
    schoolid = models.ForeignKey(School,on_delete=models.SET_NULL,null = True)
    studentid = models.ForeignKey(Student, on_delete=models.SET_NULL,null = True)
    courseid = models.ForeignKey(Course, on_delete=models.SET_NULL,null = True)
    uploadurl = models.CharField(max_length=500,null = True)
    createddate = models.DateTimeField(auto_now_add=True,null = True)

    def __str__(self):
        return str(self.uploadid)


class StudentHistory(models.Model):
    studenthistoryid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student,null=True, on_delete=models.DO_NOTHING)
    lastclass = models.CharField(max_length=50,null=True)
    createddate = models.DateTimeField(auto_now_add=True,null=True)
    lastclasssection = models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.studentid)
