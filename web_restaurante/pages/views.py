from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Page

# Create your views here.

"""
class PagesTemplateView(TemplateView):
    template_name = 'pages/sample.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page'] = get_object_or_404(Page, id=1)
        return context
"""

def page(req, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(req, 'pages/sample.html', {'page':page})