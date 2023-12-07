from django.shortcuts import render, redirect
from task.models import Task
def home(request):
    data = Task.objects.all()
    return render(request, 'index.html', {'data':data})