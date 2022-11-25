from Ejercicio_carreras.utils.conexiones import get_mysql_conection
import Ejercicio_carreras.clases.caballos as cab
import logging as log

class Caballos_Dao:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM caballos ORDER BY id'
    _INSERTAR = 'INSERT INTO caballos(id, nombre, fecha_nacimiento, velocidad, experiencia, valor_apuesta, id_gran_premio) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE caballos SET id=%s, nombre=%s, fecha_nacimiento=%s, velocidad=%s, experiencia=%s, valor_apuesta=%s, id_gran_premio=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM caballos WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                caballos = []
                for registro in registros:
                    caballos = cab.Caballos(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6])
                    caballos.append(caballos)

                return caballos

    @classmethod
    def insertar(cls, caballos):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                valores = (caballos.id, caballos.nombre, caballos.fecha_nacimiento, caballos.velocidad, caballos.experiencia, caballos.valor_apuesta, caballos.id_gran_premio)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Caballo insertado insertado: {caballos}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, caballos):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                valores = (caballos.id, caballos.nombre, caballos.fecha_nacimiento, caballos.velocidad, caballos.experiencia, caballos.valor_apuesta, caballos.id_gran_premio)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Caballo actualizado: {caballos}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, caballos):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                cursor.execute(cls._ELIMINAR, caballos.id)
                log.debug(f'Caballo eliminado: {caballos}')
                return cursor.rowcount