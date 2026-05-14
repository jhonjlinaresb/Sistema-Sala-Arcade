from src.models.machines.clown_machine import ClownMachine

print("Sistema de Gestión de una Sala de Juegos y Videojuegos estilo Arcade")

clown = ClownMachine("Payasos Locos", "Tirar los payasos con las pelotas", True)

print(clown.play(1, 2, 3, 5))