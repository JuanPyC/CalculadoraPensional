import sys
import os

#os.path.abspath("src")
sys.path.append(os.path.abspath("C:/Users/USER/PycharmProjects/CalculadoraPensional/src"))
from Logic import CalculatorLogic
from Logic import Parameters
from Logic import Exceptions


def obtener_datos():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Debe ingresar un valor numérico para la edad.")

    while True:
        try:
            sexo = input("Ingrese su sexo (M para masculino o F para femenino): ").upper()
            if sexo not in ['M', 'F']:
                raise ValueError("Debe ingresar 'M' para masculino o 'F' para femenino.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            salario_actual = int(input("Ingrese su salario actual: "))
            break
        except ValueError:
            print("Debe ingresar un valor numérico para el salario actual.")

    while True:
        try:
            semanas_laboradas = int(input("Ingrese sus semanas laboradas a hoy: "))
            break
        except ValueError:
            print("Debe ingresar un valor numérico para las semanas laboradas.")

    while True:
        try:
            ahorro_pensional_a_hoy = int(input("Ingrese su ahorro pensional a hoy: "))
            break
        except ValueError:
            print("Debe ingresar un valor numérico para el ahorro pensional a hoy.")

    while True:
        try:
            rentabilidad_promedio = float(input("Ingrese la rentabilidad promedio del fondo (debe ser mayor a 0 y menor a 3): "))
            if not 0 < rentabilidad_promedio < 3:
                raise ValueError("La rentabilidad promedio debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            tasa_administracion = float(input("Ingrese la tasa de administración del fondo (debe ser mayor a 0 y menor a 3): "))
            if not 0 < tasa_administracion < 3:
                raise ValueError("La tasa de administración debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)

    parametros = Parameters.ParametrosPension()  # ver si esta vaina está correctamente definida en CalculatorLogic
    parametros.edad = edad
    parametros.sexo = sexo
    parametros.salario_actual = salario_actual
    parametros.semanas_laboradas = semanas_laboradas
    parametros.rentabilidad_promedio = rentabilidad_promedio
    parametros.ahorro_pensional_a_hoy = ahorro_pensional_a_hoy
    parametros.tasa_administracion = tasa_administracion



    try:
        # Verificar si cumple con la edad mínima para pensionarse

        CalculatorLogic.verificarEdad(parametros.edad)

        # Calculpar el ahorro pensional esperado
        ahorro_pensional_esperado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)
        print(f"El ahorro pensional esperado es: {ahorro_pensional_esperado}")
        print(f"La pension esperada mensual es:{CalculatorLogic.calcularPensionEsperada(ahorro_pensional_esperado, sexo)}")

    except ValueError as the_error:
        print(f"El valor ingresado es incorrecto: {the_error}")
    except Exception as the_exception:
        print(f"No puede continuar, ocurrió un problema: {the_exception}")


def menu_principal():
    while True:
        print("\n--- Calculadora Pensional ---")
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


menu_principal()
