import random
from datetime import datetime, date

#Creación de clases

class Doctor:
    def __init__(self, nombre, apellidos, especialidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.especialidad = especialidad

class Enfermero(Doctor):
    def __init__(self, planta, nombre, apellidos, especialidad=None):
        Doctor.__init__(self, nombre, apellidos, especialidad)
        self.planta = planta

class Pacientes(Doctor):
    def __init__(self, sintomas, nombre, apellidos, especialidad=None):
        Doctor.__init__(self, nombre, apellidos, especialidad)
        self.sintomas = sintomas

class Enfermos:
    def __init__(self, enfermedad):
        self.enfermedad = enfermedad

class Hospital:
    def __init__(self, nombre, pacientes=[], enfermos=[], consultas=[], habitaciones=[]):
        self.nombre = nombre
        self.pacientes = pacientes
        self.enfermos = enfermos
        self.consultas = consultas
        self.habitaciones = habitaciones

    #Cada enfermero lleva al paciente a la consulta y un doctor lo diagnostica
    def atiendePaciente(self, sala_espera):
        for paciente in sala_espera:
            #El paciente ha sido atendido y lo añado a las consultas
            paciente.append(self.consultas)
            #Elimino al paciente de la sala de espera
            sala_espera = self.paciente.pop(0)
            print(f"El paciente {paciente.nombre} {paciente.apellidos} pasa a consulta")
            return paciente

    #Un doctor diagnostica al paciente generando numero aleatorio, si es mayor de 7, es enfermo y pasa a la habitacion
    def diagnostica(self, consultas):
        for paciente in consultas:
            diagnostico = random.randint(0, 10)
            if diagnostico > 7:
                #Se considera enfermo y pasa a la habitación
                paciente.append(self.enfermos)
                paciente.estaEnfermo()
                #El paciente sale de la consulta
                consultas = self.paciente.pop(0)
            else:
                print(f"El enfermo {paciente.nombre} ha sido dado de alta")
                paciente = self.paciente.pop(0)
            return paciente

    #Si el numero aleatorio es mayor de 7, es enfermo y pasa a la habitacion
    def estaEnfermo(self, enfermo):
        if len(self.habitaciones) < 3:
            enfermo.append(self.habitaciones)
        else:
            print("El enfermo se traslada a otro hospital")

    #Método para que los doctores y los enfermeros fichen
    def fichar(self, doctor=None, enfermero=None):
        hora = datetime.now()
        if doctor != None:
            print(f"El doctor {doctor.nombre} {doctor.apellidos} ha fichado a las {hora.hour}:{hora.minute}")
        elif enfermero != None:
            print(f"El enfermero {enfermero.nombre} {enfermero.apellidos} ha fichado a las {hora.hour}:{hora.minute}")
