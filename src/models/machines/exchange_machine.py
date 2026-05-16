class ExchangeMachine:

    CASH_ALLOWED = [5.0, 10.0, 20.0, 50.0]
    COINS_ALLOWED = [0.05, 0.10, 0.20, 0.50, 2.0]

    def __init__(self, initial_coins_deposit: int, maximun_coin_limit: int):
        self.coin_box = int(initial_coins_deposit)
        self.client_cash_box = 0
        self.maximun_coin_limit = maximun_coin_limit

        self.current_client_cents = 0.0

    def get_total_money_in_machine(self) -> int:
        return self.coin_box + self.client_cash_box

    def insert_money(self, amount: float):
        
        if amount in self.CASH_ALLOWED:
            billete = int(amount)
            if self.coin_box >= billete:
                self.client_cash_box += billete 
                self.coin_box -= billete
                return f"Billete de {billete}€ aceptado. Entregando {billete} monedas de 1€."
            else:
                return "Sin monedas de 1€ suficientes para cambiar este billete."

        elif amount in self.COINS_ALLOWED:
            if amount == 2.0:
                if self.coin_box >= 2:
                    self.coin_box -= 2
                    self.client_cash_box += 2
                    return "Moneda de 2€ aceptada. Entregando 2 monedas de 1€."
                else:
                    return "Sin cambio para 2€. Moneda devuelta."

            self.current_client_cents = round(self.current_client_cents + amount, 2)
            print(f"Moneda de {amount}€ contada. Acumulado flotante: {self.current_client_cents}€")

            if self.current_client_cents >= 1.0:
                if self.coin_box >= 1:
                    self.coin_box -= 1
                    self.client_cash_box += 1 
                    
                    self.current_client_cents = round(self.current_client_cents - 1.0, 2)
                    
                    return f"¡Se alcanzó 1€! Entregando 1 moneda de 1€. Flotante restante: {self.current_client_cents}€"
                else:
                    return "Error: No quedan monedas de 1€ para el cambio. " + self.cancel_and_return_coins()

            return f"Esperando a sumar 1€ para entregar moneda. Falta: {round(1.0 - self.current_client_cents, 2)}€"

        else:
            return f"El valor {amount}€ no es aceptado."

    def cancel_and_return_coins(self) -> str:
        if self.current_client_cents > 0.0:
            dinero_devuelto = self.current_client_cents
            self.current_client_cents = 0.0
            return f"Operación cancelada. Devolviendo {dinero_devuelto}€ en céntimos al usuario. Las cajas de la máquina no varían."
        return "No hay monedas que retirar."