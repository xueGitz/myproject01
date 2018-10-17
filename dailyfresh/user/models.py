from django.db import models

# Create your models here.
from  django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

class User(AbstractUser,BaseModel):
    myPhone = models.CharField(max_length=11,null=True)
    myaddress = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'df_user'


class UserAddress(models.Model):
    reciname = models.CharField(max_length=10,verbose_name='收件人')
    address = models.TextField(verbose_name='地址')
    postcode = models.CharField(max_length=10,verbose_name='邮编')
    phoneNum = models.CharField(max_length=11,verbose_name='电话号码')
    username = models.ForeignKey(User,verbose_name='用户名')

    class Meta:
        db_table = 'df_user_address'


class AreaContect(models.Model):
    tittle = models.CharField(max_length= 20,verbose_name='地区')
    parent = models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        return self.tittle