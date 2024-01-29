

# Create your views here.
from django import http
from django.shortcuts import redirect, render
from .forms import NameForm


def index(request):
    context={
        'name': request.session.get('name'),
    }
    return render(request, 'departments/index.html', context)

def add_name(request):
    form = NameForm(request.POST)

    if request.method == 'GET':
        return render(request, 'departments/add-name.html')

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            return redirect('index')
    
    return http.HttpResponse("Invalid data")
        