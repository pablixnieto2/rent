from django.db import models
from django.utils import timezone
from django.conf import settings


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Vincula al usuario de Django
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se establece automáticamente al crear
    fecha_fiesta = models.DateField(null=True, blank=True)
    fecha_cita = models.DateTimeField(null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    ubicacion_cliente = models.CharField(max_length=50, choices=[
        ('Madrid', 'Madrid'), 
        ('Valencia', 'Valencia'), 
        ('Barcelona', 'Barcelona'), 
        ('Videollamada', 'Videollamada')
    ])
    direccion = models.TextField()
    estado = models.CharField(max_length=50, choices=[
        ('Sin Cita', 'Sin Cita'), 
        ('Con Cita', 'Con Cita'), 
        ('Perdido', 'Perdido')
    ])
    como_nos_conocio = models.CharField(max_length=100, choices=[
        ('Google', 'Google'), 
        ('Facebook', 'Facebook'), 
        ('Tiktok', 'Tiktok'), 
        ('Instagram', 'Instagram'), 
        ('Recomendación', 'Recomendación'), 
        ('Google Maps', 'Google Maps'), 
        ('Otro', 'Otro')
    ])
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    prefijo = models.CharField(max_length=20)
    comentarios = models.TextField(null=True, blank=True)
    razon_perdida = models.CharField(max_length=255, null=True, blank=True)
    codigo_postal = models.CharField(max_length=20, null=True, blank=True)
    vendedora = models.CharField(max_length=100)
    es_duplicado = models.BooleanField(default=False)
    # ... continuar con los demás campos según las imágenes

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
