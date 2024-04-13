from django.contrib import admin
from .models import Producto
from .models import Inventario

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']  # ajusta esto según tus necesidades
    list_filter = ['tienda', 'tipo', 'categoria']  # igualmente, ajusta los filtros como necesites

# Si prefieres no usar el decorador, puedes descomentar la siguiente línea:
# admin.site.register(Producto, ProductoAdmin)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['producto', 'almacen', 'cantidad']
    # Configura aquí cualquier otro detalle de administración que necesites