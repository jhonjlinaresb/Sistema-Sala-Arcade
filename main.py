from src.modelos.maquinas.maquina_payaso import MaquinaPayaso
from src.modelos.maquinas.maquina_cambio import MaquinaCambio
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

if __name__ == "__main__":
    main()