from datos.conexion import Session
from modelos.marca import Marca
from auxiliares.normalizar_cadena import normalizar_cadena


sesion = Session()


def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_marca_nombre(nombre_marca):
    listado_marcas = obtener_datos_objetos(Marca)
    marca_encontrada = False
    if listado_marcas:
        for marca in listado_marcas:
            if normalizar_cadena(marca.nombre_marca) == normalizar_cadena(nombre_marca):
                marca_encontrada = True
    return marca_encontrada
