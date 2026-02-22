"""Pruebas unitarias extendidas para alcanzar >85% de cobertura."""
import unittest
import os
from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Casos de prueba para validar la gestión de hoteles."""

    def setUp(self):
        """Configura un entorno de prueba limpio."""
        self.test_file = "data/test_hotels.json"
        self.hotel_manager = Hotel(self.test_file)

    def tearDown(self):
        """Limpia los archivos de prueba creados."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_hotel(self):
        """Prueba la creación de un hotel y el caso de ID duplicado."""
        self.assertTrue(self.hotel_manager.create_hotel("H1", "Grand Hotel"))
        # Esto cubre la línea de ID ya existente
        self.assertFalse(self.hotel_manager.create_hotel("H1", "Duplicate"))

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel y el caso de ID inexistente."""
        self.hotel_manager.create_hotel("H1", "Grand Hotel")
        self.assertTrue(self.hotel_manager.delete_hotel("H1"))
        # Esto cubre el caso donde el hotel no existe
        self.assertFalse(self.hotel_manager.delete_hotel("NONAME"))

    def test_modify_hotel(self):
        """Prueba la modificación y el caso de ID inexistente."""
        self.hotel_manager.create_hotel("H1", "Old Name")
        self.assertTrue(self.hotel_manager.modify_hotel("H1", "New Name"))
        # Caso negativo
        self.assertFalse(self.hotel_manager.modify_hotel("H2", "Error"))

    def test_display_hotel(self):
        """Prueba la visualización de información (cubre display_hotel)."""
        self.hotel_manager.create_hotel("H1", "Show Hotel")
        hotel_data = self.hotel_manager.display_hotel("H1")
        self.assertEqual(hotel_data["name"], "Show Hotel")
        # Caso donde no existe
        self.assertIsNone(self.hotel_manager.display_hotel("H2"))

    def test_load_invalid_json(self):
        """Fuerza un error de lectura para cubrir el bloque except."""
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("invalid json contents")
        new_manager = Hotel(self.test_file)
        self.assertEqual(new_manager.hotels, {})
