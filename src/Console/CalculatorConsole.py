"""import sys
sys.path.append("CalculadoraPensional/src")
import src.Logic.CalculatorLogic as CalculatorLogic
from src.Logic.CalculatorLogic import Parameters

"""


def menu_principal():
    while True:
        print("\n--- Calculadora de Pensión ---")
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
            estado_civil = input("Ingrese su estado civil (C para casad@ o S para solter@): ").upper()
            if estado_civil not in ['C', 'S']:
                raise ValueError("Debe ingresar 'C' para casad@ o 'S' para solter@.")
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
            rentabilidad_promedio = float(
                input("Ingrese la rentabilidad promedio del fondo (debe ser mayor a 0 y menor a 3): "))
            if not 0 < rentabilidad_promedio < 3:
                raise ValueError("La rentabilidad promedio debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            tasa_administracion = float(
                input("Ingrese la tasa de administración del fondo (debe ser mayor a 0 y menor a 3): "))
            if not 0 < tasa_administracion < 3:
                raise ValueError("La tasa de administración debe ser mayor a 0 y menor a 3.")
            break
        except ValueError as e:
            print(e)

    parametros = ParametrosPension()
    parametros.edad = edad
    parametros.salario_actual = salario_actual
    parametros.semanas_laboradas = semanas_laboradas
    parametros.rentabilidad_promedio = rentabilidad_promedio
    parametros.ahorro_pensional_a_hoy = ahorro_pensional_a_hoy
    parametros.tasa_administracion = tasa_administracion
    parametros.edad_pension_total = edad_pension_total

    while True:
        try:
            hereda_pension = input("Ingrese 'S' si desea heredar su pensión o 'N' si no: ").upper()
            if hereda_pension == "S" and estado_civil == "C":
                hereda = 1
            elif hereda_pension == "S" and estado_civil == "S":
                hereda = 0
            elif hereda_pension == "N":
                hereda = 0
            break
        except ValueError:
            print("Debe ingresar 'S' si desea heredar su pensión o 'N' si no.")

    try:
        AhorroPensionalEsperado = CalculatorLogic.calcularAhorroPensionalEsperado(parametros)

        print(f"El ahorro pensional esperado es: {AhorroPensionalEsperado}")

        if AhorroPensionalEsperado:
            if sexo == "M":
                esperanza_vida = 80  # Esperanza de vida para hombres en Colombia
            elif sexo == "F":
                esperanza_vida = 85  # Esperanza de vida para mujeres en Colombia

            PensionEsperadaTotal = CalculatorLogic.calcPensionEsperada(
                AhorroPensionalEsperado, esperanza_vida, edad_pension_total, hereda, tasa_administracion)

            print(f"La pensión esperada es: {PensionEsperadaTotal}")

    except ValueError as the_error:
        print(f"El valor ingresado es incorrecto: {the_error}")
    except Exception as the_exception:
        # Maneja las excepciones controladas
        print(f"No puede continuar, ocurrió un problema: {the_exception}")
