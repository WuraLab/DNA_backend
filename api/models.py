from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, unique=True)
    facebook_user = models.CharField(max_length=50, blank=True, null=True, unique=True )
    telephone = models.IntegerField(validators=[MinLengthValidator(0), MaxLengthValidator(11)])
    profile = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return self.user.first_name
