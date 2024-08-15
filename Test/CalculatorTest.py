import unittest
import Test_Error

class ParametrosPension:
    def __init__(self):
        self.edad = None
        self.salario_actual = None
        self.semanas_laboradas = None
        self.ahorro_pensional_a_hoy = None
        self.rentabilidad_promedio = None
        self.tasa_administracion = None
        self.edad_pension_total = None


class PensionTest(unittest.TestCase):
    # casos normales (6)
    def test_caso_normal1(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 25
        sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 1500000
        parametros.semanas_laboradas = 200
        parametros.ahorro_pensional_a_hoy = 1000000
        parametros.rentabilidad_promedio = 4
        parametros.tasa_administracion = 1
        # salidas esperadas
        valor_ahorro_pensional_esperado = 1000000
        valor_pension_esperada = 300_000

    def test_caso_normal2(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 45
        sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 3000000
        parametros.semanas_laboradas = 1000
        parametros.ahorro_pensional_a_hoy = 50000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1
        # salidas esperadas
        valor_ahorro_pensional_esperado = 50000000
        valor_pension_esperada = 1500000

    def test_caso_normal3(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 28
        sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 1800000
        parametros.semanas_laboradas = 300
        parametros.ahorro_pensional_a_hoy = 2000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1
        # salidas esperadas
        valor_ahorro_pensional_esperado = 2000000
        valor_pension_esperada = 600000

    def test_caso_normal4(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 50
        sexo = "f"
        estado_civil = "c"
        parametros.salario_actual = 3500000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = 75000000
        parametros.rentabilidad_promedio = 4
        parametros.tasa_administracion = 1
        # salidas esperadas
        valor_ahorro_pensional_esperado = 75000000
        valor_pension_esperada = 2100000

    def test_caso_normal5(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 60
        sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 4000000
        parametros.semanas_laboradas = 1600
        parametros.ahorro_pensional_a_hoy = 100000000
        parametros.rentabilidad_promedio = 4
        parametros.tasa_administracion = 1
        # salidas esperadas
        valor_ahorro_pensional_esperado = 100000000
        valor_pension_esperada = 2800000

    def test_caso_normal6(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 58
        sexo = "f"
        estado_civil = "c"
        parametros.salario_actual = 3800000
        parametros.semanas_laboradas = 1500
        parametros.ahorro_pensional_a_hoy = 95000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1
        # salidas esperadas
        valor_ahorro_pensional_esperado = 95000000
        valor_pension_esperada = 2600000

    # casos Extraordinarios (6)
    def test_extraordinario1(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 78
        sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 1300000
        parametros.semanas_laboradas = 200
        parametros.ahorro_pensional_a_hoy = 25000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2
        # salidas esperadas: semanas laboradas menores que que 1000

    def test_extraordinario2(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 36
        sexo = "f"
        estado_civil = "c"
        parametros.salario_actual = 500000
        parametros.semanas_laboradas = 220
        parametros.ahorro_pensional_a_hoy = 15000000
        parametros.rentabilidad_promedio =2
        parametros.tasa_administracion =1
        # salidas esperadas: Su salario es menor que el SMLV

    def test_extraordinario3(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 77
        sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 200000
        parametros.semanas_laboradas = 700
        parametros.ahorro_pensional_a_hoy = 30000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 2
        # salidas esperadas: las semanas minimas para pensionarse son 1300

    def test_extraordinario4(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 40
        sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 1300000
        parametros.semanas_laboradas = 1301
        parametros.ahorro_pensional_a_hoy = 15600000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 2
        # salidas esperadas: Aun no tienes la edad minima para pensionarse

    def test_extraordinario5(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 76
        sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 80000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 12078720000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 2
        # salidas esperadas
        valor_ahorro_pensional_esperado = 12078720000
        valor_pension_esperada = 56000000

    def test_extraordinario6(self):
        parametros = ParametrosPension()
        # entradas
        parametros.edad = 62
        sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 1300000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 117843200
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 1
        # salidas esperadas
        valor_ahorro_pensional_esperado = 117843200
        valor_pension_esperada = 490930

    # casos de ErROR
    def test_error_edad_negativa(self):
        """
        Prueba para un caso donde la edad ingresada es negativa.
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = -5  # Error
        sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 2000000
        parametros.semanas_laboradas = 500
        parametros.ahorro_pensional_a_hoy = 20000000
        parametros.rentabilidad_promedio = 4
        parametros.tasa_administracion = 1
        # salidas esperadas: EdadNegativaError

    def test_error_salario_negativo(self):
        """
        Prueba para un caso donde el salario ingresado es negativo.
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = 35
        sexo = "f"
        estado_civil = "c"
        parametros.salario_actual = -3000000
        parametros.semanas_laboradas = 800
        parametros.ahorro_pensional_a_hoy = 40000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1
        # salidas esperadas: SalarioNegativoError

    def test_error_semanas_laboradas_negativas(self):
        """
        Prueba para un caso donde las semanas laboradas ingresadas son negativas.
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = 40
        sexo = "m"
        estado_civil = "s"
        parametros.salario_actual = 3500000
        parametros.semanas_laboradas = -100  # Error
        parametros.ahorro_pensional_a_hoy = 60000000
        parametros.rentabilidad_promedio = 4
        parametros.tasa_administracion = 1
        # salidas esperadas: SemanasLaboradasNegativasError

    def test_error_ahorro_pensional_negativo(self):
        """
        Prueba para un caso donde el ahorro pensional a hoy es negativo.
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = 50
        sexo = "f"
        estado_civil = "c"
        parametros.salario_actual = 4000000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = -10000000  # Error
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1
        # salidas esperadas: AhorroPensionalNegativoError

    def test_error_rentabilidad_promedio_negativa(self):
        """
        Prueba para un caso donde la rentabilidad promedio es negativa.
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = 55
        sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 5000000
        parametros.semanas_laboradas = 1500
        parametros.ahorro_pensional_a_hoy = 100000000
        parametros.rentabilidad_promedio = -2  # Error
        parametros.tasa_administracion = 1
        # salidas esperadas: RentabilidadPromedioNegativaError

    def test_error_tasa_administracion_excesiva(self):
        """
        Prueba para un caso donde la tasa de administración excede el 3%.
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = 45
        sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 3800000
        parametros.semanas_laboradas = 1000
        parametros.ahorro_pensional_a_hoy = 70000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 4  # Error (excede el 3%)
        # salidas esperadas: TasaAdministracionExcesivaError

    def test_error_edad_muy_alta(self):
        """
        Prueba para un caso donde la edad ingresada es demasiado alta (por ejemplo, más de 120 años).
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = 130  # Error
        sexo = "m"
        estado_civil = "c"
        parametros.salario_actual = 2500000
        parametros.semanas_laboradas = 1200
        parametros.ahorro_pensional_a_hoy = 50000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1
        # salidas esperadas: EdadDemasiadoAltaError

    def test_error_edad_muy_baja(self):
        """
        Prueba para un caso donde la edad ingresada es demasiado baja (por ejemplo, menos de 16 años).
        """
        parametros = ParametrosPension()
        # entradas erróneas
        parametros.edad = 12  # Error
        sexo = "f"
        estado_civil = "s"
        parametros.salario_actual = 1200000
        parametros.semanas_laboradas = 50
        parametros.ahorro_pensional_a_hoy = 2000000
        parametros.rentabilidad_promedio = 3
        parametros.tasa_administracion = 1
        # salidas esperadas: EdadDemasiadoBajaError
