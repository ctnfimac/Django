from django.db import models

# Create your models here.
class Integrante(models.Model):
    # cod_integrante = models.IntegerField('codigo integrante', null = False, blank = False)
    nombre = models.CharField('Nombre', max_length = 50, null = False, blank = False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')

# se relaciona con el Jugador
class Posicion(models.Model):
    descripcion = models.CharField("Posición", max_length = 50, null = False)

    def __str__(self):
        return self.descripcion

class Jugador(Integrante):
    fecha_debut = models.DateField('Fecha Debut', auto_now_add=True)
    cant_goles = models.IntegerField('Cantidad de Goles', null = False, default= 0)
    posicion = models.ForeignKey(Posicion, on_delete = models.CASCADE, null= True)