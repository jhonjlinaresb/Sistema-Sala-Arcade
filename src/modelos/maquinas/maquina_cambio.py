from src.modelos.maquinas.maquina import Maquina
from src.excepciones.excepciones import ErrorMonedaNoAceptada, ErrorSinCambio

class MaquinaCambio(Maquina):
    BILLETES_PERMITIDOS = [5.0, 10.0, 20.0, 50.0]
    MONEDAS_PERMITIDAS = [0.05, 0.10, 0.20, 0.50, 2.0]

    def __init__(self, deposito_inicial: int, limite_maximo: int):
        super().__init__("Cajero de Cambio", "Cambia dinero por fichas de 1€")
        self.caja_monedas = int(deposito_inicial)
        self.caja_cliente = 0
        self.centimos_acumulados = 0.0

    def ejecutar(self, cantidad: float):
        
        if cantidad in self.BILLETES_PERMITIDOS:
            if self.caja_monedas >= cantidad:
                self.caja_cliente += cantidad 
                self.caja_monedas -= cantidad
                return f"Aceptado: {int(cantidad)} fichas de 1€ entregadas."
            raise ErrorSinCambio("No hay suficientes fichas de 1€.")

        elif cantidad in self.MONEDAS_PERMITIDAS:
            self.centimos_acumulados = round(self.centimos_acumulados + cantidad, 2)
            if self.centimos_acumulados >= 1.0:
                self.caja_monedas -= 1
                self.caja_cliente += 1
                self.centimos_acumulados -= 1.0
                return "¡1€ alcanzado! Ficha entregada."
            return f"Acumulado: {self.centimos_acumulados}€"
        
        raise ErrorMonedaNoAceptada(f"El valor {cantidad}€ no es válido.")