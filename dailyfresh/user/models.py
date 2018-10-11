from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=10,unique=True)
    upwd = models.CharField(max_length=20)
    uemail = models.CharField(max_length=50,unique=True)
    isdelete = models.BooleanField(default=False)