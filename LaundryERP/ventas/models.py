from django.db import models
from ordenes.models import OrdenDeServicio

# Create your models here.

class Venta(models.Model):
    METODOS_DE_PAGO=[
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de Debito o Credito'),
        ('cheque', 'Cheque'),
    ]

    orden_servicio=models.OneToOneField(OrdenDeServicio, on_delete=models.CASCADE)
    monto_total=(models.DecimalField(max_digits=10, decimal_places=2))
    fecha_venta=models.DateTimeField(auto_now_add=True) #Hay que agregar el auto now_add
    metodo_pago=models.CharField(max_length=20, choices=METODOS_DE_PAGO)
    

    def __str__(self):
        return f"Venta #{self.id} - ${self.monto_total}"

