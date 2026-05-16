from src.models.machines.clown_machine import ClownMachine
from src.models.machines.exchange_machine import ExchangeMachine

print("Sistema de Gestión de una Sala de Juegos y Videojuegos estilo Arcade\n")

clown_machine = ClownMachine("Payasos Locos", "Tirar los payasos con las pelotas", True)

print(clown_machine.play(1, 2, 3, 5))

exchange_machine = ExchangeMachine(initial_coins_deposit=1000, maximun_coin_limit=2000)

print("=== ESTADO INICIAL DE LA MÁQUINA ===")
print(f"Total dinero en cajas: {exchange_machine.get_total_money_in_machine()}€")
print(f"Monedas de 1€ disponibles: {exchange_machine.coin_box}")
print("====================================\n")

print("--- ESCENARIO 1: Introduciendo billetes ---")
resultado = exchange_machine.insert_money(20.0)
print(resultado)
print(f"Total en máquina actual: {exchange_machine.get_total_money_in_machine()}€\n")

print("--- ESCENARIO 2: Introduciendo céntimos (Bucle de espera) ---")
print(exchange_machine.insert_money(0.50))
print(exchange_machine.insert_money(0.20))
print(f"-> Total real en máquina (Sigue igual): {exchange_machine.get_total_money_in_machine()}€\n")

print("--- ESCENARIO 3: Usuario pulsa botón Retirar/Cancelar ---")
print(exchange_machine.cancel_and_return_coins())
print(f"Flotante actual en máquina: {exchange_machine.current_client_cents}€\n")

print("--- ESCENARIO 4: Introduciendo céntimos hasta consolidar 1€ ---")
print(exchange_machine.insert_money(0.50))  
print(exchange_machine.insert_money(0.10)) 
print(exchange_machine.insert_money(0.50))

print(f"\n-> Total real en máquina: {exchange_machine.get_total_money_in_machine()}€")
print(f"-> Monedas de 1€ restantes en tolva: {exchange_machine.coin_box}")
print(f"-> Flotante sobrante en el búfer: {exchange_machine.current_client_cents}€\n")

print("--- ESCENARIO 5: Validación de billetes prohibidos ---")
print(exchange_machine.insert_money(100.0))