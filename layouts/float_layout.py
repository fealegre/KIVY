# ─────────────────────────────────────────────────────────
# float_layout.py — Disposición flotante con FloatLayout
# ─────────────────────────────────────────────────────────
# Muestra cómo usar FloatLayout para posicionar widgets libremente
# usando coordenadas relativas (proporciones de 0 a 1).
# A diferencia de BoxLayout o GridLayout, FloatLayout NO organiza
# automáticamente los widgets; nosotros controlamos su posición y tamaño.
# Conceptos clave: FloatLayout, size_hint, pos_hint, center_x, center_y, right, y
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana
from kivy.core.window import Window

# Button: botón interactivo
from kivy.uix.button import Button

# FloatLayout: layout que permite posicionar widgets libremente.
# Los widgets no se apilan ni se organizan en grilla; cada uno
# se coloca en una posición específica usando pos_hint.
from kivy.uix.floatlayout import FloatLayout


class FloatLayoutApp(App):

    def build(self):
        # Título de la ventana
        self.title = "Disposición flotante Kivy"

        # Tamaño inicial de la ventana
        Window.size = (600, 300)

        # FloatLayout sin restricciones de organización.
        # Cada widget hijo debe indicar su posición y tamaño manualmente.
        root = FloatLayout()

        # ── Botón 1: Centrado en la ventana ───────────────
        # - size_hint=(0.5, 0.2): el botón ocupa el 50% del ancho y
        #   el 20% del alto de la ventana. Los valores van de 0.0 a 1.0.
        # - pos_hint={"center_x": 0.5, "center_y": 0.5}: el centro del
        #   botón se ubica en el 50% del ancho y 50% del alto de la ventana,
        #   es decir, en el centro exacto.
        button1 = Button(
            text="Centrado",
            size_hint=(0.5, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        # ── Botón 2: Esquina inferior derecha ─────────────
        # - size_hint=(0.3, 0.1): ocupa el 30% del ancho y 10% del alto.
        # - pos_hint={"right": 1, "y": 0}:
        #   - right=1: el borde derecho del botón toca el borde derecho
        #     de la ventana (1 = 100% del ancho).
        #   - y=0: el borde inferior del botón toca el borde inferior
        #     de la ventana (0 = 0% del alto).
        button2 = Button(
            text="Esquina inferior derecha",
            size_hint=(0.3, 0.1),
            pos_hint={"right": 1, "y": 0},
        )

        # Agregamos los botones al layout
        root.add_widget(button1)
        root.add_widget(button2)

        return root


# Iniciamos la aplicación
FloatLayoutApp().run()