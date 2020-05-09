from django.contrib import admin
from .models import *


class PosicionAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    #read_only = ['id']

##
# Jugador
###
class JugadorAdmin(admin.ModelAdmin):
    list_display =  ('id','nombre','fecha_nacimiento','fecha_debut','cant_goles','posicion_id')
    date_hierarchy = ('fecha_debut')


admin.site.register(Posicion, PosicionAdmin)
admin.site.register(Jugador, JugadorAdmin)

