from kivy.app import App


from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

import sys
sys.path.append("src")

#logica para la implementacion de la calculadora ´pensional

from Logic import CalculatorLogic
from Logic import Parameters
from Logic import Exceptions


class CalculatorApp(App):
    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=20)

        contenedor.add.widget(Label(text="Ingresa tu edad"))
        contenedor = TextInput(font_zise=30)
        contenedor.add_widget(Label(self.edad))


        contenedor.add.widget(Label(text="Ingresa tu sexo (M ó F)"))
        contenedor = TextInput(font_zise=30)
        contenedor.add_widget(Label(self.sexo))


        contenedor.add.widget(Label(text="Ingresa tu salario actual"))
        contenedor = TextInput(font_zise=30)
        contenedor.add_widget(Label(self.salario_actual))


        contenedor.add.widget(Label(text="Ingresa tus semanas laboradas"))
        contenedor = TextInput(font_zise=30)
        contenedor.add_widget(Label(self.semanas_laboradas))


        contenedor.add.widget(Label(text="Ingresa tu ahorro pensional a hoy"))
        contenedor = TextInput(font_zise=30)
        contenedor.add_widget(Label(self.ahorro_pensional_a_hoy))


        contenedor.add.widget(Label(text="Ingresa tu rentabilidad promedio:"))
        contenedor = TextInput(font_zise=30)
        contenedor.add_widget(Label(self.rentabilidad_promedio))


        contenedor.add.widget(Label(text="ingresa tu tasa de administracion"))
        contenedor = TextInput(font_zise=30)
        contenedor.add_widget(Label(self.tasa_administracion))

    def CalculatorPension(self):
        pass

    def calcular_pension_esperada(self, sender):
        pass

    def validar(self):
        pass


if __name__ == "__main__":
    CalculatorApp().run()