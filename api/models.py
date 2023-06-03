from django.db import models
import datetime

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    ap_paterno = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.IntegerField()

class Medico_Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    ap_paterno = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.IntegerField()

class Tecnico_Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    ap_paterno = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.IntegerField()

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    descripcion = models.TextField()