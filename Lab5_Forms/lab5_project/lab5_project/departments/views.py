import os
import sys
import django

# Create your views here.
from django import http
from django.shortcuts import redirect, render
from django.urls import reverse

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab5_project.lab5_project.settings")
# django.setup()

# from departments.models import EmployeeModel
from lab5_project.departments.forms import DepartmentForm, EmployeeForm
# import departments.models
from lab5_project.departments.models import EmployeeModel
# print(sys.path)

def index(request, **kwargs):
    # form = DepartmentForm(request.POST)
    # if form.is_valid():
    #     print(form)
    context={
                "employees": EmployeeModel.objects.all(),
            }
            

    return render(request, 'departments/index.html', context)

def add_department(request):

    if request.method == 'GET':
        context={
        "department_form": DepartmentForm(),
        }

        return render(request, 'departments/add-department.html', context)

    if request.method == 'POST':

        form = DepartmentForm(request.POST)
        
        if form.is_valid():
            return redirect('index')
        
        else:
            context={
                "department_form": form,
            }
            return render(request, 'departments/add-department.html', context)



def add_employee(request):

    # if request.method == 'GET':
    #     context={
    #     "employee_form": EmployeeForm(),
    #     }

    #     return render(request, 'departments/add-employee.html', context)

    # if request.method == 'POST':

    #     form = EmployeeForm(request.POST)
    #     print("post")
        
    #     if form.is_valid():
    #         print("valid")
    #         form.save()
            
    #         return redirect('index')
        
    # else:
    #     context={
    #             "employee_form": form,
    #         }
    # return render(request, 'departments/add-employee.html', context)
    if request.method == 'GET':
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context={
        "employee_form": form,
        "employees": EmployeeModel.objects.all(),
        }

    return render(request, 'departments/add-employee.html', context)

# context={
#                 "employees": EmployeeModel.objects.all(),
#             }
# print(context)
        
def edit_employee(request, pk):
    employee=EmployeeModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
    else:
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('index/'))
    context={
        "employee_form": form,
        "employee": employee,
        }
    
    return render(request, 'departments/edit-employee.html', context)

        