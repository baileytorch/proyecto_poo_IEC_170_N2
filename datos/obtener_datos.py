from datos.conexion import Session
from modelos.comuna import Comuna
from modelos.marca import Marca
from sqlalchemy import func


sesion = Session()


def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if listado_objetos:
        return listado_objetos
