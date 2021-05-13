from django.urls import path
#from .views import PagesTemplateView
from . import views

urlpatterns = [
    #path('<int:page_id>/<slug:page_slug>/', PagesTemplateView.as_view(), name="page"),
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]