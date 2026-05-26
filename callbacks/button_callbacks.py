# ─────────────────────────────────────────────────────────
# button_callbacks.py — Enlazar eventos (callbacks) en Kivy
# ─────────────────────────────────────────────────────────
# Muestra cómo conectar un evento de botón (on_press) con una función
# callback, de modo que al presionar un botón se ejecute una acción.
# Conceptos clave: bind(), on_press, callback, instancia de widget
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana
from kivy.core.window import Window

# BoxLayout organiza los widgets en una dirección
from kivy.uix.boxlayout import BoxLayout

# Button: botón interactivo que responde a clics
from kivy.uix.button import Button

# Label: etiqueta de texto no editable
from kivy.uix.label import Label


class ButtonsCallbacksApp(App):

    def build(self):
        # Título de la ventana
        self.title = "Enlazar eventos Kivy"

        # Tamaño inicial de la ventana
        Window.size = (220, 220)

        # Layout vertical: label arriba, botones abajo
        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Label que mostrará qué botón fue presionado.
        # Lo guardamos como atributo (self.label) para poder
        # modificar su texto desde la función callback.
        self.label = Label(
            text="Presionaste: ...",
        )
        root.add_widget(self.label)

        # ── Callback ──────────────────────────────────────
        # Una función callback es una función que se pasa como argumento
        # a otra función para que sea ejecutada cuando ocurra un evento.
        #
        # on_press(instance) se ejecuta cada vez que se presiona un botón.
        # - instance: referencia al botón que fue presionado.
        #   Nos permite acceder a sus propiedades (como .text).
        def on_press(instance):
            # Actualizamos el texto del label con el texto del botón presionado.
            # instance.text contiene el texto del botón que disparó el evento.
            self.label.text = f"Presionaste: {instance.text}"

        # ── Creación de botones con enlace de eventos ─────
        for text in ["Ok", "Cancelar", "Aplicar"]:
            button = Button(text=text)

            # bind() conecta un evento del widget con una función callback.
            # on_press=on_press significa: "cuando se presione este botón,
            # ejecuta la función on_press()".
            # NOTA: on_press=on_press pasa la función sin llamarla
            #       (sin paréntesis). Si escribieramos on_press=on_press()
            #       la función se ejecutaría inmediatamente, no al presionar.
            button.bind(on_press=on_press)

            root.add_widget(button)

        return root


# Iniciamos la aplicación
ButtonsCallbacksApp().run()