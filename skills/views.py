from django.shortcuts import render
from .models import Skills

def skills(request):
    projects = Skills.objects.all()
    return render(request, 'skills/skills.html', {'projects': projects})
