from src.excepciones.excepciones import ErrorTicketsInsuficientes

class Premio:

    def __init__(self, nombre, costo_tickets, stock):
        self.nombre = nombre
        self.costo_tickets = costo_tickets
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - Costo: {self.costo_tickets} tickets (Stock: {self.stock})"

class MaquinaPremios:
    def __init__(self):
        self.catalogo = [
            Premio("Peluche de Payaso", 500, 5),
            Premio("Llavero Ilusiona", 100, 20),
            Premio("Consola Retro", 5000, 2)
        ]

    def canjear_premio(self, usuario, indice_premio):
        if indice_premio < 0 or indice_premio >= len(self.catalogo):
            return "Selección de premio no válida."
        
        premio = self.catalogo[indice_premio]
        
        if premio.stock <= 0:
            return f"Lo sentimos, no hay stock de {premio.nombre}."
            
        if usuario.tickets_acumulados < premio.costo_tickets:
            raise ErrorTicketsInsuficientes(
                f"Te faltan {premio.costo_tickets - usuario.tickets_acumulados} tickets para el {premio.nombre}."
            )
            
        usuario.tickets_acumulados -= premio.costo_tickets
        premio.stock -= 1
        return f"¡Felicidades! Has canjeado un {premio.nombre}."