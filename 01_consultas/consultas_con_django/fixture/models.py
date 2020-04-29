from django.db import models

# Create your models here.
class Integrante(models.Model):
    cod_integrante = models.IntegerField('codigo integrante', null = False, blank = False)
    nombre = models.CharField('Nombre', max_length = 50, null = False, blank = False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')

class Jugador(Integrante):
    fecha_debut = models.DateField('Fecha Debut')
    cant_goles = models.IntegerField('Cantidad de Goles', null = False, default= 0)