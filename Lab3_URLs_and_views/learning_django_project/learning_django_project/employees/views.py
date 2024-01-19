import datetime
from django import http
from django.shortcuts import render

# Create your views here.

def show_employee_info(request):
    context={
        "employee_id": 123,
        "employee_name": {
            "first_name": "John",
            "last_name": "Doe"
        },
    }
    return render(request, 'employees/show_employee_info.html', context)

class Person():
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
def show_employee_info_with_class(request):
    context={
        "employee_id": 123,
        "employee": Person("John", "Doe"),
        "grades": [6,4,5,-1,3],
        "empty_grades": [],
        "date": datetime.datetime.now,
        "get_params": request.GET,
    }
    return render(request, 'employees/show_employee_info_with_class.html', context)

def grades(request):
    grades_dict={
        "6": "Excellent",
        "5": "Very good",
        "4": "Good",
        "3": "Fair",
        "2": "Poor",
        "1": "Very poor",
    }

    context={
        "grade": request.GET["grade"],
        "verbal": grades_dict[str(request.GET["grade"])]
    }
    return render(request, 'employees/grades.html',context)