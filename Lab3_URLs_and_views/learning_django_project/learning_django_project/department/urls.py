from django.urls import path

from learning_django_project.department.views import departments_index

urlpatterns = [

    path('<department_id>/', departments_index)
]
