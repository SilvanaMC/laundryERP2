from django.urls import path
from . import views

app_name='ventas'

urlpatterns = [
    path('', views.lista_venta, name='lista_ventas'),
    path('detalle/<int:id>', views.detalle_venta, name='detalle_venta'),
    path('crear/', views.crear_venta, name='crear_venta'),
    path('eliminar/<int:id>', views.eliminar_venta, name='eliminar_venta'),
    path('actualizar_venta/<int:id>', views.actualizar_venta, name='actualizar_venta'),
]