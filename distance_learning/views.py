from django.shortcuts import render
from distance_learning.models import Task
import collections

def distance_learning(request):
    tasks_arr = Task.objects.all()
    t = { x : int(''.join(list(filter(str.isdigit, x.class_name)))) for x in tasks_arr}
    t1 = {k: v for k, v in sorted(t.items(), key=lambda item: item[1])}
    print(t1)
    return render(request, 'distance_learning/distance_learning.html', {"tasks" : t1})