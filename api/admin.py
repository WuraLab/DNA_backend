from django.contrib import admin
from .models import Profile,Loan_Record, Payment

admin.site.register(Profile)
admin.site.register(Loan_Record)
admin.site.register(Payment)
