from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.

def index(request):
    tform = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            data = Task.objects.create(title=title, description=description)     
    context = {'form':tform}              
    return render(request, 'index.html', context)

