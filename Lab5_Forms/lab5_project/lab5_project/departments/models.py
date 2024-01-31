from django.db import models

# Create your models here.

class DepartmentModel(models.Model):
    department_name=models.CharField(max_length=100, blank=False, null=False)