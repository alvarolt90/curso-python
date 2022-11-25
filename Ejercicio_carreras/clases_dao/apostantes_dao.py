from Ejercicio_carreras.utils.conexiones import get_mysql_conection
import Ejercicio_carreras.clases.apostantes as ap
import logging as log

class Apostantes_Dao:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM apostantes ORDER BY id'
    _INSERTAR = 'INSERT INTO apostantes(id, nombre, saldo) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE apostantes SET id=%s, nombre=%s, saldo=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM apostantes WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                apostantes = []
                for registro in registros:
                    apostantes = ap.Apostantes(registro[0], registro[1], registro[2])
                    apostantes.append(apostantes)

                return apostantes

    @classmethod
    def insertar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostantes.id, apostantes.nombre, apostantes.saldo)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Apostante insertado: {apostantes}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostantes.id, apostantes.nombre, apostantes.saldo)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Apostante actualizado: {apostantes}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, apostantes.id)
                log.debug(f'Apostante eliminado: {apostantes}')
                return cursor.rowcount