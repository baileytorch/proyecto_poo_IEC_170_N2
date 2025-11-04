from datos.conexion import sesion


def eliminar_objeto(objeto):
    sesion.delete(objeto)
    try:
        sesion.commit()
        print("El objeto se ha eliminado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al eliminar el objeto: {e}")
    finally:
        sesion.close()