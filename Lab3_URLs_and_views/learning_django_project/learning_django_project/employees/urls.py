from django.urls import path
from learning_django_project.employees.views import show_employee_info, show_employee_info_with_class


urlpatterns = [
    path('show_info/', show_employee_info, name='show_employee_info'),
    path('show_info_with_class/', show_employee_info_with_class, name='show_employee_info_with_class'),
]
