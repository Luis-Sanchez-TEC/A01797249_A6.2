"""Módulo para la gestión de reservaciones vinculando Hoteles y Clientes."""
import json
import os


class Reservation:
    """Clase para gestionar las reservaciones del sistema."""

    def __init__(self, storage_file):
        """Inicializa la gestión de reservaciones."""
        self.storage_file = storage_file
        self.reservations = self._load_data()

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

    def cancel_reservation(self, res_id):
        """Elimina una reservación del sistema."""
        if res_id in self.reservations:
            del self.reservations[res_id]
            self._save_data()
            return True
        return False
