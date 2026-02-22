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

    def test_create_and_display(self):
        """Prueba creación y visualización."""
        self.assertTrue(self.manager.create_customer("C1", "Luis", "l@test.com"))
        customer = self.manager.display_customer("C1")
        self.assertEqual(customer["name"], "Luis")

    def test_modify_customer(self):
        """Prueba la modificación de datos del cliente."""
        self.manager.create_customer("C1", "Luis", "l@test.com")
        self.manager.modify_customer("C1", name="Luis Fer")
        self.assertEqual(self.manager.customers["C1"]["name"], "Luis Fer")

    def test_delete_customer(self):
        """Prueba la eliminación de un cliente."""
        self.manager.create_customer("C1", "Luis", "l@test.com")
        self.assertTrue(self.manager.delete_customer("C1"))
        self.assertFalse(self.manager.delete_customer("C1"))
