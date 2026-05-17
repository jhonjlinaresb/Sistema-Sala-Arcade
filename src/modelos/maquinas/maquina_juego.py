from src.modelos.maquinas.maquina import Maquina

class MaquinaJuego(Maquina):
    
    def __init__(self, nombre, descripcion, entrega_tickets: bool):
        super().__init__(nombre, descripcion)
        self.entrega_tickets = entrega_tickets
        self.tickets_acumulados_maquina = 0

    def jugar(self, moneda, *args, **kwargs):
        self.validar_ficha(moneda)
        return self.ejecutar(*args, **kwargs)