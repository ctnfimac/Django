from django.contrib import admin
from .models import *
# Register your models here.


class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('cod_integrante','nombre','fecha_nacimiento',)
    date_hierarchy = ('fecha_nacimiento')


admin.site.register(Integrante, IntegranteAdmin)
