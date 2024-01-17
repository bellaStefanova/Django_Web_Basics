from django import http
from django.shortcuts import render

#function based views - a function that hase one or more parameters and returns response.

def index(request):

    context={'name': 'Ivan'}
    # name = request.GET.get('name', 'Anonymous')
    # return http.HttpResponse(f"Hello, {name}")
    return render(request, 'first_app/index.html', context)