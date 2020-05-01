from django.shortcuts import render
from django.http import JsonResponse
from fixture.models import Integrante, Jugador
from django.db.models.functions import Lower # sirve para poder convertir en minuscula a los campos de una query


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



"""
@brief: integrantesPorRangoDeFechaDeNacimiento
@details: obtengo todos los integrantes esten dentro del rango de fecha de nacimiento
          indicada
"""
def integrantesPorRangoDeFechaDeNacimiento(request, fecha_inicial, fecha_final):
    respuesta = {
        "type": "Integrante",
        "cantidad": 0,
        "integrantes": []
    }
    try:
        tabla = Integrante.objects.filter(
                    fecha_nacimiento__gte = fecha_inicial, 
                    fecha_nacimiento__lte = fecha_final
                )
        for row in tabla:
            integrante = {
                "cod_integrante": row.cod_integrante,
                "nombre": row.nombre,
                "fecha_nacimiento": row.fecha_nacimiento
            }
            respuesta["integrantes"].append(integrante)
        respuesta["cantidad"] = len(tabla)
    except Exception as e:
        respuesta["error"] = str(e)
        
    return JsonResponse(respuesta)


"""
@brief: getJugadores
@details: obtengo todos los jugadores ordenados por nombre o no
"""
def getJugadores(request):
    ordenamiento = request.GET['orden']
    tipoDeOrdenamiento = ['cod_integrante','nombre','fecha_nacimiento','fecha_debut','cant_goles']
    respuesta = {
        "type": "Jugador",
        "cantidad": 0,
        "jugadores": []
    }
    try:
        if ordenamiento in tipoDeOrdenamiento:
            # El lower es para que no hayan problemas si las palabras inician
            # con minúsculas o mayúsculas
            registros = Jugador.objects.all().order_by(ordenamiento) if ordenamiento in 'cant_goles' else Jugador.objects.all().order_by(Lower(ordenamiento)) 
            for registro in registros:
                dato = {
                    "cod_integrante": registro.cod_integrante,
                    "nombre": registro.nombre,
                    "fecha_nacimiento": registro.fecha_nacimiento,
                    "fecha_debut": registro.fecha_debut,
                    "cant_goles": registro.cant_goles       
                }
                respuesta["jugadores"].append(dato)
            respuesta["cantidad"] = len(registros)
    except Exception as e:
        respuesta = {
            "type": "Jugador",
            "error": str(e)
        }

    return JsonResponse(respuesta)