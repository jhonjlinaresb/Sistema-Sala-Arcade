class ErrorArcade(Exception):
    pass

class ErrorMaquina(ErrorArcade): 
    pass

class ErrorMonedaNoAceptada(ErrorMaquina):
    pass

class ErrorSinCambio(ErrorMaquina):
    pass