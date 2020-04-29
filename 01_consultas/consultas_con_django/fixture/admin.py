from django.contrib import admin
from .models import *
# Register your models here.


class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('cod_integrante','nombre','fecha_nacimiento',)
    # date_hierarchy = ('fecha_nacimiento')

admin.site.register(Integrante, IntegranteAdmin)



class JugadorAdmin(IntegranteAdmin):
    list_display = IntegranteAdmin.list_display + ('fecha_debut','cant_goles')
    date_hierarchy = ('fecha_debut')

admin.site.register(Jugador, JugadorAdmin)

