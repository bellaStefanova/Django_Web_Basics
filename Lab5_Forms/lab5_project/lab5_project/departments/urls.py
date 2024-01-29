from django.urls import path

from .views import add_name, index

urlpatterns = [
    path('index/', index, name='index'),
    path('add-name/', add_name, name='add-name'),
]