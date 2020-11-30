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
