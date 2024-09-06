import unittest
import sys
import os

#sys.path.append("src")
sys.path.append(os.path.abspath("C:/Users/USER/PycharmProjects/CalculadoraPensional/src"))
from Logic import Parameters
from Logic import CalculatorLogic
from Logic import Exceptions


class PensionTest(unittest.TestCase):

    # Casos normales (6)
    def test_normal_case1(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 65
        parametros.sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 2300000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = 30000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 1

        ahorro_total = 3637.656861250826
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_normal_case2(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 30
        parametros.sexo = "F"
        estado_civil = "s"
        parametros.salario_actual = 1800000
        parametros.semanas_laboradas = 1520
        parametros.ahorro_pensional_a_hoy = 25000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 1

        ahorro_total = 3.141746163814644e+20
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_normal_case3(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 40
        parametros.sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 3500000
        parametros.semanas_laboradas = 1040
        parametros.ahorro_pensional_a_hoy = 85000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 1

        ahorro_total = 1.35381937545e+16
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_normal_case4(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 45
        parametros.sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 2500000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 120000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 1

        ahorro_total = 552960000000.0
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_normal_case5(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 50
        parametros.sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 4200000
        parametros.semanas_laboradas = 1560
        parametros.ahorro_pensional_a_hoy = 200000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2

        ahorro_total = 27481600000.0
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_normal_case6(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 25
        parametros.sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 1200000
        parametros.semanas_laboradas = 1260
        parametros.ahorro_pensional_a_hoy = 10000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 2

        ahorro_total = 4.224886030582197e+22
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    # casos Extraordinarios (6)

    def test_extraordinario1(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 35
        parametros.sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 2000000
        parametros.semanas_laboradas = 300
        parametros.ahorro_pensional_a_hoy = 25000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2

        ahorro_total = 197132288000000.0
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_extraordinario2(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 36
        parametros.sexo = "f"
        estado_civil = "c"
        parametros.salario_actual = 500000
        parametros.semanas_laboradas = 220
        parametros.ahorro_pensional_a_hoy = 15000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 1

        ahorro_total = 1.935165342555e+17
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_extraordinario3(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 77
        parametros.sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 200000
        parametros.semanas_laboradas = 700
        parametros.ahorro_pensional_a_hoy = 30000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 2

        ahorro_total = 0.008221519706938333
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_extraordinario4(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 40
        parametros.sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 1300000
        parametros.semanas_laboradas = 1301
        parametros.ahorro_pensional_a_hoy = 15600000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 2

        ahorro_total = 3.62924736512e+17
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_extraordinario5(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 76
        parametros.sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 80000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 12078720000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 2

        ahorro_total = 0.042559695430099964
        resultado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        self.assertEqual(resultado, ahorro_total)

    def test_extraordinario6(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 62
        parametros.sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 1300000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 117843200
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 1


    # Casos de Error...
    def test_error_edad_muy_alta(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 130  # Error
        estado_civil = "s"
        parametros.sexo = "m"
        parametros.salario_actual = 2500000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = 50000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        self.assertRaises(Exceptions.EdadError, CalculatorLogic.calcularAhorroPensionalEsperado,
                          parametros)

    def test_error_edad_muy_baja(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 12  # Error
        parametros.sexo = "M"
        estado_civil = "s"
        parametros.salario_actual = 1200000
        parametros.semanas_laboradas = 50
        parametros.ahorro_pensional_a_hoy = 2000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        self.assertRaises(Exceptions.EdadError,CalculatorLogic.calcularAhorroPensionalEsperado, parametros)

    def test_error_salario_negativo(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 35
        parametros.sexo = "F"
        estado_civil = "s"
        parametros.salario_actual = -3000000  # Error
        parametros.semanas_laboradas = 800
        parametros.ahorro_pensional_a_hoy = 40000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        self.assertRaises(Exceptions.SalarioActualNegativoError, CalculatorLogic.calcularAhorroPensionalEsperado,
                          parametros)

    def test_error_semanas_laboradas_negativas(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 40
        parametros.sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 3500000
        parametros.semanas_laboradas = -100  # Error
        parametros.ahorro_pensional_a_hoy = 60000000
        parametros.rentabilidad_promedio = 4
        parametros.tasa_administracion = 1

        self.assertRaises(Exceptions.SemanasLaboradasNegativasError, CalculatorLogic.calcularAhorroPensionalEsperado,
                          parametros)

    def test_error_ahorro_pensional_negativo(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 50
        parametros.sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 4000000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = -10000000  # Error
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        self.assertRaises(Exceptions.AhorroPensionalNegativoError, CalculatorLogic.calcularAhorroPensionalEsperado,
                          parametros)

    def test_error_tasa_administracion_excesiva(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 45
        parametros.sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 3800000
        parametros.semanas_laboradas = 1000
        parametros.ahorro_pensional_a_hoy = 70000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 4  # Error (excede el 3%)

        self.assertRaises(Exceptions.TasaAdministracionError, CalculatorLogic.calcularAhorroPensionalEsperado,
                          parametros)

    def test_error_rentabilidad_promedio_negativa(self):
        parametros = Parameters.ParametrosPension()
        # Entradas
        parametros.edad = 55
        parametros.sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 5000000
        parametros.semanas_laboradas = 1500
        parametros.ahorro_pensional_a_hoy = 100000000
        parametros.rentabilidad_promedio = -2  # Error
        parametros.tasa_administracion = 1

        self.assertRaises(Exceptions.RentabilidadPromedioNegativaError, CalculatorLogic.calcularAhorroPensionalEsperado,
                          parametros)


# Este fragmento de codigo permite ejecutar la prueba individualmente
# Va fijo en todas las pruebas


if __name__ == '__main__':
    # print( Payment.calcPayment.__doc__)
    unittest.main()
