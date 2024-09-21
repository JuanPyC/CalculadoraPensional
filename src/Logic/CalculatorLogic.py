import sys
import os

sys.path.append("src")

"""Se importan los módulos necesarios desde la lógica de la calculadora
pensional y excepciones personalizadas"""

from Logic import Parameters
from Logic import Exceptions


def verificarEdad(edad):
    """
    Función para verificar que la edad ingresada esté dentro de un rango aceptable
    """

    EDAD_MINIMA = 18
    EDAD_MAXIMA = 115

    if edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
        raise Exceptions.EdadError(f"Su edad, la cual es: {edad}, debe ser mayor a 18 y menor a 115")


def verificarSalarioActual(salario_actual):
    """
    Función para verificar que el salario actual sea válido
    """

    SALARIO_MINIMO = 0

    if salario_actual < SALARIO_MINIMO:
        raise Exceptions.SalarioActualNegativoError(f"Su salario, el cual es: {salario_actual}, debe ser mayor a 0")


def verificarSemanasLaboradas(semanas_laboradas):
    """
    Función para verificar que las semanas laboradas sean positivas
    """

    SEMANAS_LABORADAS_MINIMAS = 0

    if semanas_laboradas < SEMANAS_LABORADAS_MINIMAS:
        raise Exceptions.SemanasLaboradasNegativasError(
            f"Las semanas laboradas, las cuales son: {semanas_laboradas}, deben ser mayores a 0")


def verificarTasaAdministracion(tasa_administracion):
    """
    Función para verificar que la tasa de administración esté en un rango válido (0-3%)
    """

    TASA_ADMINISTRACION_MINIMA = 0
    TASA_ADMINISTRACION_MAXIMA = 3

    if tasa_administracion < TASA_ADMINISTRACION_MINIMA or tasa_administracion > TASA_ADMINISTRACION_MAXIMA:
        raise Exceptions.TasaAdministracionError(
            f"La tasa de administración, la cual es: {tasa_administracion}, debe ser mayor a 0 y menor a 3")


def verificarAhorroPensional(ahorro_pensional_a_hoy):
    """
    Función para verificar que el ahorro pensional no sea negativo
    """

    AHORRO_PENSIONAL_MINIMO = 0

    if ahorro_pensional_a_hoy < AHORRO_PENSIONAL_MINIMO:
        raise Exceptions.AhorroPensionalNegativoError(
            f"El ahorro pensional a hoy, el cual es: {ahorro_pensional_a_hoy}, debe ser mayor a 0")


def verificarRentabilidadPromedio(rentabilidad_promedio):
    """
    Función para verificar que la rentabilidad promedio sea positiva
    """

    AHORRO_PENSIONAL_MINIMO = 0

    if rentabilidad_promedio < AHORRO_PENSIONAL_MINIMO:
        raise Exceptions.RentabilidadPromedioNegativaError(
            f"La rentabilidad promedio, la cual es: {rentabilidad_promedio}, debe ser mayor que 0")


def calcularAhorroPensionalEsperado(parametros):
    """
    Función para calcular el ahorro pensional esperado
    """

    verificarAhorroPensional(parametros.ahorro_pensional_a_hoy)
    verificarEdad(parametros.edad)
    verificarSalarioActual(parametros.salario_actual)
    verificarTasaAdministracion(parametros.tasa_administracion)
    verificarSemanasLaboradas(parametros.semanas_laboradas)

    # Determina la edad de retiro según el sexo (62 años para hombres, 57 para mujeres)
    EDAD_JUBILACION_HOMBRES = 62
    EDAD_JUBILACION_MUJERES = 57

    edad_retiro = EDAD_JUBILACION_HOMBRES if parametros.sexo == 'M' else EDAD_JUBILACION_MUJERES
    años_restantes = edad_retiro - parametros.edad

    # Cálculo de las semanas restantes hasta la edad de retiro

    NUMERO_DE_SEMANAS_ANUALES = 52
    semanas_restantes = años_restantes * NUMERO_DE_SEMANAS_ANUALES

    # Cálculo del ahorro pensional esperado usando una fórmula financiera

    ahorro_pensional_esperado = (
            parametros.ahorro_pensional_a_hoy * (1 + parametros.rentabilidad_promedio) ** años_restantes +
            parametros.salario_actual * semanas_restantes * (1 + parametros.rentabilidad_promedio) ** (
                    años_restantes - 1) / NUMERO_DE_SEMANAS_ANUALES
    )

    return ahorro_pensional_esperado


def calcular_pension_esperada(ahorro_pensional_esperado, sexo):
    """
    Función para calcular la pensión esperada basada en el ahorro y el sexo.

    :param ahorro_pensional_esperado: El total del ahorro pensional que se espera tener.
    :param sexo: El sexo de la persona ('M' para masculino, 'F' para femenino).
    :return: La pensión mensual esperada.
    """

    EDAD_JUBILACION_HOMBRES = 62
    EDAD_JUBILACION_MUJERES = 57
    ESPERANZA_DE_VIDA_PROMEDIO = 80

    # Validar el parámetro 'sexo'
    if sexo not in ['M', 'F']:
        raise ValueError("El sexo debe ser 'M' para masculino o 'F' para femenino.")

    # Asignar años esperados de vida según el sexo
    if sexo == 'M':
        años_esperados_de_vida = ESPERANZA_DE_VIDA_PROMEDIO - EDAD_JUBILACION_HOMBRES
    else:
        años_esperados_de_vida = ESPERANZA_DE_VIDA_PROMEDIO - EDAD_JUBILACION_MUJERES

    # Calcular la pensión mensual esperada
    pension = pension_esperada_mensual(ahorro_pensional_esperado, años_esperados_de_vida)

    return pension


def pension_esperada_mensual(ahorro_pensional_esperado, años_esperados_de_vida):
    """
    Función auxiliar para calcular la pensión mensual esperada.

    :param ahorro_pensional_esperado: El total del ahorro pensional que se espera tener.
    :param años_esperados_de_vida: El número de años que se espera que viva después de pensionarse.
    :return: La pensión mensual esperada.
    """

    MESES_POR_AÑO = 12
    AÑOS_MINIMOS= 0
    AHORRO_PENSIONAL_MINIMO = 0
    # Verificar que los años esperados de vida sean mayores a cero para evitar divisiones por cero
    if años_esperados_de_vida <= AÑOS_MINIMOS:
        raise ValueError("El número de años esperados de vida debe ser mayor a 0.")

    # Verificar que el ahorro pensional sea mayor o igual a cero
    if ahorro_pensional_esperado < AHORRO_PENSIONAL_MINIMO:
        raise ValueError("El ahorro pensional esperado no puede ser negativo.")

    # Calcular la pensión mensual esperada
    pension_mensual = ahorro_pensional_esperado / (años_esperados_de_vida * MESES_POR_AÑO)
    return pension_mensual
