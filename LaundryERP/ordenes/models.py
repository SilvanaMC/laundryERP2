from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Prenda(models.Model):
    TIPO_PRENDA_CHOICES =  [
        ('pantalon', 'Pantalón'),
        ('camisa', 'Camisa'),
        ('saco', 'Saco'),
        ('calcetines', 'Calcetines'),
        ('zapatos', 'Zapatos'),
        ('medias', 'Medias'),
        ('blusa', 'Blusa'),
        ('chaleco', 'Chaleco'),
        ('traje', 'Traje'),
        ('pantalones_jeans', 'Pantalones Jeans'),
        ('chaquetas', 'Chaquetas'),
        ('jeans', 'Jeans'),
        ('jersey', 'Jersey'),
        ('sweater', 'Sweater'),
        ('t-shirt', 'T-Shirt'),
        ('buzo', 'Buzo'),
        ('sudadera', 'Sudadera'),
        ('pantalones_shorts', 'Pantalones Shorts'),
    ]
    tipo_prenda=models.CharField(max_length=50, choices=TIPO_PRENDA_CHOICES, default= 'pantalon') 
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.TextField()

    def __str__(self):
        return f'{self.tipo_prenda} - {self.precio}'
# crear el modelo cliente 
class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.EmailField(unique=True) #con unique=true se establece para que los correos sean unicos
    direccion=models.TextField()
    
    def __str__(self):
        return self.nombre

     
#Creacion de modelo de Orden de servicio 
class OrdenDeServicio(models.Model):
    ESTADOS=[
        ('pendiente', 'Pendiente'),
        ('proceso', 'En Proceso'),
        ('completada', 'Completada')
    ]

    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado=models.ForeignKey(Usuario, on_delete=models.SET_NULL,null=True)
    prendas=models.ManyToManyField(Prenda, related_name='ordenes'), #Se asocia mas de una prenda a la orden y la misma prenda puede estar en varias ordenes
    fecha_creacion=models.DateTimeField(auto_now_add=True) # no se requiere agregar mas parametros 
    estado=models.CharField(max_length=20 , choices=ESTADOS, default='pendiente') #'pendiente', va el valor no la etiqueta
    total=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pago_realizado=models.BooleanField(default=False)

    #Calculo del total de la orden sumando los precios de las prendas asociadas
    def calculo_total(self):
        self.total=sum(prenda.precio for prenda in self.prendas.all())
        self.save()
        return self.total


    def __str__(self):   # devielve cadena de caracteres 
        return f"Orden #{self.id} - {self.cliente.nombre} - {self.estado} - {self.total}"