from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

"""
def index(req):
    return render(req, "core/index.html")

def about(req):
    return render(req, "core/about.html")

def store(req):
    return render(req, "core/store.html")
"""

class IndexTemplateView(TemplateView):
    template_name = 'core/index.html'

class AboutTemplateView(TemplateView):
    template_name = 'core/about.html'

class StoreTemplateView(TemplateView):
    template_name = 'core/store.html'