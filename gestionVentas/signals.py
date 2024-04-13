
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DetalleVenta, Venta

@receiver(post_save, sender=DetalleVenta)
def update_venta_total(sender, instance, **kwargs):
    venta = instance.venta
    venta.calcular_total()
    venta.save()