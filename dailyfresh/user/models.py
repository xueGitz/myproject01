from django.db import models

# Create your models here.
from  django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

class User(AbstractUser,BaseModel):
    class Meta:
        db_table = 'df_user'