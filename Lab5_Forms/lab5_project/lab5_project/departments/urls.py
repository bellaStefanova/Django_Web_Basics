from django.urls import path

from .views import add_department, index

urlpatterns = [
    path('index/', index, name='index'),
    path('add-department/', add_department, name='add-department'),
]