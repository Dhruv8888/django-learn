from django.db import models

# Create your models here.

class Student(models.Model):
    stid=models.IntegerField
    stname=models.CharField(max_length=70)
    stemail=models.CharField(max_length=70)
    stpass=models.CharField(max_length=70)
    comment=models.CharField(max_length=70)
            

