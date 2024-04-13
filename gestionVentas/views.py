# views.py en gestionVentas
from django.shortcuts import render
from .forms import VentaForm, DetalleVentaFormSet


from django.shortcuts import render

def registrar_venta(request):
    # tu lógica aquí
    return render(request, 'gestionVentas/registrar_venta.html', {'form': form, 'formset': formset})
