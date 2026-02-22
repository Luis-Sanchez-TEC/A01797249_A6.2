"""Pruebas unitarias para la clase Hotel."""
import unittest
import os
from unittest.mock import patch
from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Casos de prueba para Hotel."""

    def setUp(self):
        self.test_file = "tests/test_hotels.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.hotel_manager = Hotel(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_lifecycle_success(self):
        """Cubre flujos exitosos."""
        self.hotel_manager.create_hotel("H1", "Plaza")
        self.assertTrue(self.hotel_manager.modify_hotel("H1", "Plaza Mod"))
        self.hotel_manager.display_hotel("H1")
        self.hotel_manager.display_hotel()
        self.assertTrue(self.hotel_manager.delete_hotel("H1"))

    def test_failures_coverage(self):
        """ID no encontrado."""
        # NO vaciamos el dic, solo pedimos algo que no existe
        self.assertFalse(self.hotel_manager.delete_hotel("ID_FALSO"))
        self.hotel_manager.display_hotel("ID_FALSO")
        self.assertFalse(self.hotel_manager.modify_hotel("ID_FALSO", "Nombre"))

    def test_error_handling_coverage(self):
        """Manejo de errores."""
        with patch("builtins.open", side_effect=IOError):
            # pylint: disable=protected-access
            self.hotel_manager._save_data()

        with patch("os.path.exists", return_value=True), \
             patch("builtins.open", side_effect=IOError):
            h_err = Hotel("error.json")
            self.assertEqual(h_err.hotels, {})

    def test_invalid_json(self):
        """Archivo corrupto."""
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("invalid")
        h_corrupt = Hotel(self.test_file)
        self.assertEqual(h_corrupt.hotels, {})


if __name__ == "__main__":
    unittest.main()
