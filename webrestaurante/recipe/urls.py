from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, RecipeCreatePedido, PedidoSuccess

recipes_patterns = ([
    path('pedido/', views.realizar_pedido, name='detalle_pedido'),
    path('create_pedido/', RecipeCreatePedido.as_view(), name='create_pedido'),
    path('success_pedido/', PedidoSuccess.as_view(), name='success_pedido'),
    path('create/', RecipeCreateView.as_view(), name='create'),
    path('', RecipeListView.as_view(), name='recipes'),
    path('update/<int:pk>/', RecipeUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='delete'),
    path('<int:pk>/<slug:recipe_slug>/',
         RecipeDetailView.as_view(), name='recipe'),
], 'recipes')
