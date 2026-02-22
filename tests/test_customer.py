"""Pruebas unitarias para la clase Customer."""
import unittest
import os
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """Casos de prueba para validar la gestión de clientes."""

    def setUp(self):
        """Configura un entorno limpio para cada prueba."""
        self.test_file = "data/test_customers.json"
        self.manager = Customer(self.test_file)

    def tearDown(self):
        """Elimina archivos temporales."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_customer(self):
        """Prueba creación y duplicados."""
        self.assertTrue(self.manager.create_customer("C1", "Luis", "l@t.com"))
        self.assertFalse(self.manager.create_customer("C1", "Luis", "l@t.com"))

    def test_delete_customer(self):
        """Prueba eliminación de cliente existente y no existente."""
        self.manager.create_customer("C1", "Luis", "l@t.com")
        # Cubre líneas 43-47
        self.assertTrue(self.manager.delete_customer("C1"))
        self.assertFalse(self.manager.delete_customer("C2"))

    def test_display_customer(self):
        """Prueba visualización de cliente existente y no existente."""
        self.manager.create_customer("C1", "Luis", "l@t.com")
        # Cubre líneas 53-54
        self.assertIsNotNone(self.manager.display_customer("C1"))
        self.assertIsNone(self.manager.display_customer("C2"))

    def test_modify_customer(self):
        """Prueba modificación de cliente existente y no existente."""
        self.manager.create_customer("C1", "Luis", "l@t.com")
        # Cubre líneas 60-64
        self.assertTrue(self.manager.modify_customer("C1", name="Fer"))
        self.assertFalse(self.manager.modify_customer("C2", name="Error"))

    def test_invalid_json(self):
        """Cubre el bloque de error en la carga de datos."""
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("invalid")
        new_manager = Customer(self.test_file)
        self.assertEqual(new_manager.customers, {})