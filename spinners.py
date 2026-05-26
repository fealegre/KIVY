# ─────────────────────────────────────────────────────────
# spinners.py — Lista desplegable (Spinner) en Kivy
# ─────────────────────────────────────────────────────────
# Muestra cómo crear un Spinner, que es un menú desplegable donde
# el usuario puede seleccionar una opción de una lista predefinida.
# Conceptos clave: Spinner, text, values, size_hint_y, height
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana
from kivy.core.window import Window

# BoxLayout organiza los widgets en una dirección
from kivy.uix.boxlayout import BoxLayout

# Spinner: lista desplegable (similar a un <select> en HTML o ComboBox)
from kivy.uix.spinner import Spinner


class SpinnerApp(App):

    def build(self):
        # Título de la ventana
        self.title = "Lista desplegable Kivy"

        # Tamaño inicial de la ventana
        Window.size = (250, 350)

        # Layout vertical con márgenes internos y espacio entre widgets
        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Tupla de opciones que aparecerán en el menú desplegable.
        # Usamos tupla () en lugar de lista [] porque no vamos a modificar las opciones.
        options = ("Kivy", "PyQt6", "PySide6", "Tkinter")

        # Texto que se muestra cuando no hay ninguna opción seleccionada
        base_text = "Framework GUI favorito"

        # Creamos el Spinner (lista desplegable):
        # - text: texto visible por defecto (antes de seleccionar algo).
        # - values: tupla o lista con las opciones disponibles.
        # - size_hint_y=None: desactiva el tamaño proporcional vertical,
        #   permitiendo fijar una altura fija con height.
        # - height=100: altura fija de 100 píxeles para el spinner.
        spinner = Spinner(
            text=base_text,
            values=options,
            size_hint_y=None,
            height=100,
        )

        # Agregamos el spinner al layout
        root.add_widget(spinner)

        return root


# Iniciamos la aplicación
SpinnerApp().run()