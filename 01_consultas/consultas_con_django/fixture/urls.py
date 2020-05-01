from django.urls import path, re_path
from . import views

urlpatterns = [
    path('integrantes/', views.getIntegrantes),
    path('integrantesPorFechaDeNacimiento/<str:fecha_nacimiento>/', views.integrantesPorFechaDeNacimiento),
    path('integrantesPorRangoDeFechaDeNacimiento/<str:fecha_inicial>/<str:fecha_final>/', views.integrantesPorRangoDeFechaDeNacimiento),
    re_path(r'^getJugadores/$', views.getJugadores),
]