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
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error cargando archivo: {e}") [cite: 348]
            return {}

    def create_hotel(self, hotel_id, name):
        """Crea un nuevo hotel y lo guarda."""
        if hotel_id in self.hotels:
            print("El ID del hotel ya existe.")
            return False
        self.hotels[hotel_id] = {"name": name, "rooms": {}}
        self._save_data()
        return True

    def _save_data(self):
        """Guarda los datos actuales en el archivo JSON."""
        with open(self.storage_file, 'w', encoding='utf-8') as file:
            json.dump(self.hotels, file, indent=4)