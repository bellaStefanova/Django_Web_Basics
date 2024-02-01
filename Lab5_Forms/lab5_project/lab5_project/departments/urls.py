from django.urls import path

from .views import add_department, add_employee, index, edit_employee

urlpatterns = [
    path('index/', index, name='index'),
    path('add-department/', add_department, name='add-department'),
    path('add-employee/', add_employee, name='add-employee'),
    path('edit-employee/<int:pk>/', edit_employee, name='edit-employee')
]