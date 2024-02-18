class Asiento():
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor (self, color):
        coloresValidos = ["rojo","verde","amarillo","negro","blanco"]
        if (color in coloresValidos):
            self.color = color