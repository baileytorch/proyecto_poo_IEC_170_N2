from datos.conexion import sesion


def insertar_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.commit()
        print("El objeto se ha insertado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al insertar el objeto: {e}")
    finally:
        sesion.close()


def modificar_objeto():
    try:
        sesion.commit()
        print("El objeto se ha actualizado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al actualizar el objeto: {e}")
    finally:
        sesion.close()
