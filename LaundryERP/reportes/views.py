from django.shortcuts import render
from ventas.models import Venta
from .forms import ReporteVentasForm
from django.db.models import Count
from django.db.models import Sum
from ordenes.models import OrdenDeServicio


# Create your views here.
def reporte_ventas(request):
    ordenes = None 
    total_ordenes = 0
    total_monto = 0
    metodo_pago_mas_usado = None
    
    if request.method == 'POST':
        form = ReporteVentasForm(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            ordenes = OrdenDeServicio.objects.filter(fecha_creacion__date__range=[fecha_inicio, fecha_fin])
            total_ordenes= ordenes.count()
            total_monto = ordenes.aggregate(Sum('total_monto'))['total_monto__sum'] or 0           
    else:
        form = ReporteVentasForm()
        
    return render(request,'reportes/reporte_ventas.html',{'form':form, 'ordenes':ordenes, 'total_ordenes':total_ordenes, 'total_monto':total_monto})        
           
            
    
    
    
