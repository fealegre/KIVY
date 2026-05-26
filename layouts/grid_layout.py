# ─────────────────────────────────────────────────────────
# grid_layout.py — Disposición en cuadrícula con GridLayout
# ─────────────────────────────────────────────────────────
# Muestra cómo usar GridLayout para organizar widgets en una grilla
# con un número fijo de columnas. Los widgets se colocan de izquierda
# a derecha, fila por fila.
# Conceptos clave: GridLayout, cols, padding, spacing
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana
from kivy.core.window import Window

# Button: botón interactivo
from kivy.uix.button import Button

# GridLayout: layout que organiza widgets en una cuadrícula (grilla).
# A diferencia de BoxLayout (una sola dirección), GridLayout distribuye
# los widgets en filas y columnas, como una tabla.
from kivy.uix.gridlayout import GridLayout


class GridLayoutApp(App):

    def build(self):
        # Título de la ventana
        self.title = "Disposición en cuadrícula Kivy"

        # Tamaño inicial de la ventana
        Window.size = (300, 300)

        # GridLayout con 4 columnas:
        # - cols=4: los widgets se colocan en 4 columnas. Cuando se llena
        #   una fila (4 widgets), el siguiente pasa a la fila siguiente.
        # - padding=20: margen interno de 20 píxeles.
        # - spacing=10: espacio de 10 píxeles entre widgets (horizontal y vertical).
        root = GridLayout(cols=4, padding=20, spacing=10)

        # Creamos 8 botones numerados del 1 al 8.
        # Con 4 columnas, se distribuyen en 2 filas:
        #   Fila 1: [1] [2] [3] [4]
        #   Fila 2: [5] [6] [7] [8]
        for index in range(8):
            root.add_widget(Button(text=f"{index+1}"))

        return root


# Iniciamos la aplicación
GridLayoutApp().run()