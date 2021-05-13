from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Service

# Create your views here.
class ServiceTemplateView(TemplateView):
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context

class ServiceCreateView(CreateView):
    model = Service
    fields = ['title','subtitle','description','image']
    success_url = reverse_lazy('services:services')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['title','subtitle','description','image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('services:update', args=[self.object.id])+'?ok'

"""
def services(req):
    servs = Service.objects.all()
    return render(req, "services/services.html", {"services":servs})
"""