import unittest
import sys
import os

sys.path.append(r"C:\Users\USER\PycharmProjects\CalculadoraPensional\src")
#sys.path.append("src")

from Logic import Parameters
from Logic import CalculatorLogic
from Logic import Exceptions


class PensionTest(unittest.TestCase):
    """ Casos normales: Estas pruebas evalúan escenarios realistas donde
    los parámetros están dentro de los rangos válidos.
    """

    def test_Normal_Case1(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 65
        parameters.gender = "m"
        marital_status = "s"
        parameters.current_salary = 2300000
        parameters.weeks_worked = 1200
        parameters.current_pension_savings = 30000000
        parameters.average_return = 2
        parameters.management_rate = 1

        total_savings = 3637.656861250826
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Normal_Case2(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 30
        parameters.gender = "F"
        estado_civil = "s"
        parameters.current_salary = 1800000
        parameters.weeks_worked = 1520
        parameters.current_pension_savings = 25000000
        parameters.average_return = 2
        parameters.management_rate = 1

        total_savings = 3.141746163814644e+20
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Normal_Case3(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 40
        parameters.gender = "m"
        estado_civil = "c"
        parameters.current_salary = 3500000
        parameters.weeks_worked = 1040
        parameters.current_pension_savings = 85000000
        parameters.average_return = 2
        parameters.management_rate = 1

        total_savings = 1.35381937545e+16
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Normal_Case4(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 45
        parameters.gender = "m"
        estado_civil = "c"
        parameters.current_salary = 2500000
        parameters.weeks_worked = 1300
        parameters.current_pension_savings = 120000000
        parameters.average_return = 1
        parameters.management_rate = 1

        total_savings = 552960000000.0
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Normal_Case5(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 50
        parameters.gender = "m"
        estado_civil = "c"
        parameters.current_salary = 4200000
        parameters.weeks_worked = 1560
        parameters.current_pension_savings = 200000000
        parameters.average_return = 1
        parameters.management_rate = 2

        total_savings = 27481600000.0
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Normal_Case6(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 25
        parameters.gender = "m"
        estado_civil = "s"
        parameters.current_salary = 1200000
        parameters.weeks_worked = 1260
        parameters.current_pension_savings = 10000000
        parameters.average_return = 2
        parameters.management_rate = 2

        total_savings = 4.224886030582197e+22
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    """ Casos extraordinarios: Evaluamos casos fuera de los escenarios comunes
    pero todavía posibles.    """

    def test_Extraordinary1(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 35
        parameters.gender = "m"
        estado_civil = "s"
        parameters.current_salary = 2000000
        parameters.weeks_worked = 300
        parameters.current_pension_savings = 25000000
        parameters.average_return = 1
        parameters.management_rate = 2

        ahorro_total = 197132288000000.0
        resultado = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(resultado, ahorro_total)

    def test_Extraordinary2(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 36
        parameters.gender = "f"
        estado_civil = "c"
        parameters.current_salary = 500000
        parameters.weeks_worked = 220
        parameters.current_pension_savings = 15000000
        parameters.average_return = 2
        parameters.management_rate = 1

        total_savings = 1.935165342555e+17
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Extraordinary3(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 77
        parameters.gender = "m"
        estado_civil = "s"
        parameters.current_salary = 200000
        parameters.weeks_worked = 700
        parameters.current_pension_savings = 30000000
        parameters.average_return = 2
        parameters.management_rate = 2

        total_savings = 0.008221519706938333
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Extraordinary4(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 40
        parameters.gender = "f"
        estado_civil = "s"
        parameters.current_salary = 1300000
        parameters.weeks_worked = 1301
        parameters.current_salary = 15600000
        parameters.average_return = 3
        parameters.management_rate = 2

        total_savings = 3.62924736512e+17
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Extraordinary5(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 76
        parameters.gender = "m"
        estado_civil = "c"
        parameters.current_salary = 80000000
        parameters.weeks_worked = 1300
        parameters.current_pension_savings = 12078720000
        parameters.average_return = 3
        parameters.management_rate = 2

        total_savings = 0.042559695430099964
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    def test_Extraordinary6(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 62
        parameters.gender = "f"
        estado_civil = "s"
        parameters.current_salary = 1300000
        parameters.weeks_worked = 1300
        parameters.current_pension_savings = 117843200
        parameters.average_return = 2
        parameters.management_rate = 1

        total_savings = 476035.1165980796
        result = CalculatorLogic.calculate_expected_pension_savings(parameters)
        self.assertEqual(result, total_savings)

    """ Casos de error: Validamos que el sistema arroje las excepciones
    correctas cuando se ingresan valores inválidos.   """

    def test_very_high_age_error(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 130  # Error
        estado_civil = "s"
        parameters.gender = "m"
        parameters.current_salary = 2500000
        parameters.weeks_worked = 1200
        parameters.current_pension_savings = 50000000
        parameters.average_return = 3
        parameters.management_rate = 1

        self.assertRaises(Exceptions.EdadError, CalculatorLogic.calculate_expected_pension_savings,
                          parameters)

    def test_very_low_age_error(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 12  # Error
        parameters.gender = "M"
        estado_civil = "s"
        parameters.current_salary = 1200000
        parameters.weeks_worked = 50
        parameters.current_pension_savings = 2000000
        parameters.average_return = 3
        parameters.management_rate = 1

        self.assertRaises(Exceptions.EdadError, CalculatorLogic.calculate_expected_pension_savings, parameters)

    def test_negative_salary_error(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 35
        parameters.gender = "F"
        estado_civil = "s"
        parameters.current_salary = -3000000  # Error
        parameters.weeks_worked = 800
        parameters.current_pension_savings = 40000000
        parameters.average_return = 3
        parameters.management_rate = 1

        self.assertRaises(Exceptions.SalarioActualNegativoError, CalculatorLogic.calculate_expected_pension_savings,
                          parameters)

    def test_negative_weeks_worked_error(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 40
        parameters.gender = "m"
        estado_civil = "s"
        parameters.current_salary = 3500000
        parameters.weeks_worked = -100  # Error
        parameters.current_pension_savings = 60000000
        parameters.average_return = 4
        parameters.management_rate = 1

        self.assertRaises(Exceptions.SemanasLaboradasNegativasError, CalculatorLogic.calculate_expected_pension_savings,
                          parameters)

    def test_negative_pension_savings_error(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 50
        parameters.gender = "f"
        estado_civil = "s"
        parameters.current_salary = 4000000
        parameters.weeks_worked = 1200
        parameters.current_pension_savings = -10000000  # Error
        parameters.average_return = 3
        parameters.management_rate = 1

        self.assertRaises(Exceptions.AhorroPensionalNegativoError, CalculatorLogic.calculate_expected_pension_savings,
                          parameters)

    def test_excessive_administration_rate_error(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 45
        parameters.gender = "f"
        estado_civil = "s"
        parameters.current_salary = 3800000
        parameters.weeks_worked = 1000
        parameters.current_pension_savings = 70000000
        parameters.average_return = 3
        parameters.management_rate = 4  # Error (excede el 3%)

        self.assertRaises(Exceptions.TasaAdministracionError, CalculatorLogic.calculate_expected_pension_savings,
                          parameters)

    def test_negative_average_profitability_error(self):
        parameters = Parameters.ParametrosPension()
        # Entradas
        parameters.age = 55
        parameters.gender = "m"
        estado_civil = "s"
        parameters.current_salary = 5000000
        parameters.weeks_worked = 1500
        parameters.current_pension_savings = 100000000
        parameters.average_return = -2  # Error
        parameters.management_rate = 1

        self.assertRaises(Exceptions.RentabilidadPromedioNegativaError, CalculatorLogic.calculate_expected_pension_savings,
                          parameters)


# Este fragmento de codigo permite ejecutar la prueba individualmente
# Va fijo en todas las pruebas

if __name__ == '__main__':
    unittest.main()
