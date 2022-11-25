import logging as log
import Ejercicio_carreras.clases_dao.apostantes_dao as apdao
import Ejercicio_carreras.clases.apostantes as ap

ID = 0
NOMBRE = 1
SALDO = 2
SEPARADOR_DATOS = "|"

if __name__ == "__main__":
    #Leo archivo apostantes
    apostante = []
    log.debug("Empezando a leer el archivo")
    with open('ficheros/apostantes.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            log.debug(linea)
            datos = linea.split(SEPARADOR_DATOS)
            log.debug(datos)
            #Creo objeto de cada Gran Premio
            apostante = ap.Apostantes(datos[ID], datos[NOMBRE], datos[SALDO])
            #Inserto el Gran Premio en la base de datos usando el método dao
            apdao.Apostantes_Dao.insertar(apostante)