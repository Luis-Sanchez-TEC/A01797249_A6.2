"""Pruebas unitarias para la clase Reservation."""
import unittest
import os
from unittest.mock import patch
from src.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Casos de prueba para el sistema de reservaciones."""

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.test_file = "tests/test_reservations.json"
        # Asegurarse de que el archivo no exista al inicio
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.res_mgr = Reservation(self.test_file)

    def tearDown(self):
        """Limpieza después de cada prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_reservation_success(self):
        """Prueba la creación exitosa de una reservación."""
        result = self.res_mgr.create_reservation("R1", "C1", "H1")
        self.assertTrue(result)
        self.assertIn("R1", self.res_mgr.reservations)

    def test_create_reservation_duplicate(self):
        """Prueba que no se permitan reservaciones duplicadas."""
        self.res_mgr.create_reservation("R1", "C1", "H1")
        result = self.res_mgr.create_reservation("R1", "C2", "H2")
        self.assertFalse(result)

    def test_cancel_reservation_success(self):
        """Prueba la cancelación exitosa de una reservación."""
        self.res_mgr.create_reservation("R1", "C1", "H1")
        result = self.res_mgr.cancel_reservation("R1")
        self.assertTrue(result)
        self.assertNotIn("R1", self.res_mgr.reservations)

    def test_cancel_reservation_fail(self):
        """Prueba la cancelación de una reservación inexistente."""
        result = self.res_mgr.cancel_reservation("NONEXISTENT")
        self.assertFalse(result)

    def test_display_reservations_scenarios(self):
        """Prueba todos los caminos de display_reservations para cobertura."""
        # 1. Caso: Sin reservaciones
        self.res_mgr.reservations = {}
        self.res_mgr.display_reservations()

        # 2. Caso: Una específica con datos de apoyo
        self.res_mgr.create_reservation("R1", "C1", "H1")
        h_data = {"H1": {"name": "Grand Hotel"}}
        c_data = {"C1": {"name": "Luis Fer"}}
        self.res_mgr.display_reservations("R1", h_data, c_data)

        # 3. Caso: Todas las reservaciones sin datos de apoyo
        self.res_mgr.display_reservations()

        # 4. Caso: ID que no existe
        self.res_mgr.display_reservations("R_FALSE")

    # --- PRUEBAS PARA COBERTURA DE ERRORES (MOCKS) ---
    def test_load_data_error(self):
        """Cubre el except en _load_data cuando falla la apertura."""
        with patch("os.path.exists", return_value=True):
            with patch("builtins.open", side_effect=IOError("Error de disco")):
                res_error = Reservation("ruta_ficticia.json")
                self.assertEqual(res_error.reservations, {})

    def test_save_data_error(self):
        """Cubre el except en _save_data forzando un error de escritura."""
        with patch("builtins.open", side_effect=IOError):
            # create_hotel llama a _save_data internamente
            result = self.res_mgr.create_reservation("R_ERR", "C1", "H1")
            self.assertTrue(result)

    def test_load_data_invalid_json(self):
        """Cubre el error de JSON corrupto."""
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("este no es un json")

        # Debe atrapar JSONDecodeError y devolver {}
        res_corrupt = Reservation(self.test_file)
        self.assertEqual(res_corrupt.reservations, {})


if __name__ == "__main__":
    unittest.main()
