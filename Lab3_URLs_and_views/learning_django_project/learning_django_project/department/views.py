import time
from django import http
from django.shortcuts import redirect, render

# Create your views here.

def index(request, **kwargs):
    return http.HttpResponse(f"Response from {time.time()}")

def departments_index(request, department_id):
    context={
        'path': request.path,
        'method': request.method,
        'user': request.user,
    }
    if department_id.isdigit():
        if int(department_id) in range(1,10):
            return http.HttpResponse(f'Showing info for Department {department_id}\n{context["path"]}\n{context["method"]}\{context["user"]}')
        if int(department_id) == 10:
            return redirect('index')
        if int(department_id) == 11:
            raise http.Http404
        
    return http.HttpResponseNotFound('Non existing department')
        



