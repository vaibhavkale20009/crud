from django.shortcuts import render,redirect
from crudApp import forms
from crudApp import models
from crudApp.models import Employee

# Create your views here.


def createview(request):
    form=forms.createEmployee()
    if(request.method=='POST'):
        form=forms.createEmployee(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/home')
    return render(request,'crudApp/create.html',{'form':form})



def retrieve_view(request):
    emp=Employee.objects.all()
    return render(request,'crudApp/retrieve.html',{'emp':emp})

def update_view(request,id):
    emp=Employee.objects.get(id=id)
    if(request.method=='POST'):
        empx=forms.createEmployee(request.POST,instance=emp)
        if(empx.is_valid()):
            empx.save()
            return redirect('/')
    return render(request,'crudApp/update.html',{'emp':emp})

def del_view(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete(id)
    return redirect('/')


    
    








