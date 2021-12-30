from django.db import models

# Create your models here.


class Employee(models.Model):
    emid=models.IntegerField()
    emname=models.CharField(max_length=20)
    emsalary=models.IntegerField()
    emadd=models.CharField(max_length=40)

