import sys
sys.path.append("src")
from Model.Exceptions import *
from Model.Parameters import ParametrosPension as Parameters


class CalculadoraPensionalModel:
    """Modelo de cálculo pensional que realiza validaciones y proyecciones de ahorro y pensión.

    Constantes:
        EDAD_MAXIMA (int): Edad máxima permitida.
        EDAD_MINIMA (int): Edad mínima permitida.
        SALARIO_MINIMO (int): Salario mínimo permitido.
        SEMANAS_LABORADAS_MINIMAS (int): Semanas mínimas trabajadas.
        TASA_ADMINISTRACION_MINIMA (int): Tasa mínima de administración.
        TASA_ADMINISTRACION_MAXIMA (int): Tasa máxima de administración.
        RENTABILIDAD_PROMEDIO_MINIMO (int): Rentabilidad promedio mínima.
        RENTABILIDAD_PROMEDIO_MAXIMA (int): Rentabilidad promedio máxima.
        ESPERANZA_DE_VIDA_PROMEDIO (int): Esperanza de vida promedio.
        EDAD_JUBILACION_HOMBRES (int): Edad de jubilación para hombres.
        EDAD_JUBILACION_MUJERES (int): Edad de jubilación para mujeres.
        MESES_POR_AÑO (int): Meses en un año.
        NUMERO_DE_SEMANAS_ANUALES (int): Número de semanas en un año.
    """
    
    EDAD_MAXIMA = 115
    EDAD_MINIMA = 18
    SALARIO_MINIMO = 0
    SEMANAS_LABORADAS_MINIMAS = 0
    AHORRO_PENSIONAL_MINIMO = 0
    TASA_ADMINISTRACION_MINIMA = 0
    TASA_ADMINISTRACION_MAXIMA = 3
    RENTABILIDAD_PROMEDIO_MINIMO = 0
    RENTABILIDAD_PROMEDIO_MAXIMA = 3
    ESPERANZA_DE_VIDA_PROMEDIO = 80
    EDAD_JUBILACION_HOMBRES = 62
    EDAD_JUBILACION_MUJERES = 57
    AHORRO_PENSIONAL_MINIMO = 0
    MESES_POR_AÑO = 12
    NUMERO_DE_SEMANAS_ANUALES = 52

    def __init__(self, parameters: Parameters):
        """Inicializa el modelo de cálculo pensional con los parámetros del usuario.

        Args:
            parameters (Parameters): Objeto con los parámetros necesarios para el cálculo.
        """
        self.parameters = parameters
        self.expected_pension_savings = 0

    def verify_age(self):
        """Verifica que la edad esté dentro del rango permitido.

        Raises:
            EdadError: Si la edad es menor que EDAD_MINIMA o mayor que EDAD_MAXIMA.
        """
        if self.parameters.age < CalculadoraPensionalModel.EDAD_MINIMA or self.parameters.age > CalculadoraPensionalModel.EDAD_MAXIMA:
            raise EdadError(f"Su edad, la cual es: {self.parameters.age}, debe ser mayor a 18 y menor a 115")
        
        return self.parameters.age

    def verify_current_salary(self):
        """Verifica que el salario actual sea positivo.

        Raises:
            SalarioActualNegativoError: Si el salario es menor que SALARIO_MINIMO.
        """
        if self.parameters.current_salary < CalculadoraPensionalModel.SALARIO_MINIMO:
            raise SalarioActualNegativoError(f"Su salario, el cual es: {self.parameters.current_salary}, debe ser mayor a 0")
        return self.parameters.current_salary

    def verify_weeks_worked(self):
        """Verifica que las semanas trabajadas sean mayores que cero.

        Raises:
            SemanasLaboradasNegativasError: Si weeks_worked es menor que SEMANAS_LABORADAS_MINIMAS.
        """
        if self.parameters.weeks_worked < CalculadoraPensionalModel.SEMANAS_LABORADAS_MINIMAS:
            raise SemanasLaboradasNegativasError(
                f"Las semanas laboradas, las cuales son: {self.parameters.weeks_worked}, deben ser mayores a 0")

    def verify_pension_savings(self):
        """Verifica que el ahorro pensional actual sea positivo.

        Raises:
            AhorroPensionalNegativoError: Si current_pension_savings es menor que AHORRO_PENSIONAL_MINIMO.
        """
        if self.parameters.current_pension_savings < CalculadoraPensionalModel.AHORRO_PENSIONAL_MINIMO:
            raise AhorroPensionalNegativoError(
                f"El ahorro pensional a hoy, el cual es: {self.parameters.current_pension_savings}, debe ser mayor a 0")

    def verify_management_rate(self):
        """Verifica que la tasa de administración esté dentro del rango permitido.

        Raises:
            TasaAdministracionError: Si management_rate está fuera del rango permitido.
        """
        if self.parameters.management_rate < CalculadoraPensionalModel.TASA_ADMINISTRACION_MINIMA or self.parameters.management_rate > CalculadoraPensionalModel.TASA_ADMINISTRACION_MAXIMA:
            raise TasaAdministracionError(
                f"La tasa de administración, la cual es: {self.parameters.management_rate}, debe ser mayor a 0 y menor a 3")

    def verify_average_profitability(self):
        """Verifica que la rentabilidad promedio esté dentro del rango permitido.

        Raises:
            RentabilidadPromedioNegativaError: Si average_return está fuera del rango permitido.
        """
        if self.parameters.average_return < CalculadoraPensionalModel.RENTABILIDAD_PROMEDIO_MINIMO or self.parameters.average_return > CalculadoraPensionalModel.RENTABILIDAD_PROMEDIO_MAXIMA:
            raise RentabilidadPromedioNegativaError(
                f"La rentabilidad promedio, la cual es: {self.parameters.average_return}, debe ser mayor que 0")

    def calculate_expected_pension_savings(self):
        """Calcula el ahorro pensional esperado en función de los parámetros actuales."""
        self.verify_age()
        self.verify_current_salary()
        self.verify_weeks_worked()
        self.verify_pension_savings()
        self.verify_average_profitability()
        self.verify_management_rate()

        edad_retiro = CalculadoraPensionalModel.EDAD_JUBILACION_HOMBRES if self.parameters.gender == 'M' else CalculadoraPensionalModel.EDAD_JUBILACION_MUJERES
        años_restantes = edad_retiro - self.parameters.age
        semanas_restantes = años_restantes * CalculadoraPensionalModel.NUMERO_DE_SEMANAS_ANUALES

        self.expected_pension_savings = (
            self.parameters.current_pension_savings * (1 + self.parameters.average_return) ** años_restantes +
            self.parameters.current_salary * semanas_restantes * (1 + self.parameters.average_return) ** (
                    años_restantes - 1) / CalculadoraPensionalModel.NUMERO_DE_SEMANAS_ANUALES
        )
        return

    def calculate_expected_pension(self):
        """Calcula la pensión mensual esperada basado en el ahorro proyectado y la esperanza de vida.

        Raises:
            GenderError: Si el género no es 'M' o 'F'.
        """
        self.parameters.gender = self.parameters.gender.upper()
        if self.parameters.gender not in ['M', 'F']:
            raise GenderError("El sexo debe ser 'M' para masculino o 'F' para femenino.")

        if self.parameters.gender == 'M':
            años_esperados_de_vida = CalculadoraPensionalModel.ESPERANZA_DE_VIDA_PROMEDIO - CalculadoraPensionalModel.EDAD_JUBILACION_HOMBRES
        else:
            años_esperados_de_vida = CalculadoraPensionalModel.ESPERANZA_DE_VIDA_PROMEDIO - CalculadoraPensionalModel.EDAD_JUBILACION_MUJERES

        return self.expected_monthly_pension(años_esperados_de_vida)

    def expected_monthly_pension(self, expected_years_of_life):
        """Calcula la pensión mensual esperada en función de los años de vida esperados.

        Args:
            expected_years_of_life (int): Años esperados de vida después de la jubilación.

        Returns:
            float: Valor de la pensión mensual esperada.

        Raises:
            ExpectedYearsOfLifeError: Si expected_years_of_life es menor o igual a 0.
            ExpectedPensionSavingsError: Si el ahorro pensional esperado es negativo.
        """
        if expected_years_of_life <= 0:
            raise ExpectedYearsOfLifeError("El número de años esperados de vida debe ser mayor a 0.")

        if self.expected_pension_savings < CalculadoraPensionalModel.AHORRO_PENSIONAL_MINIMO:
            raise ExpectedPensionSavingsError("El ahorro pensional esperado no puede ser negativo.")

        return self.expected_pension_savings / (expected_years_of_life * CalculadoraPensionalModel.MESES_POR_AÑO)
