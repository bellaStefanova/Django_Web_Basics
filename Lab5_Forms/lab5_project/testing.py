import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab5_project.settings")
django.setup()
from lab5_project.departments.models import EmployeeModel

employees = EmployeeModel.objects.all()
for e in employees:
    print(e.employee_name)
    print(e.department)

print(employees)