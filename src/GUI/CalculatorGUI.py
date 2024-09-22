import sys
sys.path.append(r"C:\Users\USER\PycharmProjects\CalculadoraPensional\src")
#sys.path.append("src")

from Logic import CalculatorLogic
from Logic import Parameters
from Logic import Exceptions

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup


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

        calcular_btn = Button(text="Calcular Pensión", font_size=30, on_press=self.calcular_pension_esperada)
        contenedor.add_widget(calcular_btn)
        contenedor.add_widget(Label())  # Este Label vacío ayuda a alinear

        return contenedor

    def calcular_pension_esperada(self, sender):
        try:
            edad = int(self.edad.text)
            sexo = self.sexo.text.upper()
            salario_actual = float(self.salario_actual.text)
            semanas_laboradas = int(self.semanas_laboradas.text)
            ahorro_pensional_a_hoy = float(self.ahorro_pensional_a_hoy.text)
            rentabilidad_promedio = float(self.rentabilidad_promedio.text)
            tasa_administracion = float(self.tasa_administracion.text)

            # Crear los parámetros para el cálculo
            params = Parameters(
                age=edad,
                gender=sexo,
                current_salary=salario_actual,
                weeks_worked=semanas_laboradas,
                current_pension_savings=ahorro_pensional_a_hoy,
                average_return=rentabilidad_promedio,
                management_rate=tasa_administracion
            )

            # Calcular el ahorro pensional esperado
            expected_savings = CalculatorLogic.calculate_expected_pension_savings(params)

            # Mostrar el resultado en una ventana emergente
            self.mostrar_popup(f"Ahorro pensional esperado: {expected_savings}")

        except ValueError:
            self.mostrar_popup("Error: Por favor ingresa valores numéricos válidos.")
        except Exceptions.EdadError as e:
            self.mostrar_popup(str(e))
        except Exceptions.SalarioActualNegativoError as e:
            self.mostrar_popup(str(e))
        except Exceptions.SemanasLaboradasNegativasError as e:
            self.mostrar_popup(str(e))
        except Exceptions.AhorroPensionalNegativoError as e:
            self.mostrar_popup(str(e))
        except Exceptions.TasaAdministracionError as e:
            self.mostrar_popup(str(e))
        except Exceptions.RentabilidadPromedioNegativaError as e:
            self.mostrar_popup(str(e))

    def mostrar_popup(self, mensaje):
        popup = Popup(title='Resultado',
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 400))
        popup.open()


if __name__ == "__main__":
    CalculatorApp().run()
