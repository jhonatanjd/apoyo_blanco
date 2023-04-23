from django.db import models
from .choices import *
from pyexpat import model
class soporte(models.Model):
    correo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)        

    class Meta:
        db_table ='soporte'


class cliente(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True) 
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)  
    class Meta:
        db_table ='cliente'

    def __str__(self):
            return self.nombres

class profesional(models.Model):
    correo = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    grado_estudio = models.CharField(max_length=40, choices=GRADO)
    especialidad = models.CharField(max_length=40, choices=ESPE)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)  
    class Meta:
        db_table ='profesional'

    def __str__(self):
            return self.nombres
           