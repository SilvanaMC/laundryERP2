from django.urls import path
from . import views

app_name='ordenes'

urlpatterns = [
    path('', views.lista_ordenes, name='lista_ordenes'),
    path('detalle/<int:id>', views.detalle_orden, name='detalle_orden'),
    path('crear/', views.crear_orden, name='crear_orden'),
    path('eliminar/<int:id>', views.eliminar_orden, name='eliminar_orden'),
    path('actualizar_estado/<int:id>', views.actualizar_estado, name='actualizar_estado'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes')   
]