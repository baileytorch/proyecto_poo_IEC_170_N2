from modelos.comuna import Comuna
from prettytable import PrettyTable
from datos import obtener_datos_objetos
from iu import ingresar_nombre_comuna, ingresar_codigo_comuna
from auxiliares import normalizar_cadena
from datos import insertar_objeto


def listado_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas.field_names = ['N°', 'Código Comuna', 'Nombre Comuna']
    listado_comunas = obtener_datos_objetos(Comuna)
    if listado_comunas:
        for comuna in listado_comunas:
            tabla_comunas.add_row(
                [comuna.id, comuna.codigo_comuna, comuna.nombre_comuna])
            # print(f'{comuna.id} {comuna.codigo_comuna} {comuna.nombre_comuna}')
        print(tabla_comunas)


def obtener_comuna_nombre(buscar_comuna):
    listado_comunas = obtener_datos_objetos(Comuna)
    comuna_encontrada = None
    if listado_comunas:
        for comuna in listado_comunas:
            if normalizar_cadena(comuna.nombre_comuna) == normalizar_cadena(buscar_comuna):
                comuna_encontrada = comuna
                break
    return comuna_encontrada


def insertar_comuna():
    comuna = ingresar_nombre_comuna()

    comuna_encontrada = obtener_comuna_nombre(comuna)
    if comuna_encontrada == None:
        codigo = ingresar_codigo_comuna()
        # INSTANCIA DE CLASE
        nueva_comuna = Comuna(
            nombre_comuna=comuna,
            codigo_comuna=codigo,
            habilitado=True)
        insertar_objeto(nueva_comuna)
    else:
        print('Su marca YA existe en base de datos.')
