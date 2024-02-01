from django.db import models

# Create your models here.

class DepartmentModel(models.Model):
    department_name=models.CharField(max_length=100, blank=False, null=False)

class EmployeeModel(models.Model):
    employee_name=models.CharField(max_length=100, blank=False, null=False)
    department=models.IntegerField(choices=[(1, 'Managers'), (2, 'Team Leads'), (3, 'Employees')], blank=False, null=False)
