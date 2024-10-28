import sys 
sys.path.append("src")

import unittest
from CalculadoraPensional.src.Controller.calculadora_controller import CalculadoraPensionalController
from CalculadoraPensional.src.Model.Exceptions import DatabaseError

class TestCalculadoraPensionalController(unittest.TestCase):
    def setUp(self):
        self.controller = CalculadoraPensionalController()
        
    def tearDown(self):
        self.controller.close_connection()

    def test_create_user_success(self):
        try:
            self.controller.create_user("Alejandro", 25, 3000.00, 100, 15000.00, 1.5, 2.0, "M")
        except Exception as e:
            self.fail(f"Fallo al crear usuario: {str(e)}")

    def test_create_user_error(self):
        with self.assertRaises(DatabaseError):
            self.controller.create_user("Alejandro", 17, 3000.00, 100, 15000.00, 1.5, 2.0, "M")

    def test_read_user_success(self):
        result = self.controller.read_user(1)
        self.assertIsNotNone(result)

    def test_read_user_error(self):
        result = self.controller.read_user(9999)  # ID inexistente
        self.assertIsNone(result)

    def test_update_user_success(self):
        try:
            self.controller.update_user(1, nombre="Carlos", salario_actual=4000.00)
        except Exception as e:
            self.fail(f"Fallo al actualizar usuario: {str(e)}")

    def test_update_user_error(self):
        with self.assertRaises(DatabaseError):
            self.controller.update_user(9999, nombre="Carlos", salario_actual=4000.00)

    def test_delete_user_success(self):
        try:
            self.controller.delete_user(1)
        except Exception as e:
            self.fail(f"Fallo al eliminar usuario: {str(e)}")

    def test_delete_user_error(self):
        with self.assertRaises(DatabaseError):
            self.controller.delete_user(9999)  # ID inexistente

if __name__ == "__main__":
    unittest.main()
