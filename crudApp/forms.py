from django import forms
from django.forms import fields
from crudApp import models
from crudApp.models import Employee


class createEmployee(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('__all__')


