"""Módulo para la gestión de clientes y persistencia en JSON."""
import json
import os


class Customer:
    """Clase para gestionar la información de los clientes."""

    def __init__(self, storage_file):
        """Inicializa el cliente con un archivo de persistencia."""
        self.storage_file = storage_file
        self.customers = self._load_data()

    def _load_data(self):
        """Carga datos desde el archivo JSON con manejo de errores."""
        if not os.path.exists(self.storage_file):
            return {}
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error cargando archivo de clientes: {error}")
            return {}

    def _save_data(self):
        """Guarda los datos actuales en el archivo JSON."""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as file:
                json.dump(self.customers, file, indent=4)
        except IOError as error:
            print(f"Error guardando datos de clientes: {error}")

    def create_customer(self, customer_id, name, email):
        """Crea un nuevo cliente."""
        if customer_id in self.customers:
            return False
        self.customers[customer_id] = {"name": name, "email": email}
        self._save_data()
        return True

    def delete_customer(self, customer_id):
        """Elimina un cliente existente."""
        if customer_id in self.customers:
            del self.customers[customer_id]
            self._save_data()
            return True
        return False

    def display_customer(self, customer_id):
        """Muestra la información de un cliente."""
        customer = self.customers.get(customer_id)
        if customer:
            print(f"ID: {customer_id}, Nombre: {customer['name']}")
            return customer
        return None

    def modify_customer(self, customer_id, **kwargs):
        """Modifica la información de un cliente (nombre o email)."""
        if customer_id in self.customers:
            for key, value in kwargs.items():
                if key in self.customers[customer_id]:
                    self.customers[customer_id][key] = value
            self._save_data()
            return True
        return False
