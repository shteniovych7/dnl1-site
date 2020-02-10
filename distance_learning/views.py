from django.shortcuts import render
from distance_learning.models import Task

def distance_learning(request):
    tasks = Task.objects.all()
    return render(request, 'distance_learning/distance_learning.html', {'tasks':tasks})