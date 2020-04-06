from django.shortcuts import render
from django.http import JsonResponse
from fixture.models import Integrante


# Create your views here.
def getIntegrantes(request):
    registros = Integrante.objects.all()
    respuesta = {
        "type":"Integrante",
        "features":[]
    }

    for registro in registros:
        dato = {
            "cod_integrante": registro.cod_integrante,
            "nombre": registro.nombre,
            "fecha_nacimiento": registro.fecha_nacimiento        
        }
        respuesta["features"].append(dato)
    # test = {
    #         "cod_integrante": '001',
    #         "nombre": 'teodorico',
    #         "fecha_nacimiento": '08-10-1957',
    #         "telefonos":[
    #             {
    #                 "telefono": "46446645"
    #             },
    #             {
    #                 "telefono": "46690289"   
    #             }
    #         ]        
    #     }
    return JsonResponse(respuesta)