import sys 
sys.path.append("src")
import unittest
from Controller.calculadora_controller import CrearTabla, ObtenerCursor, BorrarFilas,create_user,brows_user, UsuarioCreadoError,UsuarioBuscadoError, UsuarioActualizadoError, update_user
from Model.Exceptions import DatabaseError
from Model.Parameters import ParametrosPension


class TestCalculadoraPensionalController(unittest.TestCase):
    def setUp(self):
        """ Se ejecuta siempre antes de cada metodo de prueba """
        print("Invocando setUp")
        BorrarFilas() # Asegura que antes de cada metodo de prueba, se borren todos los datos de la tabla

    def setUpClass():
        """ Se ejecuta al inicio de todas las pruebas """
        print("Invocando setUpClass")
        CrearTabla()  # Asegura que al inicio de las pruebas, la tabla este creada

    def tearDown(self):
        """ Se ejecuta al final de cada test """
        print("Invocnado tearDown")

    def tearDownClass():
        """ Se ejecuta al final de todos los tests """
        print("Invocando tearDownClass")
    
    def test_insert1(self):
        Usuario = ParametrosPension()
        Usuario.name = "Juan"
        Usuario.age = 65 
        Usuario.gender = "m"
        Usuario.current_salary = 2300000
        Usuario.weeks_worked = 1200
        Usuario.current_pension_savings = 30000000
        Usuario.average_return = 2
        Usuario.management_rate = 1
        id = 1
        create_user(Usuario)
        usuario_buscado = brows_user(1)

        self.assertEqual(str(Usuario.name), usuario_buscado.name)
        self.assertEqual(str(Usuario.age), usuario_buscado.age)
        self.assertEqual(str(Usuario.gender), usuario_buscado.gender)
        self.assertEqual(str(Usuario.current_salary), usuario_buscado.current_salary)
        self.assertEqual(str(Usuario.weeks_worked), usuario_buscado.weeks_worked)
        self.assertEqual(str(Usuario.current_pension_sabings), usuario_buscado.current_pension_sabings)
        self.assertEqual(str(Usuario.average_return), usuario_buscado.average_return)
        self.assertEqual(str(Usuario.management_rate), usuario_buscado.management)


    def test_insertError(self):

        Usuario = ParametrosPension()
        Usuario.name = "Juan"
        Usuario.age = 65 
        Usuario.gender = "m"
        Usuario.current_salary = 2300000
        Usuario.weeks_worked = 1200
        Usuario.current_pension_savings = 30000000
        Usuario.average_return = 2
        Usuario.management_rate = 1
        create_user(Usuario)

        Usuario_error = ParametrosPension()
        Usuario_error.name = "Juan"
        Usuario_error.age = 65 
        Usuario_error.gender = "m"
        Usuario_error.current_salary = 2300000
        Usuario_error.weeks_worked = 1200
        Usuario_error.current_pension_savings = 30000000
        Usuario_error.average_return = 15
        Usuario_error.management_rate = 1
        with self.assertRaises(UsuarioCreadoError):
            create_user(Usuario_error)

    def test_buscar(self):

        Usuario = ParametrosPension()
        Usuario.name = "Juan"
        Usuario.age = 65 
        Usuario.gender = "m"
        Usuario.current_salary = 2300000
        Usuario.weeks_worked = 1200
        Usuario.current_pension_savings = 30000000
        Usuario.average_return = 2
        Usuario.management_rate = 1
        id = 1
        create_user(Usuario)
        usuario_buscado = brows_user(1)

        self.assertEqual(str(Usuario.name), usuario_buscado.name)
        self.assertEqual(str(Usuario.age), usuario_buscado.age)
        self.assertEqual(str(Usuario.gender), usuario_buscado.gender)
        self.assertEqual(str(Usuario.current_salary), usuario_buscado.current_salary)
        self.assertEqual(str(Usuario.weeks_worked), usuario_buscado.weeks_worked)
        self.assertEqual(str(Usuario.current_pension_sabings), usuario_buscado.current_pension_sabings)
        self.assertEqual(str(Usuario.average_return), usuario_buscado.average_return)
        self.assertEqual(str(Usuario.management_rate), usuario_buscado.management)

    def test_buscarError(self):

        Usuario = ParametrosPension()
        Usuario.name = "Juan"
        Usuario.age = 65 
        Usuario.gender = "m"
        Usuario.current_salary = 2300000
        Usuario.weeks_worked = 1200
        Usuario.current_pension_savings = 30000000
        Usuario.average_return = 2
        Usuario.management_rate = 1
        id = 60
        create_user(Usuario)

        with self.assertRaises(UsuarioBuscadoError):
            brows_user(id)


    def actualizarError(self):
        Usuario = ParametrosPension()
        Usuario.name = "Juan"
        Usuario.age = 65 
        Usuario.gender = "m"
        Usuario.current_salary = 2300000
        Usuario.weeks_worked = 1200
        Usuario.current_pension_savings = 30000000
        Usuario.average_return = 2
        Usuario.management_rate = 1
        id = 125
        create_user(Usuario)

        with self.assertRaises(UsuarioActualizadoError):
            update_user(Usuario, id)
            



if __name__ == "__main__":
    unittest.main()
