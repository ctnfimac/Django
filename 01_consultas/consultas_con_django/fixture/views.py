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


"""
@brief: integrantesPorFechaDeNacimiento
@details: obtengo todos los integrantes que tengan una fecha de nacimiento 
          específica.
"""
def integrantesPorFechaDeNacimiento(request, fecha_nacimiento):
    try:
        integrantes = Integrante.objects.filter(fecha_nacimiento = fecha_nacimiento)
        respuesta = {
                "type": "Integrante",
                "features": []
            }
        for integrante in integrantes:
            dato = {
                "cod_integrante": integrante.cod_integrante,
                "nombre": integrante.nombre,
                "fecha_nacimiento": integrante.fecha_nacimiento
            }   
            respuesta["features"].append(dato)   
    except Exception as e:
        respuesta = {
                "type": "Integrante",
                "error": str(e)
            }
        
    return JsonResponse(respuesta)

