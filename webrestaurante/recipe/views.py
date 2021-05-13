from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe
from .forms import PedidoForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView


class RecipeCreatePedido(CreateView):
    form_class = PedidoForm
    template_name = "recipe/pedido_cliente.html"
    success_url = reverse_lazy('recipes:success_pedido')

    def form_valid(self, form):
        # Guarda los datos del pedido
        pedido_nuevo = form.save(commit=False)
        pedido_nuevo.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Coloca el request disponible, para después obtener la sesión en la forma.         
        """
        kwargs = super(RecipeCreatePedido, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class PedidoSuccess(TemplateView):
    template_name = "recipe/pedido_success.html"


def _creaDiccionario(datos_pedido):
    diccionario = {}
    datos_pedido = datos_pedido[:-1]
    productos = datos_pedido.split('|')
    for producto in productos:
        detalle = producto.split("-")
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario


def realizar_pedido(request):
    pedido = list()
    if request.method == 'POST':
        datos_pedido = request.POST['datos_pedido']
        productos = _creaDiccionario(datos_pedido)
        total = 0
        for codigo_barra in productos.keys():
            cantidad = productos[codigo_barra]
            if cantidad > 0:
                dict_producto = {}
                receta = Recipe.objects.get(pk=codigo_barra)
                dict_producto['id'] = receta.id
                dict_producto['descripcion'] = receta.title
                dict_producto['cantidad'] = cantidad
                dict_producto['precio'] = "100"
                total += cantidad * 100
                pedido.append(dict_producto)
        # Coloca en variable de sesión el total y el pedido
        request.session['total_float'] = float(total)
        request.session['detalle_pedido'] = pedido

    return render(request, "recipe/detalle_pedido.html", {"pedido": pedido, "total": total})


class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:recipes')


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy("recipes:update", args=[self.object.id]) + '?ok'


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'content', 'order']

    success_url = reverse_lazy('recipes:recipes')

    '''def get_success_url(self):
        return reverse("recipes:recipes")
        '''


class RecipeListView(ListView):
    model = Recipe


class RecipeDetailView(DetailView):
    model = Recipe
