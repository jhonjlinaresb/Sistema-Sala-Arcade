from abc import ABC, abstractmethod
from src.excepciones.excepciones import ErrorMonedaNoAceptada

class Maquina(ABC):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.VALOR_FICHA = 1 

    def validar_ficha(self, moneda):
        if moneda == self.VALOR_FICHA:
            return True
        raise ErrorMonedaNoAceptada(f"[{self.nombre}] Error: Inserta {self.VALOR_FICHA}€.")

    @abstractmethod
    def ejecutar(self, *args, **kwargs):
        pass