# ─────────────────────────────────────────────────────────
# text_inputs.py — Campos de texto en Kivy
# ─────────────────────────────────────────────────────────
# Muestra cómo crear campos de entrada de texto (TextInput) donde
# el usuario puede escribir. Incluye texto de sugerencia (hint_text)
# y configuración de línea única.
# Conceptos clave: TextInput, hint_text, multiline
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana
from kivy.core.window import Window

# BoxLayout organiza los widgets en una dirección
from kivy.uix.boxlayout import BoxLayout

# TextInput: campo de entrada donde el usuario puede escribir texto
from kivy.uix.textinput import TextInput


class TextInputApp(App):

    def build(self):
        # Título de la ventana
        self.title = "Campos de texto Kivy"

        # Tamaño inicial de la ventana
        Window.size = (250, 180)

        # Layout vertical: los campos se apilan de arriba hacia abajo
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Creamos tres campos de texto, uno para cada dato solicitado.
        # - hint_text: texto de sugerencia que aparece cuando el campo está vacío
        #   (similar a "placeholder" en HTML). Desaparece al empezar a escribir.
        # - multiline=False: el campo es de una sola línea (no permite saltos de línea).
        #   Ideal para nombres, usuarios y contraseñas.
        for text in ["Nombre", "Usuario", "Contraseña"]:
            entry = TextInput(
                hint_text=text,
                multiline=False,
            )
            layout.add_widget(entry)

        return layout


# Iniciamos la aplicación
TextInputApp().run()