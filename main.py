from src.modelos.maquinas.maquina_payaso import MaquinaPayaso
from src.modelos.maquinas.maquina_cambio import MaquinaCambio
from src.modelos.usuarios.ususario import UsuarioComun
from src.excepciones.excepciones import ErrorArcade

def main():
    print("=== Sistema de Gestión de una Sala de Juegos y Videojuegos estilo Arcade ===")
    
    payaso = MaquinaPayaso("Payasos Locos", "Derriba payasos con pelotas", True)
    
    try:
        print("\n[JUEGO] Iniciando partida...")
        puntos, mensaje = payaso.jugar(1, golpe_arriba=2, golpe_medio=3, golpe_abajo=5)
        print(mensaje)
    except ErrorArcade as e:
        print(f"Error en el juego: {e}")

    cambio = MaquinaCambio(deposito_inicial=1000, limite_maximo=2000)
    
    print("\n[CAMBIO] Escenario 1: Billete de 20€")
    try:
        print(cambio.ejecutar(20.0))
    except ErrorArcade as e:
        print(f"Error: {e}")

    print("\n[CAMBIO] Escenario 2: Acumulando céntimos")
    print(cambio.ejecutar(0.50))
    print(cambio.ejecutar(0.50))

    print("\n[CAMBIO] Escenario 3: Error con billete no aceptado")
    try:
        print(cambio.ejecutar(100.0))
    except ErrorArcade as e:
        print(f"Captura de excepción: {e}")

    print("=== [PRUEBA]==> INTEGRACIÓN DE USUARIOS ===")

    cliente = UsuarioComun("jhon_arcade", "1234")
    cliente.añadir_fichas(5)
    
    payaso = MaquinaPayaso("Payasos Locos", "Derriba payasos", True)
    
    print(f"\nEstado inicial de {cliente.nombre_usuario}: {cliente.tickets_acumulados} tickets.")
    
    if cliente.usar_ficha():
        print("[JUEGO] Usando 1 ficha... ¡A jugar!")
        puntos, mensaje = payaso.jugar(1, 3, 4, 2)
        print(mensaje)
        
        # El usuario recibe sus tickets
        cliente.añadir_tickets(puntos)
        print(f"Estado final: {cliente.tickets_acumulados} tickets acumulados.")
    else:
        print("No tienes fichas suficientes.")

if __name__ == "__main__":
    main()