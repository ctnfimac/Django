from django.db import models

# Create your models here.
class Integrante(models.Model):
    cod_integrante = models.IntegerField('codigo integrante', null = False, blank = False)
    nombre = models.CharField('Nombre', max_length = 50, null = False, blank = True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento',auto_now_add = True)


class Jugador(Integrante):
    cant_goles = models.IntegerField('Goles', null=True, blank=True, default= 0)
    fecha_debut = models.DateField('Fecha de debut', null = True, blank = True)


class Nacionalidad(models.Model):
    descripcion = models.CharField('Nacionalidad', max_length=100,  null=False, blank=False)


class DT(Integrante):
    anios_experiencia = models.IntegerField('Años de Experiencia', null=True, blank=False, default=0)
    nacionalidad = models.ForeignKey('Nacionalidad',  Nacionalidad)