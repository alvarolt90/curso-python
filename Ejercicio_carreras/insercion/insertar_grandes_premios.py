import logging as log
import Ejercicio_carreras.clases_dao.gran_premio_dao as gpdao
import Ejercicio_carreras.clases.gran_premio as gp

ID = 0
NOMBRE = 1
DISTANCIA = 2
NUM_CARRERAS = 3
SEPARADOR_DATOS = "|"

if __name__ == "__main__":
    #Leo archivo grandes_premios
    gran_premio = []
    log.debug("Empezando a leer el archivo")
    with open('ficheros/grandes_premios.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            log.debug(linea)
            datos = linea.split(SEPARADOR_DATOS)
            log.debug(datos)
            #Creo objeto de cada Gran Premio
            gran_premio = gp.Gran_Premio(datos[ID], datos[NOMBRE], datos[DISTANCIA], datos[NUM_CARRERAS])
            #Inserto el Gran Premio en la base de datos usando el método dao
            gpdao.Gran_Premio_Dao.insertar(gran_premio)