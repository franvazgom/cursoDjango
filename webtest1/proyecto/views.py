from django.shortcuts import render
from .models import Project


def project(request):
    # Devuelve todos los objetos en la variable projects
    projects = Project.objects.all()
    return render(request, "proyecto/project.html", {'projects': projects})
