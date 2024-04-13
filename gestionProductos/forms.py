from django import forms
from .models import Producto
from .models import Inventario

# Aquí creas un formulario para el modelo Producto.
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
        
class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['producto', 'almacen', 'cantidad']