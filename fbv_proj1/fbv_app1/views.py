from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponseRedirect
import requests


# Create your views here.

def retrive_view(request):
    employees = Employee.objects.all()
    return render(request, 'fbv_app1/index.html', {'employees': employees})


def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request, 'fbv_app1/insert.html', {'form': form})


def delete_view(request, id):
    employees = Employee.objects.get(id=id)
    employees.delete()
    return redirect('/')


def update_view(request, id):
    employees = Employee.objects.get(id=id)
    if request.method=='POST':
        form= EmployeeForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request, 'fbv_app1/update.html', {'employees': employees})
