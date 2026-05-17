from src.modelos.maquinas.maquina_juego import MaquinaJuego

class MaquinaPayaso(MaquinaJuego):
    def __init__(self, nombre, descripcion, entrega_tickets: bool):
        super().__init__(nombre, descripcion, entrega_tickets)
        # Remaster: points_map -> mapa_puntos
        self.mapa_puntos = {"arriba": 10, "medio": 3, "abajo": 1}

    def ejecutar(self, golpe_arriba, golpe_medio, golpe_abajo):
        """
        Lógica polimórfica: Implementa el juego específico de los payasos.
        """
        puntuacion = (golpe_arriba * self.mapa_puntos["arriba"]) + \
                     (golpe_medio * self.mapa_puntos["medio"]) + \
                     (golpe_abajo * self.mapa_puntos["abajo"])
        
        resultado = f"[{self.nombre}] Puntuación: {puntuacion}."
        if self.entrega_tickets:
            self.tickets_acumulados_maquina += puntuacion
            resultado += f" ¡Ganaste {puntuacion} tickets!"
            
        return puntuacion, resultado