from django.shortcuts import render
from distance_learning.models import Task
import collections

def distance_learning(request):
    tasks = list(Task.objects.all())
    tasks = sorted(Task.objects.all(), key=lambda n: (int(n.class_name.split('-')[0]), n.class_name.split('-')[1]))
    '''n = len(tasks)
    print(n)
    for i in range(n):
        for j in range(0, n-i-1):
            class_n1 = int(tasks[j].class_name.split('-')[0])
            class_n2 = int(tasks[j+1].class_name.split('-')[0])
  
            if class_n1 > class_n2:
                tasks[j], tasks[j+1] = tasks[j+1], tasks[j]
                
            if class_n1 == class_n2:
                class_b1 = tasks[j].class_name.split('-')[1]
                class_b2 = tasks[j+1].class_name.split('-')[1]
                if class_b1 > class_b2:
                    tasks[j], tasks[j+1] = tasks[j+1], tasks[j]'''
    return render(request, 'distance_learning/distance_learning.html', {"tasks" : tasks})