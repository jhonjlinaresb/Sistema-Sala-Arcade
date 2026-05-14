from src.models.machines.machine import Machine

class ClownMachine(Machine):
    def __init__(self, name, game, deliver_tickets: bool):
        super().__init__(name, game, deliver_tickets)
        
        self.points_map = {"top": 10, "middle": 3, "bottom": 1}

    def play(self, coin, top_down, mid_down, bot_down):
        
        error = super().play(coin)
        if error:
            return error
        
        score = (top_down * self.points_map["top"]) + \
                (mid_down * self.points_map["middle"]) + \
                (bot_down * self.points_map["bottom"])
        
        if self.deliver_tickets:
            self.tickets_acumulados += score
            return f"¡Ganaste {score} tickets! Tickets acumulados: {self.tickets_acumulados}" #Acumular tickets a usuario
        
        return f"Puntuación: {score}. Juego terminado."