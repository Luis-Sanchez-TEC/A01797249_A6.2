from src.hotel import Hotel
from src.customer import Customer

def test_drive():
    print("--- Probando Sistema de Reservaciones ---")
    hotel_sys = Hotel("data/hotels.json")
    cust_sys = Customer("data/customers.json")

    # Mostrar información existente (Req 2.c)
    print("\nHoteles cargados:")
    hotel_sys.display_hotel("H101")

    # Probar manejo de datos inválidos (Req 5)
    print("\nProbando carga de archivo inexistente (debe continuar):")
    _ = Hotel("data/ghost.json")

    print("\n--- Prueba de consola finalizada con éxito ---")

if __name__ == "__main__":
    test_drive()
