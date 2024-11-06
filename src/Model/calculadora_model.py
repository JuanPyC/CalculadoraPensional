import sys 
sys.path.append("src")
from Model import Exceptions
from Model.Exceptions import *
from Model import Parameters


class CalculadoraPensionalModel:
    # Métodos de verificación
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

    def verify_age(self, age):
        if age < CalculadoraPensionalModel.EDAD_MINIMA or age > CalculadoraPensionalModel.EDAD_MAXIMA:
            raise EdadError(f"Su edad, la cual es: {age}, debe ser mayor a 18 y menor a 115")

    def verify_current_salary(self, current_salary):
        if current_salary < CalculadoraPensionalModel.SALARIO_MINIMO:
            raise SalarioActualNegativoError(f"Su salario, el cual es: {current_salary}, debe ser mayor a 0")

    def verify_weeks_worked(self, weeks_worked):
        if weeks_worked < CalculadoraPensionalModel.SEMANAS_LABORADAS_MINIMAS:
            raise SemanasLaboradasNegativasError(
                f"Las semanas laboradas, las cuales son: {weeks_worked}, deben ser mayores a 0")

    def verify_pension_savings(self, current_pension_savings):
        if current_pension_savings < CalculadoraPensionalModel.AHORRO_PENSIONAL_MINIMO:
            raise AhorroPensionalNegativoError(
                f"El ahorro pensional a hoy, el cual es: {current_pension_savings}, debe ser mayor a 0")

    def verify_management_rate(self, management_rate):
        if management_rate < CalculadoraPensionalModel.TASA_ADMINISTRACION_MINIMA or management_rate > CalculadoraPensionalModel.TASA_ADMINISTRACION_MAXIMA:
            raise TasaAdministracionError(
                f"La tasa de administración, la cual es: {management_rate}, debe ser mayor a 0 y menor a 3")

    def verify_average_profitability(self, average_return):
        if average_return < CalculadoraPensionalModel.RENTABILIDAD_PROMEDIO_MINIMO or average_return > CalculadoraPensionalModel.RENTABILIDAD_PROMEDIO_MAXIMA:
            raise RentabilidadPromedioNegativaError(
                f"La rentabilidad promedio, la cual es: {average_return}, debe ser mayor que 0")

    # Método para calcular el ahorro pensional esperado
    def calculate_expected_pension_savings(self, parameters: Parameters):
        self.verify_age(parameters.age)
        self.verify_current_salary(parameters.current_salary)
        self.verify_weeks_worked(parameters.weeks_worked)
        self.verify_pension_savings(parameters.current_pension_savings)
        self.verify_average_profitability(parameters.average_return)
        self.verify_management_rate(parameters.management_rate)

        EDAD_JUBILACION_HOMBRES = 62
        EDAD_JUBILACION_MUJERES = 57
        edad_retiro = EDAD_JUBILACION_HOMBRES if parameters.gender == 'M' else EDAD_JUBILACION_MUJERES
        años_restantes = edad_retiro - parameters.age

        NUMERO_DE_SEMANAS_ANUALES = 52
        semanas_restantes = años_restantes * NUMERO_DE_SEMANAS_ANUALES

        expected_pension_savings = (
            parameters.current_pension_savings * (1 + parameters.average_return) ** años_restantes +
            parameters.current_salary * semanas_restantes * (1 + parameters.average_return) ** (
                    años_restantes - 1) / NUMERO_DE_SEMANAS_ANUALES
        )
        return expected_pension_savings

    def calculate_expected_pension(self, expected_pension_savings, gender:str):
        gender.upper()
        if gender not in ['M', 'F']:
            raise GenderError("El sexo debe ser 'M' para masculino o 'F' para femenino.")

        if gender == 'M':
            años_esperados_de_vida = CalculadoraPensionalModel.ESPERANZA_DE_VIDA_PROMEDIO - CalculadoraPensionalModel.EDAD_JUBILACION_HOMBRES
        else:
            años_esperados_de_vida = CalculadoraPensionalModel.ESPERANZA_DE_VIDA_PROMEDIO - CalculadoraPensionalModel.EDAD_JUBILACION_MUJERES

        return self.expected_monthly_pension(expected_pension_savings, años_esperados_de_vida)

    def expected_monthly_pension(self, expected_pension_savings, expected_years_of_life):
        if expected_years_of_life <= 0:
            raise ExpectedYearsOfLifeError("El número de años esperados de vida debe ser mayor a 0.")

        if expected_pension_savings < CalculadoraPensionalModel.AHORRO_PENSIONAL_MINIMO:
            raise ExpectedPensionSavingsError("El ahorro pensional esperado no puede ser negativo.")

        return expected_pension_savings / (expected_years_of_life * CalculadoraPensionalModel.MESES_POR_AÑO)
