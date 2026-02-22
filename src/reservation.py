"""Módulo para la gestión de reservaciones vinculando Hoteles y Clientes."""
import json
import os


class Reservation:
    """Clase para gestionar las reservaciones del sistema."""

    def __init__(self, storage_file):
        """Inicializa la gestión de reservaciones."""
        self.storage_file = storage_file
        self.reservations = self._load_data()

    # pylint: disable=duplicate-code
    def _load_data(self):
        """Carga datos con manejo de errores de archivo."""
        if not os.path.exists(self.storage_file):
            return {}
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error cargando reservaciones: {error}")
            return {}

    def _save_data(self):
        """Guarda la base de datos de reservaciones."""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as file:
                json.dump(self.reservations, file, indent=4)
        except IOError as error:
            print(f"Error guardando reservaciones: {error}")

    def create_reservation(self, res_id, customer_id, hotel_id):
        """Crea una reservación vinculando cliente y hotel."""
        if res_id in self.reservations:
            return False
        self.reservations[res_id] = {
            "customer_id": customer_id,
            "hotel_id": hotel_id
        }
        self._save_data()
        return True

    def display_reservations(self, reservation_id=None,
                             hotels_data=None, customers_data=None):
        """Muestra las reservaciones de forma segura."""
        # 1. Decidir qué mostrar
        if (isinstance(reservation_id, str)
                and reservation_id in self.reservations):
            items_to_show = {reservation_id: self.reservations[reservation_id]}
        else:
            items_to_show = self.reservations

        if not items_to_show:
            print("AVISO: No hay reservaciones para mostrar.")
            return self.reservations

        print("--- Detalle de Reservaciones ---")
        for res_id, info in items_to_show.items():
            h_id = info.get('hotel_id', 'N/A')
            c_id = info.get('customer_id', 'N/A')

            # Obtener nombres si el diccionario existe, si no, usar el ID
            h_name = (hotels_data.get(h_id, {}).get('name', h_id)
                      if isinstance(hotels_data, dict) else h_id)

            c_name = (customers_data.get(c_id, {}).get('name', c_id)
                      if isinstance(customers_data, dict) else c_id)

            print(f"Reserva: {res_id} | Cliente: {c_name} | Hotel: {h_name}")

        return self.reservations

    def cancel_reservation(self, res_id):
        """Elimina una reservación del sistema."""
        if res_id in self.reservations:
            del self.reservations[res_id]
            self._save_data()
            return True
        return False
