from django import forms
from .models import OrdenDeServicio
from usuarios.models import Usuario
from ventas.models import Venta
from django.contrib.auth.forms import AuthenticationForm

class VentaForm(forms.ModelForm):
    class Meta: 
        model = Venta
        fields = ['orden_servicio', 'monto_total', 'metodo_pago']
        widgets = {
            'orden_servicio': forms.Select(attrs={'class': 'form-control'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Monto Total'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
        }
        
        def __init__(self, *args, **kwargs):
            super(VentaForm,self).__init__(*args, **kwargs)
            self.fields['orden_servicio'].queryset = OrdenDeServicio.objects.filter(pago_realizo=False)
            







'''METODOS_DE_PAGO=[
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de Debito o Credito'),
        ('cheque', 'Cheque'),
    ]

    orden_servicio=models.OneToOneField(OrdenDeServicio, on_delete=models.CASCADE)
    monto_total=(models.DecimalField(max_digits=10, decimal_places=2))
    fecha_venta=models.DateTimeField(auto_now_add=True) #Hay que agregar el auto now_add
    metodo_pago=models.CharField(max_length=20, choices=METODOS_DE_PAGO)'''