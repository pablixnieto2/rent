from django.urls import path
from .views import ListaProductosView, CrearProductoView
from .views import InventarioUpdateView

urlpatterns = [
    path('productos/', ListaProductosView.as_view(), name='lista-productos'),
    path('productos/crear/', CrearProductoView.as_view(), name='crear-producto'),
    path('inventario/actualizar/<int:pk>/', InventarioUpdateView.as_view(), name='actualizar-inventario'),
]
