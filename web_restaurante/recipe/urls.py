from django.urls import path
from . import views
from .views import RecipesListView, RecipeDetailView, RecipesCreateView, RecipesUpdateView, RecipesDeleteView

recipe_patterns = ([
    path('', RecipesListView.as_view() , name='recipes'),
    path('<int:pk>/<slug:recipe_slug>/', RecipeDetailView.as_view(), name='recipe'),
    path('create/', RecipesCreateView.as_view(), name='create'),
    path('update/<int:pk>', RecipesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', RecipesDeleteView.as_view(), name='delete'),
], 'recipes')
