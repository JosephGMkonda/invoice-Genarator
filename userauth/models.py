from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    Full_Name = models.CharField(null=True,blank=True,max_length=100)
    Address = models.CharField(null=True, blank=True,max_length= 500)

    # related field
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,)



