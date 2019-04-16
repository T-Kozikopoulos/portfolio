from django.shortcuts import render
from project.models import Project


def index(request):
    context = {
        'projects': Project.objects.order_by('-id')[:4]
    }
    return render(request, 'index.html', context)


def projects(request):
    return render(request, 'projects.html')
