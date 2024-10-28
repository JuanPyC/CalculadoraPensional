import sys
import os

sys.path.append("src")


"""
Imports the necessary modules: pension calculator logic,
parameters, and custom exceptions.
"""

from src.Model import calculadora_model
from Model import Parameters
from Model import Exceptions

def obtener_datos():
    """
    Función para obtener los datos ingresados por el usuario
    """

    while True:
        try:
            age = int(input("Ingrese su edad: "))  # Se asegura que el dato ingresado sea un número entero
            break  # Si el ingreso es correcto, sale del ciclo
        except ValueError:
            print("Debe ingresar un valor numérico para la edad.")  # Muestra mensaje si el dato no es válido

    # Ciclo para obtener y validar el sexo
    while True:
        try:
            gender = input("Ingrese su sexo (M para masculino o F para femenino): ").upper()  # Convierte a mayúsculas
            if gender not in ['M', 'F']:  # Valida que el sexo sea 'M' o 'F'
                raise ValueError("Debe ingresar 'M' para masculino o 'F' para femenino.")
            break
        except ValueError as e:
            print(e)

    # Ciclo para obtener y validar el salario actual
    while True:
        try:
            current_salary = int(input("Ingrese su salario actual: "))
            break
        except ValueError:
            print("Debe ingresar un valor numérico para el salario actual.")

    # Ciclo para obtener y validar las semanas laboradas
    while True:
        try:
            weeks_worked = int(input("Ingrese sus semanas laboradas a hoy: "))
            break
        except ValueError:
            print("Debe ingresar un valor numérico para las semanas laboradas.")

    # Ciclo para obtener y validar el ahorro pensional a la fecha
    while True:
        try:
            current_pension_savings = int(input("Ingrese su ahorro pensional a hoy: "))
            break
        except ValueError:
            print("Debe ingresar un valor numérico para el ahorro pensional a hoy.")

    # Ciclo para obtener y validar la rentabilidad promedio
    while True:
        try:
            average_return = float(
                input("Ingrese la rentabilidad promedio del fondo (debe ser mayor a 0 y menor a 3): "))

            RENTABILIDAD_PROMEDIO_MINIMO = 0
            RENTABILIDAD_PROMEDIO_MAXIMO = 3

            if not RENTABILIDAD_PROMEDIO_MINIMO < average_return < RENTABILIDAD_PROMEDIO_MAXIMO:
                raise ValueError("La rentabilidad promedio debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)

    # Ciclo para obtener y validar la tasa de administración del fondo
    while True:
        try:
            management_rate = float(
                input("Ingrese la tasa de administración del fondo (debe ser mayor a 0 y menor a 3): "))

            TASA_ADMINISTRACION_MINIMA = 0
            TASA_ADMINISTRACION_MAXIMA = 3

            if not TASA_ADMINISTRACION_MINIMA < management_rate < TASA_ADMINISTRACION_MAXIMA:
                raise ValueError("La tasa de administración debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)

    """
    Se crea una instancia de la clase 'ParametrosPension'
    que almacena los valores ingresados
    """

    parameters = Parameters.ParametrosPension()
    parameters.age = age
    parameters.gender = gender
    parameters.current_salary = current_salary
    parameters.weeks_worked = weeks_worked
    parameters.current_pension_savings = current_pension_savings
    parameters.average_return = average_return
    parameters.management_rate = management_rate

    try:
        calculadora_model.verify_age(parameters.age)

        expected_pension_savings = calculadora_model.calculate_expected_pension_savings(parameters)
        print(f"El ahorro pensional esperado es: {expected_pension_savings}")

        print(
            f"La pensión esperada mensual es: {calculadora_model.calculate_expected_pension(expected_pension_savings, gender)}")

    # Maneja cualquier error de valor incorrecto ingresado por el usuario

    except ValueError as the_error:
        print(f"El valor ingresado es incorrecto: {the_error}")

    # Maneja cualquier otro tipo de error general
    except Exception as the_exception:
        print(f"No puede continuar, ocurrió un problema: {the_exception}")


def main_menu():
    """
    Función que muestra el menú interactivo del programa
    """

    while True:
        print("\n--- Calculadora Pensional ---")  # Título del menú
        print("1. Ingresar datos")
        print("2. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            obtener_datos()
        elif option == "2":
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print("Opción no válida, por favor intente de nuevo.")


# Inicia el programa mostrando el menú principal
main_menu()
