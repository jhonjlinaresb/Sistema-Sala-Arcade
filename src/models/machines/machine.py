class Machine:
    def __init__(self, name, game, deliver_tickets: bool):
        self.name = name
        self.game = game
        self.deliver_tickets = deliver_tickets
        self.tickets_acumulados = 0
        self.TOKEN_VALUE = 1

    def validate_token(self, coin):
        # Hardware del monedero: solo acepta 1€ exacto.
        if coin == self.TOKEN_VALUE:
            return True
        return False

    def play(self, coin, *args, **kwargs):
        if not self.validate_token(coin):
            return f"[{self.name}] Error: Inserta 1€."
        return None