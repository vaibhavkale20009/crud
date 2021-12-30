from django.contrib import admin
from crudApp import models
from crudApp.models import Employee


# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    list_display=['emid','emname','emsalary','emadd']

admin.site.register(Employee,Employeeadmin)