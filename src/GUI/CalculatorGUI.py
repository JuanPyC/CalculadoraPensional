from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

# lógica para la implementación de la calculadora pensional
from Logic import CalculatorLogic
from Logic import Parameters
from Logic import Exceptions


class CalculatorApp(App):
    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        # Corrigiendo el uso de add_widget y el TextInput
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

        # Aquí podrías agregar un botón para calcular la pensión, por ejemplo
        calcular_btn = Button(text="Calcular Pensión", font_size=30, on_press=self.calcular_pension_esperada)
        contenedor.add_widget(calcular_btn)

        return contenedor

    def calcular_pension_esperada(self, sender):
        # Aquí puedes implementar la lógica para calcular la pensión
        pass

    def validar(self):
        # Aquí puedes implementar la validación de los datos de entrada
        pass


if __name__ == "__main__":
    CalculatorApp().run()
