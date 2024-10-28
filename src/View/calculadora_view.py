class CalculadoraPensionalView:
    def mostrar_resultado(self, resultado):
        print("Resultado:", resultado)

    def mostrar_error(self, mensaje):
        print("Error:", mensaje)

    def solicitar_datos_usuario(self):
        nombre = input("Ingrese el nombre: ")

        while True:
            try:
                edad = int(input("Ingrese la edad (entre 18 y 115): "))
                if 18 <= edad <= 115:
                    break
                else:
                    print("La edad debe estar entre 18 y 115.")
            except ValueError:
                print("Por favor ingrese un número entero para la edad.")

        while True:
            try:
                salario_actual = float(input("Ingrese el salario actual (debe ser positivo): "))
                if salario_actual >= 0:
                    break
                else:
                    print("El salario actual debe ser un valor positivo.")
            except ValueError:
                print("Por favor ingrese un número válido para el salario actual.")

        while True:
            try:
                semanas_laboradas = int(input("Ingrese las semanas laboradas (debe ser un número positivo): "))
                if semanas_laboradas >= 0:
                    break
                else:
                    print("Las semanas laboradas deben ser un valor positivo.")
            except ValueError:
                print("Por favor ingrese un número entero para las semanas laboradas.")

        while True:
            try:
                ahorro_pensional = float(input("Ingrese el ahorro pensional (debe ser positivo): "))
                if ahorro_pensional >= 0:
                    break
                else:
                    print("El ahorro pensional debe ser un valor positivo.")
            except ValueError:
                print("Por favor ingrese un número válido para el ahorro pensional.")

        while True:
            try:
                tasa_administracion = float(input("Ingrese la tasa de administración (entre 0 y 3): "))
                if 0 <= tasa_administracion <= 3:
                    break
                else:
                    print("La tasa de administración debe estar entre 0 y 3.")
            except ValueError:
                print("Por favor ingrese un número válido para la tasa de administración.")

        while True:
            try:
                rentabilidad_promedio = float(input("Ingrese la rentabilidad promedio (entre 0 y 3): "))
                if 0 <= rentabilidad_promedio <= 3:
                    break
                else:
                    print("La rentabilidad promedio debe estar entre 0 y 3.")
            except ValueError:
                print("Por favor ingrese un número válido para la rentabilidad promedio.")

        while True:
            genero = input("Ingrese el género (M/F): ").upper()
            if genero in ('M', 'F'):
                break
            else:
                print("Por favor ingrese 'M' para masculino o 'F' para femenino.")

        return (nombre, edad, salario_actual, semanas_laboradas, ahorro_pensional, tasa_administracion, rentabilidad_promedio, genero)
