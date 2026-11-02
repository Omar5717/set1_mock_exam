from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    course=models.CharField(max_length=100)
    fee=models.IntegerField()
    joining_date=models.DateField(auto_now_add=True)
    is_fee_paid = models.BooleanField(default=False)
    