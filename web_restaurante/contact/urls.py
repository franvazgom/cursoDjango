from django.urls import path
from . import views as view_core

urlpatterns = [
    path('', view_core.contact, name="contact"),
    path('ejecutaAJAX/', view_core.ejecutaAJAX, name="ejecutaAJAX")
]