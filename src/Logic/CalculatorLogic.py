import sys
import os

sys.path.append("src")
#sys.path.append(os.path.abspath("C:/Users/USER/PycharmProjects/CalculadoraPensional/src"))

"""Se importan los módulos necesarios desde la lógica de la calculadora
pensional y excepciones personalizadas"""

from Logic import Parameters
from Logic import Exceptions

"""Función para verificar que la edad ingresada esté dentro de un rango aceptable"""


def verificarEdad(edad):
    if edad < 18 or edad > 115:
        raise Exceptions.EdadError(f"Su edad, la cual es: {edad}, debe ser mayor a 18 y menor a 115")


"""Función para verificar que el salario actual sea válido"""


def verificarSalarioActual(salario_actual):
    if salario_actual < 0:
        raise Exceptions.SalarioActualNegativoError(f"Su salario, el cual es: {salario_actual}, debe ser mayor a 0")


""" Función para verificar que las semanas laboradas sean positivas"""


def verificarSemanasLaboradas(semanas_laboradas):
    if semanas_laboradas < 0:
        raise Exceptions.SemanasLaboradasNegativasError(
            f"Las semanas laboradas, las cuales son: {semanas_laboradas}, deben ser mayores a 0")


""" Función para verificar que la tasa de administración esté en un rango válido (0-3%)"""


def verificarTasaAdministracion(tasa_administracion):
    if tasa_administracion < 0 or tasa_administracion > 3:
        raise Exceptions.TasaAdministracionError(
            f"La tasa de administración, la cual es: {tasa_administracion}, debe ser mayor a 0 y menor a 3")


""" Función para verificar que el ahorro pensional no sea negativo"""


def verificarAhorroPensional(ahorro_pensional_a_hoy):
    if ahorro_pensional_a_hoy < 0:
        raise Exceptions.AhorroPensionalNegativoError(
            f"El ahorro pensional a hoy, el cual es: {ahorro_pensional_a_hoy}, debe ser mayor a 0")


""" Función para verificar que la rentabilidad promedio sea positiva"""


def verificarRentabilidadPromedio(rentabilidad_promedio):
    if rentabilidad_promedio < 0:
        raise Exceptions.RentabilidadPromedioNegativaError(
            f"La rentabilidad promedio, la cual es: {rentabilidad_promedio}, debe ser mayor que 0")


""" Función para calcular el ahorro pensional esperado"""


def calcularAhorroPensionalEsperado(parametros):
    # Se realizan las verificaciones para los parámetros ingresados
    verificarAhorroPensional(parametros.ahorro_pensional_a_hoy)
    verificarEdad(parametros.edad)
    verificarSalarioActual(parametros.salario_actual)
    verificarTasaAdministracion(parametros.tasa_administracion)
    verificarSemanasLaboradas(parametros.semanas_laboradas)

    # Determina la edad de retiro según el sexo (62 años para hombres, 57 para mujeres)
    edad_retiro = 62 if parametros.sexo == 'M' else 57
    años_restantes = edad_retiro - parametros.edad

    # Cálculo de las semanas restantes hasta la edad de retiro
    semanas_restantes = años_restantes * 52

    # Cálculo del ahorro pensional esperado usando una fórmula financiera
    ahorro_pensional_esperado = (
            parametros.ahorro_pensional_a_hoy * (1 + parametros.rentabilidad_promedio) ** años_restantes +
            parametros.salario_actual * semanas_restantes * (1 + parametros.rentabilidad_promedio) ** (
                    años_restantes - 1) / 52
    )

    return ahorro_pensional_esperado


""" Función para calcular la pensión esperada basada en el ahorro y el sexo"""


def calcularPensionEsperada(ahorro_pensional_esperado, sexo):
    # La expectativa de vida promedio es de 80 años
    if sexo == 'M':
        años_esperados_de_vida = 80 - 62
    else:
        años_esperados_de_vida = 80 - 57

    # Cálculo de la pensión mensual esperada usando el ahorro total y los años de vida esperados
    pension = pension_esperada_mensual(ahorro_pensional_esperado, años_esperados_de_vida)

    return pension


""" Función auxiliar para calcular la pensión mensual esperada"""


def pension_esperada_mensual(ahorro_pensional_esperado, años_esperados_de_vida):
    pension_mensual = ahorro_pensional_esperado / (años_esperados_de_vida * 12)
    return pension_mensual
