# gestionVentas/apps.py

from django.apps import AppConfig

class GestionVentasConfig(AppConfig):
    name = 'gestionVentas'

    def ready(self):
        import gestionVentas.signals  # Importa el archivo de señales para conectarlas
