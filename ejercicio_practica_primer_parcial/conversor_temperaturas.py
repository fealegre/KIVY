"""
Ejercicio 4: Conversor de Temperaturas
Nivel: Medio
Descripcion: Convierte entre Celsius y Fahrenheit.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


class ConversorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 25
        self.spacing = 15

        self.add_widget(Label(
            text="Conversor de Temperaturas",
            font_size=26,
            bold=True,
            size_hint_y=None,
            height=55,
        ))

        self.input_temp = TextInput(
            hint_text="Ingrese temperatura",
            multiline=False,
            input_filter="float",
            font_size=22,
            size_hint_y=None,
            height=55,
        )
        self.add_widget(self.input_temp)

        grilla = GridLayout(cols=2, size_hint_y=None, height=65, spacing=10)

        btn_cf = Button(
            text="Celsius  ->  Fahrenheit",
            background_color=(0.9, 0.4, 0.2, 1),
            font_size=16,
        )
        btn_cf.bind(on_press=self.convertir_cf)

        btn_fc = Button(
            text="Fahrenheit  ->  Celsius",
            background_color=(0.2, 0.5, 0.9, 1),
            font_size=16,
        )
        btn_fc.bind(on_press=self.convertir_fc)

        grilla.add_widget(btn_cf)
        grilla.add_widget(btn_fc)
        self.add_widget(grilla)

        self.label_resultado = Label(
            text="---",
            font_size=52,
            bold=True,
            color=(1, 0.9, 0.3, 1),
        )
        self.add_widget(self.label_resultado)

        self.label_formula = Label(
            text="",
            font_size=15,
            color=(0.6, 0.6, 0.6, 1),
        )
        self.add_widget(self.label_formula)

    def _leer_temperatura(self):
        texto = self.input_temp.text.strip()
        if not texto:
            raise ValueError("Ingrese un valor de temperatura.")
        return float(texto)

    def _mostrar_error(self, msg):
        self.label_resultado.text = "[!]"
        self.label_formula.text = msg
        self.label_resultado.color = (1, 0.4, 0.4, 1)

    def convertir_cf(self, _):
        try:
            c = self._leer_temperatura()
            f = celsius_a_fahrenheit(c)
            self.label_resultado.text = "{:.2f} F".format(f)
            self.label_formula.text = "{} C x 9/5 + 32 = {:.2f} F".format(c, f)
            self.label_resultado.color = (0.9, 0.4, 0.2, 1)
        except ValueError as e:
            self._mostrar_error(str(e))

    def convertir_fc(self, _):
        try:
            f = self._leer_temperatura()
            c = fahrenheit_a_celsius(f)
            self.label_resultado.text = "{:.2f} C".format(c)
            self.label_formula.text = "({} F - 32) x 5/9 = {:.2f} C".format(f, c)
            self.label_resultado.color = (0.2, 0.7, 0.9, 1)
        except ValueError as e:
            self._mostrar_error(str(e))


class ConversorApp(App):
    def build(self):
        return ConversorLayout()


if __name__ == "__main__":
    ConversorApp().run()