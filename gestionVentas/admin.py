# contenido de admin.py
from django.contrib import admin
from .models import Venta, DetalleVenta
from .forms import DetalleVentaFormset

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    formset = DetalleVentaFormset
    extra = 1  # Número de formas de detalle de venta para mostrar por defecto

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ['id_ventas', 'estado_venta', 'cliente']
    inlines = [DetalleVentaInline,]
    # Añade aquí cualquier configuración adicional si es necesario

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['venta', 'producto', 'cantidad', 'precio_unitario']
    # Añade aquí cualquier configuración adicional si es necesario
