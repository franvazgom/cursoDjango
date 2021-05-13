from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe

# Create your views here.

class RecipesDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:recipes')

class RecipesCreateView(CreateView):
    model = Recipe
    fields = ['title','content','order']
    success_url = reverse_lazy('recipes:recipes')

class RecipesUpdateView(UpdateView):
    model = Recipe
    fields = ['title','content','order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('recipes:update', args=[self.object.id])+'?ok'

class RecipesListView(ListView):
    model = Recipe


"""
def recipes(request):
    recipes = get_list_or_404(Recipe)
    return render(request, 'recipe/recipes.html', {'recipes': recipes})
"""
class RecipeDetailView(DetailView):
    model = Recipe

"""
def recipe(request, recipe_id, recipe_slug):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe.html', {'recipe': recipe})
"""