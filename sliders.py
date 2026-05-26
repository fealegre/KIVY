# ─────────────────────────────────────────────────────────
# sliders.py — Selector deslizante en Kivy
# ─────────────────────────────────────────────────────────
# Muestra cómo crear un Slider (barra deslizante) y reaccionar
# cuando el usuario cambia su valor, actualizando un Label.
# Conceptos clave: Slider, bind(), callback de propiedad, f-string
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# Window permite configurar el tamaño de la ventana
from kivy.core.window import Window

# BoxLayout organiza los widgets en una dirección
from kivy.uix.boxlayout import BoxLayout

# Label: etiqueta de texto no editable
from kivy.uix.label import Label

# Slider: barra deslizante para seleccionar un valor numérico dentro de un rango
from kivy.uix.slider import Slider


class SliderApp(App):

    def build(self):

        # Callback: función que se ejecuta cuando cambia el valor del Slider.
        # - instance: referencia al Slider que disparó el evento.
        # - value: el nuevo valor numérico del Slider.
        def on_value(instance, value):
            # Actualizamos el texto del label con el valor entero del slider.
            # int(value) convierte el valor decimal a número entero.
            label.text = f"Valor: {int(value)}"

        # Título de la ventana
        self.title = "Selector deslizante Kivy"

        # Tamaño inicial de la ventana
        Window.size = (300, 150)

        # Layout vertical: label arriba, slider abajo
        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Label que muestra el valor actual del slider.
        # Se inicializa con "Valor: 0" pero se actualizará al enlazar el evento.
        label = Label(text="Valor: 0")

        # Slider con rango de 0 a 100 y valor inicial de 50.
        # - min: valor mínimo del rango.
        # - max: valor máximo del rango.
        # - value: valor actual (posición inicial del indicador).
        slider = Slider(min=0, max=100, value=50)

        # Enlazamos la propiedad "value" del slider con la función on_value.
        # Cada vez que el usuario mueve el slider, on_value() se ejecuta
        # automáticamente con el nuevo valor.
        slider.bind(value=on_value)

        # Agregamos los widgets al layout (orden: primero label, luego slider)
        root.add_widget(label)
        root.add_widget(slider)

        return root


# Iniciamos la aplicación
SliderApp().run()