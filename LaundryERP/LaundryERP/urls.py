
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('ordenes/', include(('ordenes.urls', 'ordenes'), namespace='ordenes')),
    path('ventas/', include(('ventas.urls', 'ventas'), namespace='ventas')),
    path('reportes/', include(('reportes.urls', 'reportes'), namespace='reportes')),
]
