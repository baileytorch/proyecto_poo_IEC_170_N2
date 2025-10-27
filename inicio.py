from datos.conexion import Session
from datos.obtener_datos import obtener_datos_objetos, obtener_marca_nombre
from iu.iu_marcas import ingresar_datos_marca
from prettytable import PrettyTable
from datos.insertar_datos import insertar_objeto, modificar_objeto

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


sesion = Session()


def insertar_marca():
    marca = input('Ingrese nombre marca: ')
    pais = input('Ingrese país de origen: ')

    respuesta = obtener_marca_nombre(marca)
    if respuesta == None:
        nueva_marca = Marca(nombre_marca=marca.title(),
                            pais_origen=pais.title())
        insertar_objeto(nueva_marca)
    else:
        print('Su marca YA existe en base de datos.')


def modificar_marca():
    marca = input('Ingrese nombre marca: ')

    marca_encontrada = obtener_marca_nombre(marca)
    if marca_encontrada:
        nuevo_nombre_marca = input('Ingrese nuevo nombre marca: ')
        nuevo_pais_marca = input('Ingrese país de origen: ')
        if nuevo_nombre_marca != '':
            marca_encontrada.nombre_marca = nuevo_nombre_marca
        if nuevo_pais_marca != '':
            marca_encontrada.pais_origen = nuevo_pais_marca.title()
        modificar_objeto()


modificar_marca()
# insertar_marca()

# listado_comunas()
# listado_marcas()

# from iu.menu_principal import menu_principal

# menu_principal()
