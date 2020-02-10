from django.db import models

# Create your models here.
class Integrante(models.Model):
    cod_integrante = models.IntegerField('codigo integrante', null = False, blank = False)
    nombre = models.CharField('Nombre', max_length = 50, null = False, blank = True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento',auto_now_add = True)


class Posicion(models.Model):
    descripcion = models.CharField('Posicion', max_length=100, null=False)


class Jugador(Integrante):
    cant_goles = models.IntegerField('Goles', null=True, blank=True, default= 0)
    fecha_debut = models.DateField('Fecha de debut', null = True, blank = True)
    posicion = models.ForeignKey('Posicion',Posicion, default = 0)


class Nacionalidad(models.Model):
    descripcion = models.CharField('Nacionalidad', max_length=100, null=False, blank=False)


class DT(Integrante):
    anios_experiencia = models.IntegerField('Años de Experiencia', null=True, blank=False, default=0)
    nacionalidad = models.ForeignKey('Nacionalidad',  Nacionalidad)


class Grupo(models.Model):
    descripcion = models.CharField('Grupo', max_length=2, null= False)


class Equipo(models.Model):
    nombre_equipo = models.CharField('Equipo', max_length=50, null= False)
    grupo = models.ForeignKey('Grupo', Grupo)

class Provincia(models.Model):
    descripcion = models.CharField('Provincia', max_length=50, null=False)

class Localidad(models.Model):
    descripcion = models.CharField('Localidad', max_length=50, null=False)
    provincia = models.ForeignKey('Provincia',Provincia, null=False)

class Estadio(models.Model):
    nombre = models.CharField('Estadio', max_length=100, null=False, blank=False)
    capacidad = models.IntegerField('Capacidad',null=False)
    localidad = models.ForeignKey('Localidad', Localidad, null=False)

     
class Partido(models.Model):
    goles = models.IntegerField('Goles',null=false,default=0)
    fecha_hora = models.DateField('Hora y fecha', null= True, blank= False)
    estadio = models.ForeignKey('Estadio', Estadio, null= False, blank= False)

