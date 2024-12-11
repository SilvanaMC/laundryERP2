from django.shortcuts import render, redirect, get_object_or_404
from .forms import VentaForm
from.models import Venta
from django.contrib import messages

# Create your views here.

def lista_venta(request):
    ventas = Venta.objects.all()
    return render(request,'ordenes/lista_venta.html',{'ventas':ventas})

def detalle_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    return render(request,'venta/detalle_venta.html',{'venta':venta})

def crear_venta(request):
    if request.method == 'POST':
        form = Venta(request.POST)
        if form.is_valid():
            venta = form.save()
            venta.orden_servicio.pago_realizado=True
            venta.orden_servicio.save()    
            messages.success(request, 'La venta ha sido creada con éxito!')
            return redirect('ventas:lista_venta')
    else:
        form = VentaForm()      
    return render(request,'ventas/crear_venta.html', {'form':form})
 
def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        form = Venta(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, f'La venta {venta.id}  ha sido actualizada')
            return redirect('ventas:lista_ventas.html')
    else:
        form = Venta(instance=venta)  # Pass the instance to the form for pre-filling the form fields with the current data.
    return render(request, 'venta/actualizar_venta.html', {'form': form, 'venta': venta})
        

def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, f'La venta {venta.id} ha sido eliminada')
        return redirect('ventas:lista_ventas')
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})
