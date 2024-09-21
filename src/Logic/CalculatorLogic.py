import sys
import os

sys.path.append("src")

"""
Necessary modules are imported from the pension calculator logic and custom exceptions.
"""

from Logic import Parameters
from Logic import Exceptions


def verify_age(age):
    """
    Función para verificar que la edad ingresada esté dentro de un rango aceptable.
    """

    EDAD_MAXIMA = 115
    EDAD_MINIMA = 18

    if age < EDAD_MINIMA or age > EDAD_MAXIMA:
        raise Exceptions.EdadError(f"Su edad, la cual es: {age}, debe ser mayor a 18 y menor a 115")


def verify_current_salary(current_salary):
    """
    Función para verificar que el salario actual sea válido.
    """

    SALARIO_MINIMO = 0

    if current_salary < SALARIO_MINIMO:
        raise Exceptions.SalarioActualNegativoError(f"Su salario, el cual es: {current_salary}, debe ser mayor a 0")


def verify_weeks_worked(weeks_worked):
    """
    Función para verificar que las semanas laboradas sean positivas.
    """

    SEMANAS_LABORADAS_MINIMAS = 0

    if weeks_worked < SEMANAS_LABORADAS_MINIMAS:
        raise Exceptions.SemanasLaboradasNegativasError(
            f"Las semanas laboradas, las cuales son: {weeks_worked}, deben ser mayores a 0")


def verify_management_rate(management_rate):
    """
    Función para verificar que la tasa de administración esté en un rango válido (0-3%).
    """

    TASA_ADMINISTRACION_MINIMA = 0
    TASA_ADMINISTRACION_MAXIMA = 3

    if management_rate < TASA_ADMINISTRACION_MINIMA or management_rate > TASA_ADMINISTRACION_MAXIMA:
        raise Exceptions.TasaAdministracionError(
            f"La tasa de administración, la cual es: {management_rate}, debe ser mayor a 0 y menor a 3")


def verify_pension_savings(current_pension_savings):
    """
    Función para verificar que el ahorro pensional no sea negativo.
    """

    AHORRO_PENSIONAL_MINIMO = 0

    if current_pension_savings < AHORRO_PENSIONAL_MINIMO:
        raise Exceptions.AhorroPensionalNegativoError(
            f"El ahorro pensional a hoy, el cual es: {current_pension_savings}, debe ser mayor a 0")


def check_average_profitability(average_return):
    """
    Función para verificar que la rentabilidad promedio sea positiva.
    """

    RENTABILIDAD_PROMEDIO_MINIMO = 0

    if average_return < RENTABILIDAD_PROMEDIO_MINIMO:
        raise Exceptions.RentabilidadPromedioNegativaError(
            f"La rentabilidad promedio, la cual es: {average_return}, debe ser mayor que 0")


def calculate_expected_pension_savings(parameters):
    """
      Función para calcular el ahorro pensional esperado.

      :param parameters: Un objeto que contiene datos del usuario como edad, sexo, salario actual,
                         semanas laboradas, tasa de administración, ahorro pensional actual,
                         y rentabilidad promedio.
      :return: El ahorro pensional esperado hasta la edad de retiro.
      """

    verify_age(parameters.age)
    verify_gender(parameters.gender)
    verify_current_salary(parameters.current_salary)
    verify_weeks_worked(parameters.weeks_worked)
    verify_pension_savings(parameters.current_pension_savings)
    verify_management_rate(parameters.management_rate)

    # Determina la edad de retiro según el sexo (62 años para hombres, 57 para mujeres)
    EDAD_JUBILACION_HOMBRES = 62
    EDAD_JUBILACION_MUJERES = 57

    edad_retiro = EDAD_JUBILACION_HOMBRES if parameters.gender == 'M' else EDAD_JUBILACION_MUJERES
    años_restantes = edad_retiro - parameters.age

    # Cálculo de las semanas restantes hasta la edad de retiro

    NUMERO_DE_SEMANAS_ANUALES = 52
    semanas_restantes = años_restantes * NUMERO_DE_SEMANAS_ANUALES

    # Cálculo del ahorro pensional esperado usando una fórmula financiera

    expected_pension_savings = (
            parameters.current_pension_savings * (1 + parameters.average_return) ** años_restantes +
            parameters.current_salary * semanas_restantes * (1 + parameters.average_return) ** (
                    años_restantes - 1) / NUMERO_DE_SEMANAS_ANUALES
    )

    return expected_pension_savings


def calculate_expected_pension(expected_pension_savings, gender):
    """
    Función para calcular la pensión esperada basada en el ahorro y el sexo.

    :param expected_pension_savings: El total del ahorro pensional que se espera tener.
    :param gender: El sexo de la persona ('M' para masculino, 'F' para femenino).
    :return: La pensión mensual esperada.
    """

    ESPERANZA_DE_VIDA_PROMEDIO = 80
    EDAD_JUBILACION_HOMBRES = 62
    EDAD_JUBILACION_MUJERES = 57

    # Validar el parámetro 'sexo'
    if gender not in ['M', 'F']:
        raise ValueError("El sexo debe ser 'M' para masculino o 'F' para femenino.")

    # Asignar años esperados de vida según el sexo
    if gender == 'M':
        años_esperados_de_vida = ESPERANZA_DE_VIDA_PROMEDIO - EDAD_JUBILACION_HOMBRES
    else:
        años_esperados_de_vida = ESPERANZA_DE_VIDA_PROMEDIO - EDAD_JUBILACION_MUJERES

    # Calcular la pensión mensual esperada
    pension = expected_monthly_pension(expected_pension_savings, años_esperados_de_vida)

    return pension


def expected_monthly_pension(expected_pension_savings, expected_years_of_life):
    """
    Función auxiliar para calcular la pensión mensual esperada.

    :param expected_pension_savings: El total del ahorro pensional que se espera tener.
    :param expected_years_of_life: El número de años que se espera que viva después de pensionarse.
    :return: La pensión mensual esperada.
    """

    AHORRO_PENSIONAL_MINIMO = 0
    MESES_POR_AÑO = 12
    AÑOS_MINIMOS = 0

    # Verificar que los años esperados de vida sean mayores a cero para evitar divisiones por cero
    if expected_years_of_life <= AÑOS_MINIMOS:
        raise ValueError("El número de años esperados de vida debe ser mayor a 0.")

    # Verificar que el ahorro pensional sea mayor o igual a cero
    if expected_pension_savings < AHORRO_PENSIONAL_MINIMO:
        raise ValueError("El ahorro pensional esperado no puede ser negativo.")

    # Calcular la pensión mensual esperada
    pension_mensual = expected_pension_savings / (expected_years_of_life * MESES_POR_AÑO)
    return pension_mensual
