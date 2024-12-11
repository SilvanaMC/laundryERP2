from django.urls import path
from . import views

app_name = 'reportes' 

urlpatterns = [
    path( 'ventas/', views.reporte_ventas, name= 'reporte_ventas'),
    
]
