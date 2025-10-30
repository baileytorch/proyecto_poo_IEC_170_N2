from modelos.comuna import Comuna
from prettytable import PrettyTable
from datos import obtener_datos_objetos


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
