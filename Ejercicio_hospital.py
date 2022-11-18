import random

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
        if doctor != None:
            print(f"El doctor {doctor.nombre} {doctor.apellidos} ha fichado")
        elif enfermero != None:
            print(f"El enfermero {enfermero.nombre} {enfermero.apellidos}ha fichado")


#Creación de objetos

#Dos doctores
doctor1 = Doctor("Andres", "Tovar", "Traumatologia")
doctor2 = Doctor("Maria", "Lopez", "Pediatria")
doctores = [doctor1, doctor2]

#Dos enfermeros
enfermero1 = Enfermero(1, "Jose", "Martinez")
enfermero2 = Enfermero(2, "Guillermo", "Bujalance")
enfermeros = [enfermero1, enfermero2]

#Lista de enfermedades
enfermedades = ["Migraña", "Nauseas", "Fiebre", "Tos", "Mareos", "Vómitos"]

#Pacientes
paciente1 = Pacientes(random.choice(list(enfermedades)), "Juan", "Lopez")
paciente2 = Pacientes(random.choice(list(enfermedades)), "Martin", "Fernandez")
paciente3 = Pacientes(random.choice(list(enfermedades)), "Sandra", "Tovar")
paciente4 = Pacientes(random.choice(list(enfermedades)), "Carmen", "Sanchez")

#Sala de espera con pacientes
sala_espera = [paciente1, paciente2, paciente3, paciente4]

#Atendiendo a los pacientes de la sala de espera (En construcción)
while len(sala_espera) > 0:
    for enfermero in enfermeros:
        enfermero.atiendePaciente(sala_espera)