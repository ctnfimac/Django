from django.contrib import admin
from .models import *
# Register your models here.


<<<<<<< HEAD
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_nacimiento')

admin.site.register(Integrante, IntegranteAdmin)
=======
admin.site.register(Integrante)
admin.site.regiter(Posicion)
admin.site.register(Jugador)
admin.site.register(Nacionalidad)
admin.site.register(DT)
admin.site.regiter(Grupo)
admin.site.regiter(Equipo)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.regiter(Estadio)
admin.site.regiter(Ronda)
admin.site.regiter(TipoAutoridad)
admin.site.regiter(Autoridad)
admin.site.regiter(Partido)
>>>>>>> 030cce917051e1847f0397169312e4c27cb7a81f
