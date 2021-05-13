from django.urls import path
from . import views
from .views import BlogTemplateView, BlogCreateView, BlogDeleteView, BlogUpdateView

blog_patterns = ([
    path('', BlogTemplateView.as_view(), name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),
], 'blog')
