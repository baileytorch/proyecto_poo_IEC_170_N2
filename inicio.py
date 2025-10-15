from datos.obtener_datos import obtener_datos_objetos
from prettytable import PrettyTable

from modelos.comuna import Comuna
from modelos.marca import Marca


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


def listado_marcas():
    tabla_marcas = PrettyTable()
    tabla_marcas.field_names = ['N°', 'Marca', 'País de Origen']
    listado_marcas = obtener_datos_objetos(Marca)
    if listado_marcas:
        for marca in listado_marcas:
            tabla_marcas.add_row(
                [marca.id, marca.nombre_marca, marca.pais_origen])
            # print(f'{marca.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_marcas)


listado_marcas()


# from iu.menu_principal import menu_principal

# menu_principal()
