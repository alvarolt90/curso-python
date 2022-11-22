#Creación de excepciones

class TemperatureException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje

class TooHotTemperature(TemperatureException):
    def __init__(self, mensaje):
        self.message = mensaje

class TooColdTemperature(TemperatureException):
    def __init__(self, mensaje):
        self.message = mensaje