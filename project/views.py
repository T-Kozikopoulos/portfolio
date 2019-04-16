from django.shortcuts import render
from .models import Project


def projects(request):
    context = {
        'projects': Project.objects.all
    }
    return render(request, 'projects.html', context)
