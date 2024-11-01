from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    break_time = models.BooleanField(default=False)
    lunch_time = models.BooleanField(default=False)
    time_got = models.DateTimeField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return self.first_name



