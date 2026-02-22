"""Pruebas unitarias para la clase Customer."""
import unittest
import os
from unittest.mock import patch
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """Casos de prueba para Customer."""

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.test_file = "tests/test_customers.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.customer_manager = Customer(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_lifecycle_success(self):
        """Ciclo de vida del cliente."""
        self.customer_manager.create_customer("C1", "Luis", "l@t.com")
        self.assertTrue(self.customer_manager.modify_customer("C1", "Luis S"))
        self.customer_manager.display_customer("C1")
        self.customer_manager.display_customer()
        self.assertTrue(self.customer_manager.delete_customer("C1"))

    def test_failures_coverage(self):
        self.assertFalse(self.customer_manager.delete_customer("VOID"))
        self.customer_manager.display_customer("VOID")
        self.assertFalse(
            self.customer_manager.modify_customer("VOID", "Nombre")
        )

    def test_error_handling_coverage(self):
        """Configuración inicial para cada prueba."""
        with patch("builtins.open", side_effect=IOError):
            # pylint: disable=protected-access
            self.customer_manager._save_data()

        with patch("os.path.exists", return_value=True), \
             patch("builtins.open", side_effect=IOError):
            c_err = Customer("error.json")
            self.assertEqual(c_err.customers, {})

    def test_invalid_json(self):
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("invalid")
        c_corrupt = Customer(self.test_file)
        self.assertEqual(c_corrupt.customers, {})


if __name__ == "__main__":
    unittest.main()
