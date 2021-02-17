from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.

class Parents(models.Model):
    #user = models.OneToOneField(User, on_delete=CASCADE)
    parentsid = models.IntegerField()
    parentsname = models.CharField(max_length=50)
    parentsemail = models.IntegerField()
    parentsnumber = models.IntegerField()

    def __str__(self):
        return self.parentsname
