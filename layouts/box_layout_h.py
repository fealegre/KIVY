# ─────────────────────────────────────────────────────────
# box_layout_h.py — Disposición horizontal con BoxLayout
# ─────────────────────────────────────────────────────────
# Muestra cómo usar BoxLayout con orientación horizontal:
# los widgets se colocan de izquierda a derecha.
# Conceptos clave: BoxLayout, orientation="horizontal", padding, spacing
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana
from kivy.core.window import Window

# BoxLayout: layout que organiza widgets en una sola dirección
# (horizontal o vertical). Es el layout más usado en Kivy.
from kivy.uix.boxlayout import BoxLayout

# Button: botón interactivo
from kivy.uix.button import Button


class BoxLayoutApp(App):

    def build(self):
        # Título de la ventana
        self.title = "Disposición horizontal Kivy"

        # Tamaño inicial de la ventana
        Window.size = (300, 100)

        # BoxLayout horizontal: los widgets se colocan de izquierda a derecha.
        # - orientation="horizontal": los widgets se distribuyen de izquierda a derecha.
        #   (Si fuera "vertical", se apilarían de arriba hacia abajo).
        # - padding=20: margen interno de 20 píxeles alrededor de todo el layout.
        # - spacing=10: espacio de 10 píxeles entre cada widget hijo.
        root = BoxLayout(orientation="horizontal", padding=20, spacing=10)

        # Agregamos tres botones al layout horizontal.
        # Al ser horizontal, aparecerán: [Izquierda] [Centro] [Derecha]
        root.add_widget(Button(text="Izquierda"))
        root.add_widget(Button(text="Centro"))
        root.add_widget(Button(text="Derecha"))

        return root


# Iniciamos la aplicación
BoxLayoutApp().run()