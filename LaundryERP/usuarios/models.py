from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES=[('admin', 'Administrador'), 
           ('empleado', 'Empleado')
           ]
    #Agregando nuevos campos al modelo 
    rol=models.CharField(max_length=100, choices=ROLES, default='empleado')
    
# Create your models here.

    
