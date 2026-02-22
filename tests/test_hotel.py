"""Pruebas unitarias para la clase Hotel."""
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
        """Prueba la creación de un hotel."""
        self.assertTrue(self.hotel_manager.create_hotel("H1", "Grand Hotel"))

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel."""
        self.hotel_manager.create_hotel("H1", "Grand Hotel")
        self.assertTrue(self.hotel_manager.delete_hotel("H1"))

    def test_modify_hotel(self):
        """Prueba la modificación de un hotel."""
        self.hotel_manager.create_hotel("H1", "Old Name")
        self.assertTrue(self.hotel_manager.modify_hotel("H1", "New Name"))
        self.assertEqual(self.hotel_manager.hotels["H1"]["name"], "New Name")
