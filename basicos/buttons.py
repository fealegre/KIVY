# ─────────────────────────────────────────────────────────
# buttons.py — Botones en Kivy
# ─────────────────────────────────────────────────────────
# Muestra cómo crear varios botones dentro de un BoxLayout vertical.
# Conceptos clave: Button, BoxLayout, orientación, padding, spacing
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana de la app
from kivy.core.window import Window

# BoxLayout organiza los widgets en una sola dirección (vertical u horizontal)
from kivy.uix.boxlayout import BoxLayout

# Button es el widget interactivo que responde a clics
from kivy.uix.button import Button


class ButtonsApp(App):

    def build(self):
        # Título que aparece en la barra de la ventana
        self.title = "Botones Kivy"

        # Configuramos el tamaño inicial de la ventana (ancho, alto) en píxeles
        Window.size = (200, 200)

        # Creamos un layout vertical: los widgets se apilan de arriba hacia abajo.
        # - padding=20: margen interno de 20 píxeles alrededor del layout.
        # - spacing=10: espacio de 10 píxeles entre cada widget hijo.
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Creamos un botón por cada texto en la lista y lo agregamos al layout.
        # Cada Button se crea con su texto y se añade con add_widget().
        for text in ["Ok", "Cancelar", "Aplicar", "Sí", "No", "Cerrar"]:
            button = Button(text=text)
            layout.add_widget(button)

        # El layout con todos los botones es el widget raíz de la app
        return layout


# Iniciamos la aplicación
ButtonsApp().run()