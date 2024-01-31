

# Create your views here.
from django import http
from django.shortcuts import redirect, render
from .forms import DepartmentForm


def index(request):
    # form = DepartmentForm(request.POST)
    # if form.is_valid():
    #     print(form)
    context={
        'name': 'something',
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

        