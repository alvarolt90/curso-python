from Ejercicio_carreras.utils.conexiones import get_mysql_conection
import Ejercicio_carreras.clases.gran_premio as gp
import logging as log

class Gran_Premio_Dao:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM gran_premio ORDER BY id'
    _INSERTAR = 'INSERT INTO gran_premio(id, nombre, distancia, num_carreras) VALUES(%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE gran_premio SET id=%s, nombre=%s, distancia=%s, num_carreras=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM gran_premio WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                gran_premio = []
                for registro in registros:
                    gran_premio = gp.Gran_Premio(registro[0], registro[1], registro[2], registro[3])
                    gran_premio.append(gran_premio)

                return gran_premio

    @classmethod
    def insertar(cls, gran_premio):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                valores = (gran_premio.id, gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Gran Premio insertado: {gran_premio}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, gran_premio):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                valores = (gran_premio.id, gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Gran Premio actualizado: {gran_premio}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, gran_premio):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                cursor.execute(cls._ELIMINAR, gran_premio.id)
                log.debug(f'Gran Premio eliminado: {gran_premio}')
                return cursor.rowcount