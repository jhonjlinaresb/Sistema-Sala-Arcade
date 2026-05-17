from src.modelos.maquinas.maquina_payaso import MaquinaPayaso
from src.modelos.maquinas.maquina_cambio import MaquinaCambio
from src.modelos.premio import MaquinaPremios

class SistemaArcade:
    
    def __init__(self):
        self.maquina_payaso = MaquinaPayaso("Payasos Locos", "Juego de puntería", True)
        self.cajero_cambio = MaquinaCambio(1000, 2000)
        self.dispensador_premios = MaquinaPremios()
        self.usuarios = {}
        self.usuario_actual = None

    def registrar_usuario(self, nombre, pin):
        from src.modelos.usuarios.usuario import UsuarioComun
        self.usuarios[nombre] = UsuarioComun(nombre, pin)
        return f"Usuario {nombre} registrado."

    def login(self, nombre, pin):
        if nombre in self.usuarios and self.usuarios[nombre].validar_pin(pin):
            self.usuario_actual = self.usuarios[nombre]
            return True
        return False