"""Script de prueba de consola para el Sistema de Reservaciones."""
from src.hotel import Hotel
from src.customer import Customer
from src.reservation import Reservation

def main():
    print("=== INICIANDO PRUEBA DE CONSOLA ===")

    # 1. Inicializar sistemas
    h_sys = Hotel("data/hotels.json")
    c_sys = Customer("data/customers.json")
    r_sys = Reservation("data/reservations.json")

    # ---
    # Ver datos precargados desde el JSON ---
    print("\n--- Verificando Persistencia (Carga de Archivo) ---")
    h_sys.display_hotel()
    c_sys.display_customer()
    r_sys.display_reservations()
    print("------------------------------------------")
    # -----------------------------------------------------------

    # 2. Operaciones de Hotel
    print("\n--- Sección Hotel ---")
    h_sys.create_hotel("H1", "Grand Hotel")
    h_sys.display_hotel("H1")

    # 3. Operaciones de Cliente
    print("\n--- Sección Cliente ---")
    c_sys.create_customer("C1", "Luis Fer", "luis@test.com")
    c_sys.display_customer("C1")

    # 4. Operaciones de Reservación
    print("\n--- Sección Reservación ---")
    r_sys.create_reservation("R1", "C1", "H1")
    print(f"Reservaciones actuales: {r_sys.reservations}")

    # 5. Prueba de manejo de errores (Req 5)
    print("\n--- Prueba de Error (Archivo Corrupto) ---")
    _ = Hotel("data/corrupto.json") # Esto debería imprimir un error y continuar

    print("\n=== PRUEBA FINALIZADA ===")

if __name__ == "__main__":
    main()
