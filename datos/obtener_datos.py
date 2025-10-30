from datos.conexion import sesion
from modelos.marca import Marca
from auxiliares.normalizar_cadena import normalizar_cadena


def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(objeto).filter_by(habilitado=True).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_marca_nombre(nombre_marca):
    listado_marcas = obtener_datos_objetos(Marca)
    marca_encontrada = None
    if listado_marcas:
        for marca in listado_marcas:
            if normalizar_cadena(marca.nombre_marca) == normalizar_cadena(nombre_marca):
                marca_encontrada = marca
                break
    return marca_encontrada
