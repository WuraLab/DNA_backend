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




class Loan_Record(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='record')
    due_date=models.DateField(blank=True, null=True)
    created=models.DateField(auto_now_add=True)
    amount=models.CharField(max_length=200)
    interest_rate=models.DecimalField(max_digits=5, decimal_places=2,)
    paid=models.BooleanField(default=False)
    lender=models.BooleanField(default=True)
    description=models.TextField()
    balance_to_pay=models.IntegerField(blank=True,null=True)



    def create(self, *args, **kwargs):
      #the interest is gotten by interest/year * amount
      if self.interest_rate ==0:
        super(Loan_Record, self).save(*args, **kwargs)
        return self.amount
      else:
        self.interest_rate = self.interest_rate/12  * int(self.amount)
        super(Loan_Record, self).save(*args, **kwargs)



    def __str__(self):
       """one-line docstring for representing the L object."""
       return self.description


