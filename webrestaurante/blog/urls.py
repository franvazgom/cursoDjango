from django.urls import path
from .import views
from .views import BlogPageView

urlpatterns = [
    #path('', views.blog, name="blog"),
    path('', BlogPageView.as_view(), name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
]
