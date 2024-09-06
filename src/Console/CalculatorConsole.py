import sys
import os

# sys.path.append("src")
sys.path.append(os.path.abspath("C:/Users/USER/PycharmProjects/CalculadoraPensional/src"))

"""Importa los módulos necesarios: lógica de la calculadora pensional,
 parámetros y excepciones personalizadas."""

from Logic import CalculatorLogic
from Logic import Parameters
from Logic import Exceptions

""" Función para obtener los datos ingresados por el usuario"""


def obtener_datos():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))  # Se asegura que el dato ingresado sea un número entero
            break  # Si el ingreso es correcto, sale del ciclo
        except ValueError:
            print("Debe ingresar un valor numérico para la edad.")  # Muestra mensaje si el dato no es válido

    # Ciclo para obtener y validar el sexo
    while True:
        try:
            sexo = input("Ingrese su sexo (M para masculino o F para femenino): ").upper()  # Convierte a mayúsculas
            if sexo not in ['M', 'F']:  # Valida que el sexo sea 'M' o 'F'
                raise ValueError("Debe ingresar 'M' para masculino o 'F' para femenino.")
            break
        except ValueError as e:
            print(e)

    # Ciclo para obtener y validar el salario actual
    while True:
        try:
            salario_actual = int(input("Ingrese su salario actual: "))  # Asegura que sea un número entero
            break
        except ValueError:
            print("Debe ingresar un valor numérico para el salario actual.")

    # Ciclo para obtener y validar las semanas laboradas
    while True:
        try:
            semanas_laboradas = int(input("Ingrese sus semanas laboradas a hoy: "))  # Debe ser un número entero
            break
        except ValueError:
            print("Debe ingresar un valor numérico para las semanas laboradas.")

    # Ciclo para obtener y validar el ahorro pensional a la fecha
    while True:
        try:
            ahorro_pensional_a_hoy = int(input("Ingrese su ahorro pensional a hoy: "))  # Debe ser un número entero
            break
        except ValueError:
            print("Debe ingresar un valor numérico para el ahorro pensional a hoy.")

    # Ciclo para obtener y validar la rentabilidad promedio
    while True:
        try:
            rentabilidad_promedio = float(
                input("Ingrese la rentabilidad promedio del fondo (debe ser mayor a 0 y menor a 3): "))
            if not 0 < rentabilidad_promedio < 3:  # Valida que la rentabilidad esté en el rango válido
                raise ValueError("La rentabilidad promedio debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)

    # Ciclo para obtener y validar la tasa de administración del fondo
    while True:
        try:
            tasa_administracion = float(
                input("Ingrese la tasa de administración del fondo (debe ser mayor a 0 y menor a 3): "))
            if not 0 < tasa_administracion < 3:  # Verifica que esté dentro del rango válido
                raise ValueError("La tasa de administración debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)
    """ Se crea una instancia de la clase 'ParametrosPension'
    que almacena los valores ingresados"""

    parametros = Parameters.ParametrosPension()
    parametros.edad = edad
    parametros.sexo = sexo
    parametros.salario_actual = salario_actual
    parametros.semanas_laboradas = semanas_laboradas
    parametros.rentabilidad_promedio = rentabilidad_promedio
    parametros.ahorro_pensional_a_hoy = ahorro_pensional_a_hoy
    parametros.tasa_administracion = tasa_administracion

    try:

        CalculatorLogic.verificarEdad(parametros.edad)

        ahorro_pensional_esperado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        print(f"El ahorro pensional esperado es: {ahorro_pensional_esperado}")

        print(
            f"La pension esperada mensual es:{CalculatorLogic.calcularPensionEsperada(ahorro_pensional_esperado, sexo)}")

    # Maneja cualquier error de valor incorrecto ingresado por el usuario
    except ValueError as the_error:
        print(f"El valor ingresado es incorrecto: {the_error}")

    # Maneja cualquier otro tipo de error general
    except Exception as the_exception:
        print(f"No puede continuar, ocurrió un problema: {the_exception}")


""" Función que muestra el menú interactivo del programa"""


def menu_principal():
    while True:
        print("\n--- Calculadora Pensional ---")  # Título del menú
        print("1. Ingresar datos")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            obtener_datos()
        elif opcion == "2":
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print("Opción no válida, por favor intente de nuevo.")


# Inicia el programa mostrando el menú principal
menu_principal()
