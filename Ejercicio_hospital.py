import random
import clases

#Creación de objetos

#Dos doctores
doctor1 = clases.Doctor("Andres", "Tovar", "Traumatologia")
doctor2 = clases.Doctor("Maria", "Lopez", "Pediatria")
doctores = [doctor1, doctor2]

#Dos enfermeros
enfermero1 = clases.Enfermero(1, "Jose", "Martinez")
enfermero2 = clases.Enfermero(2, "Guillermo", "Bujalance")
enfermeros = [enfermero1, enfermero2]

#Lista de enfermedades
enfermedades = ["Migraña", "Nauseas", "Fiebre", "Tos", "Mareos", "Vómitos"]

#Pacientes
paciente1 = clases.Pacientes(random.choice(list(enfermedades)), "Juan", "Lopez")
paciente2 = clases.Pacientes(random.choice(list(enfermedades)), "Martin", "Fernandez")
paciente3 = clases.Pacientes(random.choice(list(enfermedades)), "Sandra", "Tovar")
paciente4 = clases.Pacientes(random.choice(list(enfermedades)), "Carmen", "Sanchez")

#Sala de espera con pacientes
sala_espera = [paciente1, paciente2, paciente3, paciente4]

#Atendiendo a los pacientes de la sala de espera (En construcción)
while len(sala_espera) > 0:
    for enfermero in enfermeros:
        enfermero.atiendePaciente(sala_espera)