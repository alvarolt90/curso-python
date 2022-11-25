import logging as log
import random
import clases.caballos as cb
import clases.gran_premio as gp
import clases.apostantes as ap
from datetime import datetime

#Método para iniciar una carrera
def iniciar_carrera():
    #Recorriendo los caballos para saber el ganador
    for caballo in cb.Caballos:
        edad = cb.Caballos.fecha_nacimiento - datetime.now()
        #Calculo la distancia recorrida sumando la velocidad, experiencia y metros aleatorios, le resto la edad calculada
        caballo.dist_recorrida += (cb.Caballos.velocidad+cb.Caballos.experiencia+random.randint(1, 50)-edad)
        #Añado los caballos participantes
        cb.Caballos.append(caballo)

    #Recorriendo los caballos participantes
    for caballo in cb.Caballos:
        if caballo.dist_recorrida > ganador.dist_recorrida:
            ganador = caballo
    log.info(f"Ha ganado el caballo {ganador}")

#Método generar apuesta
def apostar():
    #Recorro los posibles apostantes
    for apostante in ap.Apostantes:
        #Si el apostante tiene dinero se realiza la apuesta
        if apostante.saldo > 0:
            saldo = input("¿Cuanto saldo quieres apostar?")
            while saldo > apostante.saldo:
                saldo = random.randint(1, 200)
                for caballo in cb.Caballos:
                    log.info(caballo)
            caballo_elegido = input("Elige el caballo")
            apostante.saldo_apostado = saldo
            apostante.caballo_apostado = caballo
            #Descuento el saldo apostado de la cuenta
            apostante.saldo -= saldo
            log.info(f"{apostante.nombre} ha apostado por el caballo {caballo_elegido} {saldo} dinero")

#Método mostrar resumen
def mostrar_resumen():
    #Datos de cada apostante
    for apostante in ap.Apostantes:
        log.info(f"{ap.Apostantes.nombre} tiene {ap.Apostantes.saldo} de saldo")

########################################################################################################################

#Iniciando
if __name__ == "__main__":
    #Recorro los grandes premios para iniciar las carreras y las apuestas
    for gran_premio in gp.Gran_Premio:
        log.info(f"Comienza el Gran premio: {gp.Gran_Premio.nombre}")
        iniciar_carrera()
        apostar()
        mostrar_resumen()


