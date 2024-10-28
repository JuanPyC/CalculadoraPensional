import sys 
sys.path.append("src")

import psycopg2
from src import SecretConfig
from Model import Exceptions
from Model.Exceptions import DatabaseError

class CalculadoraPensionalModel:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                HOST = SecretConfig.PGHOST,
                DATABASE = SecretConfig.PGDATABASE,
                USER = SecretConfig.PGUSER,
                PASSWORD = SecretConfig.PGPASSWORD
                )
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            raise DatabaseError("Error al conectar con la base de datos") from e

    # Métodos de verificación
    def verify_age(self, age):
        EDAD_MAXIMA = 115
        EDAD_MINIMA = 18
        if age < EDAD_MINIMA or age > EDAD_MAXIMA:
            raise Exceptions.EdadError(f"Su edad, la cual es: {age}, debe ser mayor a 18 y menor a 115")

    def verify_current_salary(self, current_salary):
        SALARIO_MINIMO = 0
        if current_salary < SALARIO_MINIMO:
            raise Exceptions.SalarioActualNegativoError(f"Su salario, el cual es: {current_salary}, debe ser mayor a 0")

    def verify_weeks_worked(self, weeks_worked):
        SEMANAS_LABORADAS_MINIMAS = 0
        if weeks_worked < SEMANAS_LABORADAS_MINIMAS:
            raise Exceptions.SemanasLaboradasNegativasError(
                f"Las semanas laboradas, las cuales son: {weeks_worked}, deben ser mayores a 0")

    def verify_pension_savings(self, current_pension_savings):
        AHORRO_PENSIONAL_MINIMO = 0
        if current_pension_savings < AHORRO_PENSIONAL_MINIMO:
            raise Exceptions.AhorroPensionalNegativoError(
                f"El ahorro pensional a hoy, el cual es: {current_pension_savings}, debe ser mayor a 0")

    def verify_management_rate(self, management_rate):
        TASA_ADMINISTRACION_MINIMA = 0
        TASA_ADMINISTRACION_MAXIMA = 3
        if management_rate < TASA_ADMINISTRACION_MINIMA or management_rate > TASA_ADMINISTRACION_MAXIMA:
            raise Exceptions.TasaAdministracionError(
                f"La tasa de administración, la cual es: {management_rate}, debe ser mayor a 0 y menor a 3")

    def verify_average_profitability(self, average_return):
        RENTABILIDAD_PROMEDIO_MINIMO = 0
        RENTABILIDAD_PROMEDIO_MAXIMA = 3
        if average_return < RENTABILIDAD_PROMEDIO_MINIMO or average_return > RENTABILIDAD_PROMEDIO_MAXIMA:
            raise Exceptions.RentabilidadPromedioNegativaError(
                f"La rentabilidad promedio, la cual es: {average_return}, debe ser mayor que 0")

    # Método para calcular el ahorro pensional esperado
    def calculate_expected_pension_savings(self, parameters):
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

    def calculate_expected_pension(self, expected_pension_savings, gender):
        ESPERANZA_DE_VIDA_PROMEDIO = 80
        EDAD_JUBILACION_HOMBRES = 62
        EDAD_JUBILACION_MUJERES = 57

        if gender not in ['M', 'F']:
            raise ValueError("El sexo debe ser 'M' para masculino o 'F' para femenino.")

        if gender == 'M':
            años_esperados_de_vida = ESPERANZA_DE_VIDA_PROMEDIO - EDAD_JUBILACION_HOMBRES
        else:
            años_esperados_de_vida = ESPERANZA_DE_VIDA_PROMEDIO - EDAD_JUBILACION_MUJERES

        return self.expected_monthly_pension(expected_pension_savings, años_esperados_de_vida)

    def expected_monthly_pension(self, expected_pension_savings, expected_years_of_life):
        AHORRO_PENSIONAL_MINIMO = 0
        MESES_POR_AÑO = 12

        if expected_years_of_life <= 0:
            raise ValueError("El número de años esperados de vida debe ser mayor a 0.")

        if expected_pension_savings < AHORRO_PENSIONAL_MINIMO:
            raise ValueError("El ahorro pensional esperado no puede ser negativo.")

        return expected_pension_savings / (expected_years_of_life * MESES_POR_AÑO)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
