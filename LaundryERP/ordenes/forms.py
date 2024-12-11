from django import forms
from .models import OrdenDeServicio, Prenda, Cliente 
from usuarios.models import Usuario  
from django.contrib.auth.forms import AuthenticationForm


class OrdenDeServicioForm(forms.ModelForm):
    class Meta:  
        model = OrdenDeServicio
        fields = ['cliente', 'empleado', 'prendas', 'estado']
        
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label='Seleccione un Cliente', widget=forms.Select(attrs={'class': 'form-control'}))
    empleado = forms.ModelChoiceField(queryset=Usuario.objects.filter(rol='empleado'), empty_label='Seleccione un Empleado', widget=forms.Select(attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(choices=OrdenDeServicio.ESTADOS, initial='pendiente', widget=forms.Select(attrs={'class': 'form-control'}))
    prendas = forms.ModelMultipleChoiceField(queryset=Prenda.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super(OrdenDeServicioForm,self).__init__(*args, **kwargs)
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['cliente'].widget.attrs.update({'class': 'form-control'})
        self.fields['empleado'].widget.attrs.update({'class': 'form-control'})
        self.fields['prendas'].widget.attrs.update({'class': 'form-control'})
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido', 'correo', 'direccion', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido': forms.TextInput(attrs = {'class': 'form-control'}),
            'correo': forms.EmailInput(attrs = {'class': 'form-control'}),
            'direccion': forms.Textarea(attrs = {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs = {'class': 'form-control'}),
        }

        