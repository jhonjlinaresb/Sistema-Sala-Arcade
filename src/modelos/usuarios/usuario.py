from abc import ABC

class Usuario(ABC):
    def __init__(self, nombre_usuario, pin):
        self.nombre_usuario = nombre_usuario
        self.__pin = pin 
        self.sesion_activa = False

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}"

class UsuarioComun(Usuario):
    
    def __init__(self, nombre_usuario, pin):
        super().__init__(nombre_usuario, pin)
        self.tickets_acumulados = 0
        self.fichas = 0

    def añadir_tickets(self, cantidad):
        if cantidad > 0:
            self.tickets_acumulados += cantidad

    def usar_ficha(self):
        if self.fichas > 0:
            self.fichas -= 1
            return True
        return False

    def añadir_fichas(self, cantidad):
        self.fichas += cantidad

class UsuarioOperador(Usuario):
    
    def __init__(self, nombre_usuario, pin, codigo_empleado):
        super().__init__(nombre_usuario, pin)
        self.codigo_empleado = codigo_empleado
        self.es_admin = True