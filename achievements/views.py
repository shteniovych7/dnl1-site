from django.shortcuts import render
from achievements.models import AllMedalist, ContestYear

def achievements(request):
    medalists = AllMedalist.objects.all()
    size = len(medalists)
    contest_winners_by_years = ContestYear.objects.all()

    return render(request, 'achievements/achievements.html', {'medalists': medalists, 'size': size, 'contest_winners_by_years': contest_winners_by_years})