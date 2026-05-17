from src.modelos.sistema_arcade import SistemaArcade
from src.excepciones.excepciones import ErrorArcade

def main():
    print("=== Sistema de Gestión de una Sala de Juegos y Videojuegos estilo Arcade ===")
    
    sistema = SistemaArcade()
    
    sistema.registrar_usuario("jhon", "1234")
    if sistema.login("jhon", "1234"):
        user = sistema.usuario_actual
        print(f"Bienvenido {user.nombre_usuario}!")
        
        user.añadir_tickets(600)
        print(f"Tienes {user.tickets_acumulados} tickets.")
        
        print("\n--- Catálogo de Premios ---")
        for i, p in enumerate(sistema.dispensador_premios.catalogo):
            print(f"{i}. {p}")
            
        try:
            resultado = sistema.dispensador_premios.canjear_premio(user, 0)
            print(f"\nResultado: {resultado}")
            print(f"Tickets restantes: {user.tickets_acumulados}")
        except ErrorArcade as e:
            print(f"\nError en canje: {e}")

if __name__ == "__main__":
    main()