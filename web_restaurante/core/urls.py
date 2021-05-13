from django.urls import path
from . import views as view_core
from .views import IndexTemplateView, AboutTemplateView, StoreTemplateView

core_patterns = ([
    path('', IndexTemplateView.as_view(), name="index"),
    path('acerca-de/', AboutTemplateView.as_view(), name="about"),
    path('visitanos/', StoreTemplateView.as_view(), name="store"),
], 'core')