# Generated by Django 5.0.4 on 2024-04-12 22:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionVentas', '0002_remove_transaccion_cliente_venta_detalleventa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='id',
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_ventas',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
