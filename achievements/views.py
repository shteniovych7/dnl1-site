from django.shortcuts import render
from achievements.models import AllMedalist

def achievements(request):
    medalists = AllMedalist.objects.all()
    size = len(medalists)

    return render(request, 'achievements/achievements.html', {'medalists': medalists, 'size': size})