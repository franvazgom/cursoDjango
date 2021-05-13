from django.urls import path
from .views import ServiceTemplateView, ServiceCreateView, ServiceUpdateView
from . import views as view_services

services_patterns = ([
    path('', ServiceTemplateView.as_view(), name="services"),
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('update/<int:pk>', ServiceUpdateView.as_view(), name='update'),
],'services')