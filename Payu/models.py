from django.db import models

from django.contrib.auth.models import AbstractUser


class RegistrationModel(models.Model):
     fullname = models.CharField(max_length=300)
     email=models.CharField(max_length=300)
     phone=models.IntegerField()
