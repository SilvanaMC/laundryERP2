from django import forms

class ReporteVentasForm(forms.Form):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Fecha Inicio',
                'type': 'date'
            }   
        ),
        label='Fecha Inicio'
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Fecha Fin',
                'type': 'date'
            }   
        ),
        label='Fecha Fin'
    )
    
    