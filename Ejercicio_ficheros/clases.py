#Creación de clases
class Colegio():
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno():
    def __init__(self, nombre, apellidos, dni):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

class Asignatura(Colegio):
    def __init__(self, nombre):
        Colegio.__init__(self, nombre)

#Clase para manejar el archivo
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.nombre = open(self.nombre, 'r', encoding='utf-8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        if self.nombre:
            self.nombre.close()

