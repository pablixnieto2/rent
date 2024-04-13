# contenido de urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ventas/nueva/', views.crear_venta, name='crear_venta'),
    # Añadir más paths según sea necesario.
    path('nueva/', registrar_venta, name='nueva_venta'),
]
