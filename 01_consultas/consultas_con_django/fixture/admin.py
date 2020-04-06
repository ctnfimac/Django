from django.contrib import admin
from .models import *
# Register your models here.


class IntegranteAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_nacimiento')

admin.site.register(Integrante, IntegranteAdmin)
