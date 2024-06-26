# Generated by Django 5.0.4 on 2024-04-10 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('label_precio', models.CharField(max_length=100)),
                ('almacen_m', models.IntegerField()),
                ('madrid', models.IntegerField()),
                ('barcelona', models.IntegerField()),
                ('tienda', models.CharField(choices=[('Madrid', 'Madrid'), ('Barcelona', 'Barcelona'), ('Valencia', 'Valencia'), ('Videollamada', 'Videollamada')], max_length=50)),
                ('tipo', models.CharField(choices=[('Alquiler', 'Alquiler'), ('Venta', 'Venta')], max_length=50)),
                ('categoria', models.CharField(choices=[('Vestido', 'Vestido'), ('Vestido Corto', 'Vestido Corto'), ('Accesorios', 'Accesorios'), ('Complementos', 'Complementos'), ('Envio', 'Envio'), ('Invitaciones', 'Invitaciones'), ('Paquete Fotos', 'Paquete Fotos'), ('Recuerdos', 'Recuerdos'), ('Otros', 'Otros')], max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('Rosa', 'Rosa'), ('Rojo', 'Rojo'), ('Azul', 'Azul'), ('Turquesa', 'Turquesa'), ('Verde', 'Verde'), ('Amarillo', 'Amarillo'), ('Rosa Dorado', 'Rosa Dorado'), ('Azul Oscuro', 'Azul Oscuro'), ('Negro', 'Negro'), ('Otro', 'Otro')], max_length=50)),
                ('talla', models.CharField(max_length=50)),
                ('pvp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen', models.ImageField(upload_to='imagenes_productos/')),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]
