from datos import obtener_datos_objetos
from auxiliares import normalizar_cadena
from modelos.pais import Pais

def obtener_pais_nombre(buscar_pais):
    listado_paises = obtener_datos_objetos(Pais)
    pais_encontrado = None
    if listado_paises:
        for pais in listado_paises:
            if normalizar_cadena(pais.nombre_pais) == normalizar_cadena(buscar_pais):
                pais_encontrado = pais
                break
    return pais_encontrado