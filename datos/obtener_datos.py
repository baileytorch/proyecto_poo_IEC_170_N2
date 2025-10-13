from datos.conexion import Session
from modelos.comuna import Comuna
from modelos.marca import Marca
from sqlalchemy import func


sesion = Session()


def obtener_datos_comunas():
    listado_comunas = sesion.query(Comuna).all()
    if listado_comunas:
        for comuna in listado_comunas:
            print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')


def obtener_datos_marcas():
    listado_marcas = sesion.query(Marca).all()
    if len(listado_marcas) > 0:
        for marca in listado_marcas:
            print(f'{marca.id} {marca.nombre_marca} {marca.pais_origen}')
