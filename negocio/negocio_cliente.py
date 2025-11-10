from prettytable import PrettyTable

from auxiliares import normalizar_cadena
from datos.obtener_datos import obtener_datos_objetos
from modelos import Cliente


def listado_clientes():
    tabla_clientes = PrettyTable()
    tabla_clientes.field_names = ['N°', 'RUT', 'Nombre','Correo','Teléfono']
    listado_clientes = obtener_datos_objetos(Cliente)
    if listado_clientes:
        for cliente in listado_clientes:
            tabla_clientes.add_row(
                [cliente.id, cliente.rut_cliente, cliente.razon_social,cliente.correo_contacto,cliente.telefono_contacto])
        print(tabla_clientes)


def obtener_cliente_nombre(nombre_cliente):
    listado_clientes = obtener_datos_objetos(Cliente)
    cliente_encontrado = None
    if listado_clientes:
        for cliente in listado_clientes:
            if normalizar_cadena(cliente.razon_social) == normalizar_cadena(nombre_cliente):
                cliente_encontrado = cliente
                break
    return cliente_encontrado


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