"""Pruebas unitarias para la clase Reservation."""
import unittest
import os
from src.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Casos de prueba para validar las reservaciones."""

    def setUp(self):
        """Configura el archivo de pruebas."""
        self.test_file = "data/test_reservations.json"
        self.manager = Reservation(self.test_file)

    def tearDown(self):
        """Limpia el entorno después de la prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_and_cancel(self):
        """Verifica el flujo completo de una reservación."""
        # Crear
        self.assertTrue(self.manager.create_reservation("R1", "C1", "H1"))
        # Duplicado
        self.assertFalse(self.manager.create_reservation("R1", "C1", "H1"))
        # Cancelar
        self.assertTrue(self.manager.cancel_reservation("R1"))
        # Cancelar inexistente
        self.assertFalse(self.manager.cancel_reservation("R2"))

    def test_invalid_json_handling(self):
        """Prueba la resiliencia ante archivos corruptos."""
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("!!!")
        new_manager = Reservation(self.test_file)
        self.assertEqual(new_manager.reservations, {})
