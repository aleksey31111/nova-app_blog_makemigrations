from django.shortcuts import render
from .models import Equipments


def equipments(request):
    projects = Equipments.objects.all()
    return render(request, 'equipments/equipments.html', {'projects': projects})