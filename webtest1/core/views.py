from django.shortcuts import render, HttpResponse


def home(request):
    # return HttpResponse("<h1>Bienvenid@ a mi página</h1>")
    return render(request, "core/home.html")


def conctact(request):
    return render(request, "core/contact.html")


def about(request):
    return render(request, "core/about.html")
