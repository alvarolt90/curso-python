#Creación de excepciones

class AfinacionException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje
