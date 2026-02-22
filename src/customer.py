"""Módulo para la gestión de clientes y persistencia en JSON."""
import json
import os


class Customer:
    """Clase para gestionar la información de los clientes."""

    def __init__(self, storage_file):
        """Inicializa el cliente con un archivo de persistencia."""
        self.storage_file = storage_file
        self.customers = self._load_data()

    # pylint: disable=duplicate-code
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

    def display_customer(self, customer_id=None):
        """Muestra la información de un cliente específico o de todos."""
        if customer_id:
            customer = self.customers.get(customer_id)
            if customer:
                print(f"ID: {customer_id} | Nombre: {customer['name']} | "
                      f"Email: {customer['email']}")
                return customer
            print(f"Cliente con ID {customer_id} no encontrado.")
            return None

        # Si no hay ID, muestra todos
        if not self.customers:
            print("AVISO: No hay clientes registrados.")
        else:
            print("--- Lista de Clientes Registrados ---")
            for c_id, info in self.customers.items():
                print(f"ID: {c_id} | Nombre: {info['name']} "
                      f"| Email: {info['email']}")
        return self.customers

    # Ejemplo para Hotel (y hazlo igual para Customer)
    def modify_customer(self, customer_id, name=None, email=None):
        """Modifica el nombre o email de un cliente."""
        if customer_id in self.customers:
            if name is not None:
                self.customers[customer_id]['name'] = name
            if email is not None:
                self.customers[customer_id]['email'] = email
            self._save_data()
            return True
        return False
