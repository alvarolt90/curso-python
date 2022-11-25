import logging as log
import Ejercicio_carreras.clases_dao.caballos_dao as cabdao
import Ejercicio_carreras.clases.caballos as cab

ID = 0
NOMBRE = 1
FECHA_NACIMIENTO = 2
VELOCIDAD = 3
EXPERIENCIA = 4
VALOR_APUESTA = 5
ID_GRAN_PREMIO = 6
SEPARADOR_DATOS = "|"

if __name__ == "__main__":
    #Leo archivo caballos
    caballo = []
    log.debug("Empezando a leer el archivo")
    with open('../ficheros/caballos.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            log.debug(linea)
            datos = linea.split(SEPARADOR_DATOS)
            log.debug(datos)
            #Creo objeto de cada Caballo
            caballo = cab.Caballos(datos[ID], datos[NOMBRE], datos[FECHA_NACIMIENTO],
                            datos[VELOCIDAD], datos[EXPERIENCIA], datos[VALOR_APUESTA], datos[ID_GRAN_PREMIO].split(SEPARADOR_DATOS))
            #Inserto el Gran Premio en la base de datos usando el método dao
            cabdao.Caballos_Dao.insertar(caballo)