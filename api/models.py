from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, unique=True,
                                related_name = 'user')
    facebook_user = models.CharField(max_length=50, blank=True, null=True, unique=True )
    phone = models.CharField( blank=True, unique=True, null=True, max_length=19)
    profile = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.user.first_name
