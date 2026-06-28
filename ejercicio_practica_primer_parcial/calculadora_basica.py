"""
Ejercicio 3: Calculadora de Dos Operandos
Nivel: Básico
Descripción: Calculadora con dos entradas y cuatro operaciones básicas.
Valida entradas inválidas y división por cero.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculadoraLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Configuramos el layout principal como una columna vertical
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 12

        # Título de la aplicación
        self.add_widget(Label(
            text="Calculadora",
            font_size=28,
            bold=True,
            size_hint_y=None,
            height=50,
        ))

        # Contenedor horizontal para las dos entradas de números
        fila_entradas = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=55,
            spacing=10,
        )
        self.input_a = TextInput(
            hint_text="Número A",
            multiline=False,
            input_filter="float",  # Solo permite caracteres válidos de número decimal
            font_size=20,
        )
        self.input_b = TextInput(
            hint_text="Número B",
            multiline=False,
            input_filter="float",
            font_size=20,
        )
        fila_entradas.add_widget(self.input_a)
        fila_entradas.add_widget(self.input_b)
        self.add_widget(fila_entradas)

        # Cuatro botones de operación colocados en una grilla de 2 columnas
        grilla = GridLayout(cols=2, size_hint_y=None, height=130, spacing=8)

        operaciones = [
            ("+ Sumar",     self.sumar,       (0.2, 0.6, 0.9, 1)),
            ("- Restar",    self.restar,      (0.6, 0.4, 0.9, 1)),
            ("* Multiplicar", self.multiplicar, (0.2, 0.75, 0.5, 1)),
            ("/ Dividir",   self.dividir,     (0.9, 0.6, 0.1, 1)),
        ]

        for texto, handler, color in operaciones:
            btn = Button(
                text=texto,
                background_color=color,
                font_size=16,
            )
            btn.bind(on_press=handler)  # Llama al método correspondiente al pulsar
            grilla.add_widget(btn)

        self.add_widget(grilla)

        # Label de resultado
        self.label_resultado = Label(
            text="Resultado: —",
            font_size=26,
            bold=True,
            color=(1, 1, 1, 1),
        )
        self.add_widget(self.label_resultado)

    def _obtener_numeros(self):
        """Lee y convierte los textos de entrada en dos números flotantes."""
        texto_a = self.input_a.text.strip()
        texto_b = self.input_b.text.strip()

        # Validación básica: ambos campos deben tener contenido
        if not texto_a or not texto_b:
            raise ValueError("Ambos campos son obligatorios.")

        a = float(texto_a)
        b = float(texto_b)
        return a, b

    def _mostrar_resultado(self, valor):
        # Si el resultado es un float sin parte decimal significativa, lo mostramos como entero
        if isinstance(valor, float) and valor.is_integer():
            self.label_resultado.text = f"Resultado: {int(valor)}"
        else:
            # Si tiene decimales, formateamos hasta 4 cifras y quitamos ceros sobrantes
            self.label_resultado.text = f"Resultado: {valor:.4f}".rstrip("0").rstrip(".")

        # Color verde para resultados válidos
        self.label_resultado.color = (0.3, 1, 0.5, 1)

    def _mostrar_error(self, mensaje):
        # Muestra un mensaje de error en rojo
        self.label_resultado.text = f"⚠️ {mensaje}"
        self.label_resultado.color = (1, 0.4, 0.4, 1)

    def sumar(self, _):
        try:
            a, b = self._obtener_numeros()
            self._mostrar_resultado(a + b)
        except ValueError as e:
            self._mostrar_error(str(e))

    def restar(self, _):
        try:
            a, b = self._obtener_numeros()
            self._mostrar_resultado(a - b)
        except ValueError as e:
            self._mostrar_error(str(e))

    def multiplicar(self, _):
        try:
            a, b = self._obtener_numeros()
            self._mostrar_resultado(a * b)
        except ValueError as e:
            self._mostrar_error(str(e))

    def dividir(self, _):
        try:
            a, b = self._obtener_numeros()
            if b == 0:
                self._mostrar_error("No se puede dividir por cero.")
                return
            self._mostrar_resultado(a / b)
        except ValueError as e:
            self._mostrar_error(str(e))


class CalculadoraApp(App):
    def build(self):
        # Construye y retorna el layout principal de la aplicación
        return CalculadoraLayout()


if __name__ == "__main__":
    # Inicia la aplicación Kivy
    CalculadoraApp().run()