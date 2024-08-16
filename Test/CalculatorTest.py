import unittest
import Test_Error

import unittest


class ParametrosPension:
    def __init__(self):
        self.edad = None
        self.salario_actual = None
        self.semanas_laboradas = None
        self.ahorro_pensional_a_hoy = None
        self.rentabilidad_promedio = None
        self.tasa_administracion = None


class PensionTest(unittest.TestCase):

    def setUp(self):
        # Configuración inicial común a todas las pruebas
        self.parametros = ParametrosPension()

    # Casos normales (6)
    def test_caso_normal1(self):
        # Entradas
        self.parametros.edad = 25
        sexo = "m"
        estado_civil = "s"
        self.parametros.salario_actual = 1500000
        self.parametros.semanas_laboradas = 200
        self.parametros.ahorro_pensional_a_hoy = 1000000
        self.parametros.rentabilidad_promedio = 4
        self.parametros.tasa_administracion = 1

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 1000000
        valor_pension_esperada = 300000

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_caso_normal2(self):
        # Entradas
        self.parametros.edad = 45
        sexo = "m"
        estado_civil = "c"
        self.parametros.salario_actual = 3000000
        self.parametros.semanas_laboradas = 1000
        self.parametros.ahorro_pensional_a_hoy = 50000000
        self.parametros.rentabilidad_promedio = 3
        self.parametros.tasa_administracion = 1

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 50000000
        valor_pension_esperada = 1500000

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_caso_normal3(self):
        # Entradas
        self.parametros.edad = 28
        sexo = "f"
        estado_civil = "s"
        self.parametros.salario_actual = 1800000
        self.parametros.semanas_laboradas = 300
        self.parametros.ahorro_pensional_a_hoy = 2000000
        self.parametros.rentabilidad_promedio = 3
        self.parametros.tasa_administracion = 1

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 2000000
        valor_pension_esperada = 600000

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_caso_normal4(self):
        # Entradas
        self.parametros.edad = 50
        sexo = "f"
        estado_civil = "c"
        self.parametros.salario_actual = 3500000
        self.parametros.semanas_laboradas = 1200
        self.parametros.ahorro_pensional_a_hoy = 75000000
        self.parametros.rentabilidad_promedio = 4
        self.parametros.tasa_administracion = 1

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 75000000
        valor_pension_esperada = 2100000

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_caso_normal5(self):
        # Entradas
        self.parametros.edad = 60
        sexo = "m"
        estado_civil = "c"
        self.parametros.salario_actual = 4000000
        self.parametros.semanas_laboradas = 1600
        self.parametros.ahorro_pensional_a_hoy = 100000000
        self.parametros.rentabilidad_promedio = 4
        self.parametros.tasa_administracion = 1

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 100000000
        valor_pension_esperada = 2800000

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_caso_normal6(self):
        # Entradas
        self.parametros.edad = 58
        sexo = "f"
        estado_civil = "c"
        self.parametros.salario_actual = 3800000
        self.parametros.semanas_laboradas = 1500
        self.parametros.ahorro_pensional_a_hoy = 95000000
        self.parametros.rentabilidad_promedio = 3
        self.parametros.tasa_administracion = 1

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 95000000
        valor_pension_esperada = 2600000


        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    # casos Extraordinarios (6)

    def test_extraordinario1(self):
        # Entradas
        self.parametros.edad = 78
        sexo = "m"
        estado_civil = "s"
        self.parametros.salario_actual = 1300000
        self.parametros.semanas_laboradas = 200
        self.parametros.ahorro_pensional_a_hoy = 25000000
        self.parametros.rentabilidad_promedio = 1
        self.parametros.tasa_administracion = 2

        # Salidas esperadas: semanas laboradas menores que 1000
        valor_ahorro_pensional_esperado = 25000000
        valor_pension_esperada = 0

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_extraordinario2(self):
        # Entradas
        self.parametros.edad = 36
        sexo = "f"
        estado_civil = "c"
        self.parametros.salario_actual = 500000
        self.parametros.semanas_laboradas = 220
        self.parametros.ahorro_pensional_a_hoy = 15000000
        self.parametros.rentabilidad_promedio = 2
        self.parametros.tasa_administracion = 1

        # Salidas esperadas: Su salario es menor que el SMLV
        valor_ahorro_pensional_esperado = 15000000
        valor_pension_esperada = 0

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_extraordinario3(self):
        # Entradas
        self.parametros.edad = 77
        sexo = "m"
        estado_civil = "s"
        self.parametros.salario_actual = 200000
        self.parametros.semanas_laboradas = 700
        self.parametros.ahorro_pensional_a_hoy = 30000000
        self.parametros.rentabilidad_promedio = 2
        self.parametros.tasa_administracion = 2

        # Salidas esperadas: las semanas mínimas para pensionarse son 1300
        valor_ahorro_pensional_esperado = 30000000
        valor_pension_esperada = 0

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)  # Usando un valor que fallará

    def test_extraordinario4(self):
        # Entradas
        self.parametros.edad = 40
        sexo = "f"
        estado_civil = "s"
        self.parametros.salario_actual = 1300000
        self.parametros.semanas_laboradas = 1301
        self.parametros.ahorro_pensional_a_hoy = 15600000
        self.parametros.rentabilidad_promedio = 3
        self.parametros.tasa_administracion = 2

        # Salidas esperadas: Aún no tienes la edad mínima para pensionarse
        valor_ahorro_pensional_esperado = 15600000
        valor_pension_esperada = 0

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_extraordinario5(self):
        # Entradas
        self.parametros.edad = 76
        sexo = "m"
        estado_civil = "c"
        self.parametros.salario_actual = 80000000
        self.parametros.semanas_laboradas = 1300
        self.parametros.ahorro_pensional_a_hoy = 12078720000
        self.parametros.rentabilidad_promedio = 3
        self.parametros.tasa_administracion = 2

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 12078720000
        valor_pension_esperada = 56000000

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    def test_extraordinario6(self):
        # Entradas
        self.parametros.edad = 62
        sexo = "f"
        estado_civil = "s"
        self.parametros.salario_actual = 1300000
        self.parametros.semanas_laboradas = 1300
        self.parametros.ahorro_pensional_a_hoy = 117843200
        self.parametros.rentabilidad_promedio = 2
        self.parametros.tasa_administracion = 1

        # Salidas esperadas
        valor_ahorro_pensional_esperado = 117843200
        valor_pension_esperada = 490930

        self.assertEqual(self.parametros.ahorro_pensional_a_hoy, valor_ahorro_pensional_esperado)
        self.assertEqual(0, valor_pension_esperada)

    # casos de ErROR
    def test_error_salario_negativo(self):
        parametros = ParametrosPension()
        parametros.edad = 35
        parametros.salario_actual = -3000000  # Error
        parametros.semanas_laboradas = 800
        parametros.ahorro_pensional_a_hoy = 40000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        with self.assertRaises(SalarioNegativoError):
            parametros.validar()

    def test_error_semanas_laboradas_negativas(self):
        parametros = ParametrosPension()
        parametros.edad = 40
        parametros.salario_actual = 3500000
        parametros.semanas_laboradas = -100  # Error
        parametros.ahorro_pensional_a_hoy = 60000000
        parametros.rentabilidad_promedio = 4
        parametros.tasa_administracion = 1

        with self.assertRaises(SemanasLaboradasNegativasError):
            parametros.validar()

    def test_error_ahorro_pensional_negativo(self):
        parametros = ParametrosPension()
        parametros.edad = 50
        parametros.salario_actual = 4000000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = -10000000  # Error
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        with self.assertRaises(AhorroPensionalNegativoError):
            parametros.validar()

    def test_error_rentabilidad_promedio_negativa(self):
        parametros = ParametrosPension()
        parametros.edad = 55
        parametros.salario_actual = 5000000
        parametros.semanas_laboradas = 1500
        parametros.ahorro_pensional_a_hoy = 100000000
        parametros.rentabilidad_promedio = -2  # Error
        parametros.tasa_administracion = 1

        with self.assertRaises(RentabilidadPromedioNegativaError):
            parametros.validar()

    def test_error_tasa_administracion_excesiva(self):
        parametros = ParametrosPension()
        parametros.edad = 45
        parametros.salario_actual = 3800000
        parametros.semanas_laboradas = 1000
        parametros.ahorro_pensional_a_hoy = 70000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 4  # Error (excede el 3%)

        with self.assertRaises(TasaAdministracionExcesivaError):
            parametros.validar()

    def test_error_edad_muy_alta(self):
        parametros = ParametrosPension()
        parametros.edad = 130  # Error
        parametros.salario_actual = 2500000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = 50000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        with self.assertRaises(EdadDemasiadoAltaError):
            parametros.validar()

    def test_error_edad_muy_baja(self):
        parametros = ParametrosPension()
        parametros.edad = 12  # Error
        parametros.salario_actual = 1200000
        parametros.semanas_laboradas = 50
        parametros.ahorro_pensional_a_hoy = 2000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1

        with self.assertRaises(EdadDemasiadoBajaError):
            parametros.validar()
