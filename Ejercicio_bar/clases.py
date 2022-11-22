import random
import excepciones

#Creación de clases

class TazaCafe:
    def __init__(self, temperature, tipo_cafe):
        self.temperature = temperature
        self.tipo_cafe = tipo_cafe

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomarTazaCafe(TazaCafe):
        try:
            if TazaCafe > 80:
                raise excepciones.TooHotTemperature("El café está ardiendo y el cliente se ha quemado la lengua")
            elif TazaCafe < 20:
                raise excepciones.TooColdTemperature("El cliente protesta porque el café está frio")
        except Exception as e:
            print(f'Exception - Ocurrió un error: {e} , {type(e)}')

class Camarero:
    def __init__(self, nombre):
        self.nombre = nombre

    def servirTazaCafe(self):
        try:
            temperature = random.randint(0, 100)
            tipo_cafe = input("¿Que tipo de café desea tomar?")
            cafe = TazaCafe(temperature, tipo_cafe)
        except Exception as e:
            print(f'Exception - Ocurrió un error: {e} , {type(e)}')

class Bar:
    def __init__(self, camarero, cliente):
        self.camarero = camarero
        self.cliente = cliente