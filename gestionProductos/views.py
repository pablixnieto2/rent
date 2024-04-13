from django.views.generic import ListView, CreateView
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from .models import Inventario
from .forms import InventarioForm

class ListaProductosView(ListView):
    model = Producto
    template_name = 'gestionProductos/lista_productos.html'

class CrearProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'gestionProductos/crear_producto.html'
    success_url = '/productos/'  # Redirecciona a la lista de productos tras crear uno

class InventarioUpdateView(UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'gestionProductos/inventario_form.html'
    success_url = '/ruta-a-redireccionar-despues-de-guardar/'

    def form_valid(self, form):
        # Aquí puedes agregar lógica adicional si es necesario
        return super().form_valid(form)