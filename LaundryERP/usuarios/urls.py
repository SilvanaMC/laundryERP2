from django.urls import path
from . import views

app_name='usuarios'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_empleado, name='login'),
    path('logout/', views.logout_empleado, name='logout'),
    path('registrar/', views.registrar_empleado, name='registar_empleado'),
    path('lista/', views.lista_empleados, name='lista_empleados'),
]