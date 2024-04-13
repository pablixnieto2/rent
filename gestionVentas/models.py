import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import Sum 
from gestionClientes.models import Cliente
from gestionProductos.models import Producto, Almacen   

class Venta(models.Model):
    
    ESTADO_INICIAL = 'En proceso'
    ESTADO_COMPLETO = 'Completa'
    ESTADO_CANCELADA = 'Cancelada'
    
    ESTADO_OPCIONES = [
    (ESTADO_INICIAL, 'En proceso'),
    (ESTADO_COMPLETO, 'Completa'),
    (ESTADO_CANCELADA, 'Cancelada'),
    # ... otras opciones de estado
]


    TIPO_ENTREGA = [
        ('Envio', 'Envio'),
        ('Entrega', 'Entrega en tienda'),
    ]

    TIPO_VENTA = [
        ('Alquiler', 'Alquiler'),
        ('Venta', 'Venta'),
    ]

    ESTADO_DEPOSITO = [
        ('Entregado', 'Entregado'),
        ('Sin entregar', 'Sin entregar'),
        ('Devuelto', 'Devuelto'),
    ]
    
    
    id_ventas = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ID único generado automáticamente
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='ventas_creadas')
    creation_date = models.DateTimeField(default=timezone.now)
        # Campo para almacenar el estado de la venta
    estado_venta = models.CharField(
        max_length=20,
        choices=ESTADO_OPCIONES,
        default=ESTADO_INICIAL
    )
    tienda = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True, related_name='ventas')  # Usa tu modelo Almacen
    envio_entrega = models.CharField(max_length=20, choices=TIPO_ENTREGA)
    tipo = models.CharField(max_length=20, choices=TIPO_VENTA)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    importe_deposito = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
    estado_deposito = models.CharField(
        max_length=20,
        choices=ESTADO_DEPOSITO,
        default='Sin entregar'
    )
    direccion_envio = models.TextField(blank=True, null=True)
    precio_envio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pendiente_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado_pago = models.CharField(max_length=100, default=ESTADO_INICIAL)
    comentarios = models.TextField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    motivo_descuento = models.TextField(blank=True, null=True)
    devolucion = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    identificacion = models.CharField(max_length=100, blank=True, null=True)
    direccion_cliente = models.TextField(blank=True, null=True)
    tiara = models.CharField(max_length=20, null=True, blank=True)
    fecha_extra_fotos = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Venta {self.id_ventas} - {self.estado_venta}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Si es una nueva instancia de Venta
            self.total_pagar = 0
            self.total_pagado = 0
            self.pendiente_pago = 0
        else:
            # Calcula el total a pagar como la suma de los precios de los detalles de venta
            detalles = DetalleVenta.objects.filter(venta=self)
            self.total_pagar = detalles.aggregate(total=Sum('precio_unitario * cantidad'))['total'] or 0
            # Calcula el pendiente de pago
            self.pendiente_pago = self.total_pagar - self.total_pagado
            # Actualiza el estado de pago
            if self.pendiente_pago > 0:
                self.estado_pago = 'Pagado parcialmente'
            elif self.pendiente_pago == 0:
                self.estado_pago = 'Pagado'
            else:
                self.estado_pago = 'Crédito'
        
        super().save(*args, **kwargs)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_venta')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.producto} x {self.cantidad}"