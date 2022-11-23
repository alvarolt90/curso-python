import random
import excepciones
import logging as log
from abc import ABC

#Desactivando log.info o superior
log.basicConfig(level=log.DEBUG)

#Decorador para afinar los instrumentos
def dec_afinar_instrumentos(afinar):
    def afinando():
        log.debug("Se empieza a afinar el instrumento")
        afinar()
        log.debug("Se ha terminado de afinar el instrumento")
    return afinando

#Decorador para tocar los instrumentos
def dec_tocar_instrumentos(tocar):
    def tocando():
        log.debug("Se empieza a tocar el instrumento")
        tocar()
        log.debug("Se ha terminado de tocar el instrumento")
    return tocando

#Creación de clases
class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    #Método para afinar el instrumento usando decorador de logs
    @dec_afinar_instrumentos
    def afinar(self):
        afinacion = random.randint(0, 10)
        if afinacion >= 5:
            raise excepciones.AfinacionException("Está afinado correctamente")
        else:
            raise excepciones.AfinacionException("El instrumento no está afinado correctamente")

    #Método para tocar el instrumento usando decorador de logs
    @dec_tocar_instrumentos
    def tocar(self, instrumento):
        print(f"Tocando el {instrumento.nombre} de manera correcta")

class Guitarra(Instrumento):
    def __init__(self, num_cuerdas, nombre, tipo):
        Instrumento.__init__(self, nombre, tipo)
        self.num_cuerdas = num_cuerdas

class Guitarra_Electrica(Guitarra):
    def __init__(self, potencia, num_cuerdas, nombre, tipo):
        Guitarra.__init__(self, num_cuerdas, nombre, tipo)
        self.potencia = potencia

class Piano(Instrumento):
    def __init__(self, num_teclas, nombre, tipo):
        Instrumento.__init__(self, nombre, tipo)
        self.num_teclas = num_teclas

class Tambor(Instrumento):
    def __init__(self, tamanio, nombre, tipo):
        Instrumento.__init__(self, nombre, tipo)
        self.tamanio = tamanio
    #Método aporrear el tambor
    def aporrear(self):
        print(f"Aporreando el tambor {self.nombre}")

class Orquesta:
    def __init__(self, nombre):
        self.nombre = nombre

    #Método para crear la orquesta
    def crearOrquesta(self):
            guitarra = Guitarra(7, "Guitarra", "Cuerda")
            guitarra_electrica = Guitarra_Electrica("10W", 7, "Guitarra Eléctrica", "Cuerda")
            piano = Piano(44, "Piano", "Cuerda percutida")
            tambor = Tambor("24 cm", "Tambor", "Percusión")
            #Lista de instrumentos
            self.instrumentos = [guitarra, guitarra_electrica, piano, tambor]

    #Método para iniciar el concierto
    def iniciarConcierto(self):
        for instrumento in self.instrumentos:
            instrumento.afinar()
            instrumento.tocar()

#Creacion de la orquesta
if __name__ == "__main__":
    orquesta = Orquesta("Orquesta Melodias")
    orquesta.crearOrquesta()
    orquesta.iniciarConcierto()