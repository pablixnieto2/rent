from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    # Asegúrate de definir las opciones para tu campo Enum
    TIENDA_OPCIONES = (
        ('Madrid', 'Madrid'),
        ('Barcelona', 'Barcelona'),
        ('Valencia', 'Valencia'),
        ('Videollamada', 'Videollamada'),
        # ...
    )
    
    tienda = models.CharField(max_length=50, choices=TIENDA_OPCIONES)
    
    TIPO_OPCIONES = (
        ('Alquiler','Alquiler'),
        ('Venta','Venta'),
    )
    
    tipo = models.CharField(max_length=50, choices=TIPO_OPCIONES)
    
    CATEGORIA_OPCIONES = (
        ('Vestido','Vestido'),
        ('Vestido Corto','Vestido Corto'),
        ('Accesorios','Accesorios'),
        ('Complementos','Complementos'),
        ('Envio','Envio'),
        ('Invitaciones','Invitaciones'),
        ('Paquete Fotos','Paquete Fotos'),
        ('Recuerdos','Recuerdos'),
        ('Otros','Otros'),
    )
    
    categoria = models.CharField(max_length=50, choices=CATEGORIA_OPCIONES)
    nombre = models.CharField(max_length=100)
    
    COLOR_OPCIONES = (
        ('Rosa','Rosa'),
        ('Rojo','Rojo'),
        ('Azul','Azul'),
        ('Turquesa','Turquesa'),
        ('Verde','Verde'),
        ('Amarillo','Amarillo'),
        ('Rosa Dorado','Rosa Dorado'),
        ('Azul Oscuro','Azul Oscuro'),
        ('Negro','Negro'),
        ('Otro','Otro'),
    )
    
    color = models.CharField(max_length=50, choices=COLOR_OPCIONES)
    talla = models.CharField(max_length=50)
    pvp = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_productos/')
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Almacen(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    # Otros campos relevantes para el almacén...

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventario')
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name='inventario')
    cantidad = models.IntegerField(default=0)
    # Campos adicionales como fecha de último movimiento, etc.