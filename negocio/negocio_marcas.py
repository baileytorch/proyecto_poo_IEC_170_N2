from prettytable import PrettyTable
from modelos.marca import Marca
from datos import modificar_objeto, obtener_datos_objetos, insertar_objeto, eliminar_objeto
from prettytable import PrettyTable
from auxiliares import normalizar_cadena
from negocio.negocio_paises import obtener_pais_nombre
from iu import ingresar_nombre_marca, ingresar_pais_origen, ingresar_nuevo_nombre_marca


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


def obtener_marca_nombre(nombre_marca):
    listado_marcas = obtener_datos_objetos(Marca)
    marca_encontrada = None
    if listado_marcas:
        for marca in listado_marcas:
            if normalizar_cadena(marca.nombre_marca) == normalizar_cadena(nombre_marca):
                marca_encontrada = marca
                break
    return marca_encontrada


def insertar_marca():
    marca = ingresar_nombre_marca()

    marca_encontrada = obtener_marca_nombre(marca)
    if marca_encontrada == None:
        buscar_pais = ingresar_pais_origen()
        pais_encontrado = obtener_pais_nombre(buscar_pais)
        if pais_encontrado != None:
            # INSTANCIA DE CLASE
            nueva_marca = Marca(nombre_marca=marca,
                                id_pais=pais_encontrado.id,
                                habilitado=True)
            insertar_objeto(nueva_marca)
    else:
        print('Su marca YA existe en base de datos.')


def modificar_marca():
    marca = ingresar_nombre_marca()

    marca_encontrada = obtener_marca_nombre(marca)
    if marca_encontrada:
        nuevo_nombre_marca = ingresar_nuevo_nombre_marca()
        nuevo_pais_marca = ingresar_pais_origen()
        if nuevo_nombre_marca != '':
            marca_encontrada.nombre_marca = nuevo_nombre_marca
        if nuevo_pais_marca != '':
            marca_encontrada.pais_origen = nuevo_pais_marca.title()
        modificar_objeto()


def eliminado_logico_marca():
    marca = ingresar_nombre_marca()

    marca_encontrada = obtener_marca_nombre(marca)
    if marca_encontrada:
        marca_encontrada.habilitado = False
        modificar_objeto()


def eliminado_fisico_marca():
    while True:
        marca = ingresar_nombre_marca()

        marca_encontrada = obtener_marca_nombre(marca)
        if marca_encontrada:
            eliminar_objeto(marca_encontrada)
            break
        else:
            print('Marca NO existe, vuelva a intentarlo.')
