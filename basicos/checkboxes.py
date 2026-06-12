# ─────────────────────────────────────────────────────────
# checkboxes.py — Casillas de verificación en Kivy
# ─────────────────────────────────────────────────────────
# Muestra cómo crear casillas de verificación (CheckBox) acompañadas
# de etiquetas (Label) dentro de filas horizontales.
# Conceptos clave: CheckBox, Label, BoxLayout anidado, texture_update,
#                  size_hint_x, Window.clearcolor
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar tamaño y color de fondo de la ventana
from kivy.core.window import Window

# BoxLayout organiza los widgets en fila o columna
from kivy.uix.boxlayout import BoxLayout

# CheckBox: casilla de verificación (marcada/desmarcada)
from kivy.uix.checkbox import CheckBox

# Label: etiqueta de texto no editable
from kivy.uix.label import Label


class CheckBoxApp(App):

    def build(self):
        # Título de la ventana
        self.title = "Botones de opción Kivy"

        # Tamaño inicial de la ventana
        Window.size = (250, 150)

        # Color de fondo de la ventana en formato RGBA (Rojo, Verde, Azul, Alfa).
        # (1, 1, 1, 1) = blanco puro. Los valores van de 0.0 a 1.0.
        Window.clearcolor = (1, 1, 1, 1)

        # Lista de textos para las opciones que el usuario puede marcar
        options = [
            "Recibir notificaciones",
            "Aceptar términos y condiciones",
            "Suscribirse al boletín",
        ]

        # Layout principal vertical: las filas se apilan de arriba hacia abajo
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Para cada opción, creamos una fila horizontal con CheckBox + Label
        for option in options:
            # Cada fila es un BoxLayout horizontal (los widgets van de izquierda a derecha)
            row = BoxLayout(orientation="horizontal", spacing=8)

            # CheckBox: size_hint_x=None desactiva el tamaño proporcional,
            # permitiendo fijar un ancho fijo con width=30 píxeles.
            row.add_widget(CheckBox(size_hint_x=None, width=30))

            # Label con texto de la opción y color negro (0,0,0,1) para
            # que sea visible sobre el fondo blanco.
            label = Label(
                text=option,
                color=(0, 0, 0, 1),  # Texto en color negro
                size_hint_x=None,     # Desactivamos tamaño proporcional
            )

            # texture_update() recalcula la textura del texto (su tamaño real).
            # Es necesario llamarlo antes de leer texture_size para que
            # los valores estén actualizados.
            label.texture_update()

            # Asignamos el ancho del label según el ancho real del texto renderizado.
            # texture_size[0] = ancho en píxeles del texto dibujado.
            label.width = label.texture_size[0]

            # Agregamos el label a la fila, y la fila al layout principal
            row.add_widget(label)
            layout.add_widget(row)

        return layout


# Iniciamos la aplicación
CheckBoxApp().run()