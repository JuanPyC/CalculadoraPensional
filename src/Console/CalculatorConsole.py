import sys
sys.path.append("CalculadoraPensional/src")
import src.Logic.CalculatorLogic as CalculatorLogic
from src.Logic.CalculatorLogic import Parameters


while True:
    print("_____Calcule su Pension_____")
    break


edad = int(input("Ingrese su Edad: "))
salario_actual = float(input("Ingrese su Salario Actual: "))
ahorro_pensional = float(input("Ingrese su Ahorro Pensional: "))
rentabilidad_promedio = float(input("Ingrese la Rentabilidad Promedio del Fondo (debe ser entre uno y dos): "))
tasa_administracion = float(input("Ingrese la Tasa de Administración (debe ser entre uno y dos): "))

try:
    resultado = CalculatorLogic.calcularAhorroPensionalEsperado(CalculatorLogic.calcularAhorroPensionalEsperado)
    print(f"El valor de la cuota mensual es de: {resultado}")

except Exception as el_error:
    print("Hubo un Error")
    print(str(el_error))
