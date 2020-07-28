from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxLengthValidator, MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, unique=True,
                                related_name = 'user')
    facebook_user = models.CharField(max_length=50, blank=True, null=True, unique=True )
    phone = models.CharField( blank=True, unique=True, null=True, max_length=19)
    profile = models.ImageField(upload_to='profile/', blank=True, null=True)


    def __str__(self):
        """one-line docstring for representing the Profile object."""
        return f'{self.user.first_name}'





class add_loan_record(models.Model):
    loan=models.CharField(max_length=200)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    due_date=models.DateField()
    created=models.DateField(auto_now_add=True)
    amount=models.IntegerField()
    interest_rate=models.DecimalField(max_digits=19, decimal_places=10)
    paid=models.BooleanField(default=False)
    borrower=models.BooleanField(default=True)
    description=models.TextField()
    balance_to_pay=models.CharField(max_length=200,blank=True)

    def __str__(self):
       """one-line docstring for representing the Profile object."""
       return self.loan
