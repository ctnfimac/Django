from django.db import models

# Create your models here.
class Integrante(models.Model):
    cod_integrante = models.IntegerField('codigo integrante', null = False, blank = False)
    nombre = models.CharField('Nombre', max_length = 50, null = False, blank = True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento',auto_now_add = True)

