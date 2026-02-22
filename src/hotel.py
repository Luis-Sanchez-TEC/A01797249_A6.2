"""Módulo para la gestión de hoteles y persistencia en JSON."""
import json
import os


class Hotel:
    """Clase para gestionar la información de los hoteles."""

    def __init__(self, storage_file):
        """Inicializa el hotel con un archivo de persistencia."""
        self.storage_file = storage_file
        self.hotels = self._load_data()

    def _load_data(self):
        """Carga datos desde el archivo JSON con manejo de errores."""
        if not os.path.exists(self.storage_file):
            return {}
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error cargando archivo: {error}")
            return {}

    def _save_data(self):
        """Guarda los datos actuales en el archivo JSON."""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as file:
                json.dump(self.hotels, file, indent=4)
        except IOError as error:
            print(f"Error guardando datos: {error}")

    def create_hotel(self, hotel_id, name):
        """Crea un nuevo hotel."""
        if hotel_id in self.hotels:
            return False
        self.hotels[hotel_id] = {"name": name, "rooms": {}}
        self._save_data()
        return True

    def delete_hotel(self, hotel_id):
        """Elimina un hotel existente."""
        if hotel_id in self.hotels:
            del self.hotels[hotel_id]
            self._save_data()
            return True
        return False

    def display_hotel(self, hotel_id):
        """Muestra la información de un hotel."""
        hotel = self.hotels.get(hotel_id)
        if hotel:
            print(f"ID: {hotel_id}, Nombre: {hotel['name']}")
            return hotel
        return None

    def modify_hotel(self, hotel_id, new_name):
        """Modifica el nombre de un hotel."""
        if hotel_id in self.hotels:
            self.hotels[hotel_id]["name"] = new_name
            self._save_data()
            return True
        return False
