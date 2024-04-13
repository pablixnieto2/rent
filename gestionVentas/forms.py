# forms.py en gestionVentas
from django import forms
from django.forms import inlineformset_factory
from .models import Venta, DetalleVenta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'comentarios']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio_unitario']

# Esto crea un formset de detalles de venta asociado a una venta
DetalleVentaFormSet = inlineformset_factory(
    Venta, DetalleVenta, form=DetalleVentaForm, extra=1, can_delete=True)
