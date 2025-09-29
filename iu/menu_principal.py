from auxiliares.info_aplicaion import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print(f'{nombre_aplicacion} v.{numero_version}')
    print('=======================================')
    print()
    print('[1] Gestion Empleados')
    print('[2] Gestion Proyectos')
    print('[3] Gestion Horario')
    print('[0] Salir')
