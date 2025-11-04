from datos.conexion import sesion


def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(objeto).filter_by(habilitado=True).all()
    if len(listado_objetos) > 0:
        return listado_objetos

def obtener_datos_objetos_deshabilitados(objeto):
    listado_objetos = sesion.query(objeto).filter_by(habilitado=False).all()
    if len(listado_objetos) > 0:
        return listado_objetos
