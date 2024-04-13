from django.urls import path
from . import views

urlpatterns = [
    path('clientes/registro/', views.registro_cliente, name='registro_cliente'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
]
