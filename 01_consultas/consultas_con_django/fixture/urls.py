from django.urls import path
from . import views

urlpatterns = [
    path('integrantes/', views.getIntegrantes),
    path('integrantesPorFechaDeNacimiento/<str:fecha_nacimiento>/', views.integrantesPorFechaDeNacimiento),
    path('integrantesPorRangoDeFechaDeNacimiento/<str:fecha_inicial>/<str:fecha_final>/', views.integrantesPorRangoDeFechaDeNacimiento),
]