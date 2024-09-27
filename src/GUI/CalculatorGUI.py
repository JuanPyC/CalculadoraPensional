import sys
sys.path.append(r"C:\Users\USER\PycharmProjects\CalculadoraPensional\src")
#sys.path.append("src")

from Logic import CalculatorLogic
from Logic.Parameters import ParametrosPension
from Logic import Exceptions

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import P

class CalculatorApp(App):
    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        contenedor.add_widget(Label(text="Ingresa tu edad"))
        self.edad = TextInput(font_size=30)
        contenedor.add_widget(self.edad)

        contenedor.add_widget(Label(text="Ingresa tu sexo (M ó F)"))
        self.sexo = TextInput(font_size=30)
        contenedor.add_widget(self.sexo)

        contenedor.add_widget(Label(text="Ingresa tu salario actual"))
        self.salario_actual = TextInput(font_size=30)
        contenedor.add_widget(self.salario_actual)

        contenedor.add_widget(Label(text="Ingresa tus semanas laboradas"))
        self.semanas_laboradas = TextInput(font_size=30)
        contenedor.add_widget(self.semanas_laboradas)

        contenedor.add_widget(Label(text="Ingresa tu ahorro pensional a hoy"))
        self.ahorro_pensional_a_hoy = TextInput(font_size=30)
        contenedor.add_widget(self.ahorro_pensional_a_hoy)

        contenedor.add_widget(Label(text="Ingresa tu rentabilidad promedio"))
        self.rentabilidad_promedio = TextInput(font_size=30)
        contenedor.add_widget(self.rentabilidad_promedio)

        contenedor.add_widget(Label(text="Ingresa tu tasa de administración"))
        self.tasa_administracion = TextInput(font_size=30)
        contenedor.add_widget(self.tasa_administracion)

        # Crear el Label donde se mostrará la pensión esperada
        self.resultado_label = Label(text="Pensión esperada: ")
        contenedor.add_widget(self.resultado_label)
        contenedor.add_widget(Label())  # Espacio vacío

        calcular_btn = Button(text="Calcular Pensión", font_size=30, on_press=self.calcular_pension_esperada)
        contenedor.add_widget(calcular_btn)
        contenedor.add_widget(Label())  # Espacio vacío

        return contenedor

    def calcular_pension_esperada(self, sender):
        try:
            # Capturar los valores de los inputs
            edad = int(self.edad.text)
            sexo = self.sexo.text.upper()
            salario_actual = float(self.salario_actual.text)
            semanas_laboradas = int(self.semanas_laboradas.text)
            ahorro_pensional_a_hoy = float(self.ahorro_pensional_a_hoy.text)
            rentabilidad_promedio = float(self.rentabilidad_promedio.text)
            tasa_administracion = float(self.tasa_administracion.text)

            # Se crea la instancia de ParametrosPension
            parameters = ParametrosPension()
            parameters.age = edad
            parameters.gender = sexo
            parameters.current_salary = salario_actual
            parameters.weeks_worked = semanas_laboradas
            parameters.current_pension_savings = ahorro_pensional_a_hoy
            parameters.average_return = rentabilidad_promedio
            parameters.management_rate = tasa_administracion

            # Calcular el ahorro pensional esperado
            expected_savings = CalculatorLogic.calculate_expected_pension_savings(parameters)

            # Mostrar el resultado en la interfaz
            self.resultado_label.text = f"Pensión esperada: {expected_savings:.2f} "

        except ValueError:
            # Si hay un error en la conversión de algún campo, mostrar un popup de error
            self.mostrar_popup("Error: Asegúrate de ingresar números válidos en los campos.")
        except Exceptions.EdadError:
            self.mostrar_popup("Error: La edad ingresada no es válida.")
        except Exceptions.SalarioActualNegativoError:
            self.mostrar_popup("Error: El salario actual no puede ser negativo.")
        except Exceptions.SemanasLaboradasNegativasError:
            self.mostrar_popup("Error: Las semanas laboradas no pueden ser negativas.")
        except Exceptions.AhorroPensionalNegativoError:
            self.mostrar_popup("Error: El ahorro pensional no puede ser negativo.")
        except Exceptions.TasaAdministracionError:
            self.mostrar_popup("Error: La tasa de administración ingresada no es válida.")
        except Exceptions.RentabilidadPromedioNegativaError:
            self.mostrar_popup("Error: La rentabilidad promedio ingresada no es válida.")
        except Exception as e:
            self.mostrar_popup(f"Error inesperado: {str(e)}")

    def mostrar_popup(self, mensaje):
        # Mostrar un popup con un mensaje
        popup = Popup(title='Error',
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 400))
        popup.open()


if __name__ == "__main__":
    CalculatorApp().run()
