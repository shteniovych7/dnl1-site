from django.shortcuts import render
from distance_learning.models import Task
import collections

def distance_learning(request):
    tasks_arr = Task.objects.all()
    tasks_unord = { int(''.join(list(filter(str.isdigit, x.class_name)))) : x for x in tasks_arr}
    tasks = collections.OrderedDict(sorted(tasks_unord.items()))
    return render(request, 'distance_learning/distance_learning.html', {'tasks':tasks})