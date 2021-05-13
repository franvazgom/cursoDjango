from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.conctact, name="contact"),
    path('about/', views.about, name="about"),
]
