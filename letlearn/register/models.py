from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phonenumber = models.CharField(max_length=12, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    profileimage = models.ImageField(
        default='default-avatar.png', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    User = models.OneToOneField(User, on_delete=CASCADE)
    clientname = models.CharField(max_length=50)
    clientemail = models.EmailField()
    clientnumber = models.IntegerField()

    def __str__(self):
        return self.User.userclient


class Teacher(models.Model):
    User = models.OneToOneField(User, on_delete=CASCADE)
    teachername = models.CharField(max_length=50)
    teacheremail = models.EmailField()
    teachernumber = models.IntegerField()

    def __str__(self):
        return self.User.userteacher


class StudentPro(models.Model):
    User = models.OneToOneField(User, on_delete=CASCADE)
    studentname = models.CharField(max_length=50)
    studentemail = models.EmailField()
    studentnumber = models.IntegerField()

    def __str__(self):
        return self.User.userstudentpro


class Principal(models.Model):
    User = models.OneToOneField(User, on_delete=CASCADE)
    principalname = models.CharField(max_length=50)
    principalemail = models.EmailField()
    principalnumber = models.IntegerField()

    def __str__(self):
        return self.User.userprincipal


class Parents(models.Model):
    User = models.OneToOneField(User, on_delete=CASCADE)
    parentsname = models.CharField(max_length=50)
    parentsemail = models.EmailField()
    parentsnumber = models.IntegerField()

    def __str__(self):
        return self.User.userparents
