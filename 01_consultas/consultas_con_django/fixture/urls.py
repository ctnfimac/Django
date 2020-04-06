from django.urls import path
from . import views

urlpatterns = [
    path('integrantes/', views.getIntegrantes)
]