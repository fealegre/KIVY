# ─────────────────────────────────────────────────────────
# saludo_interactivo.py — Ejercicio 1: Saludo Interactivo
# ─────────────────────────────────────────────────────────
# App con un campo de texto (TextInput), un botón (Button) y una
# etiqueta (Label). El usuario escribe su nombre, presiona el botón
# y la app genera un saludo personalizado.
#
# Conceptos clave: widget personalizado, TextInput, Button, Label,
#                  bind(), on_press, .text, .strip(), condicional if/else
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# BoxLayout organiza los widgets en una dirección
from kivy.uix.boxlayout import BoxLayout

# Label: etiqueta de texto no editable
from kivy.uix.label import Label

# Button: botón interactivo que responde a clics
from kivy.uix.button import Button

# TextInput: campo de entrada donde el usuario puede escribir texto
from kivy.uix.textinput import TextInput


# Creamos un widget personalizado heredando de BoxLayout.
# Esto nos permite encapsular toda la interfaz y su lógica en una clase
# reutilizable, en lugar de definir todo dentro de build().
class SaludoLayout(BoxLayout):

    # __init__ es el constructor: se ejecuta al crear una instancia del layout.
    # **kwargs permite pasar argumentos nombrados adicionales a la clase padre.
    def __init__(self, **kwargs):
        # super().__init__() llama al constructor de BoxLayout.
        # Siempre debemos llamar a super() antes de agregar widgets o
        # configurar propiedades del layout.
        super().__init__(**kwargs)

        # Configuración del layout principal
        self.orientation = "vertical"  # Widgets apilados de arriba hacia abajo
        self.padding = 20              # Margen interno de 20 píxeles
        self.spacing = 15              # Espacio de 15 píxeles entre widgets

        # ── Campo de entrada de texto ─────────────────────
        # TextInput donde el usuario escribe su nombre.
        # - hint_text: texto de sugerencia que aparece cuando el campo está vacío
        #   (similar a "placeholder" en HTML).
        # - multiline=False: campo de una sola línea (no permite Enter para saltar línea).
        # - size_hint_y=None: desactiva el tamaño proporcional vertical,
        #   permitiendo fijar una altura fija con height.
        # - height=50: altura fija de 50 píxeles.
        # - font_size=18: tamaño de la fuente del texto ingresado.
        self.input_nombre = TextInput(
            hint_text="Escribe tu nombre aquí",
            multiline=False,
            size_hint_y=None,
            height=50,
            font_size=18,
        )

        # ── Botón "Saludar" ──────────────────────────────
        # Botón que al presionarse genera el saludo personalizado.
        # - size_hint_y=None + height=50: altura fija de 50 píxeles.
        # - background_color: color de fondo en formato RGBA
        #   (0.2, 0.6, 0.9, 1) = azul.
        btn_saludar = Button(
            text="Saludar",
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 0.9, 1),
            font_size=18,
        )
        # Vinculamos el evento on_press del botón con el método self.saludar.
        # Cuando el usuario presione el botón, se ejecutará self.saludar().
        btn_saludar.bind(on_press=self.saludar)

        # ── Label de resultado ────────────────────────────
        # Etiqueta que muestra el saludo o un mensaje de error.
        # - halign="center": alineación horizontal del texto al centro.
        # - valign="middle": alineación vertical del texto al medio.
        # - text_size=(None, None): sin restricción de tamaño para el texto.
        self.label_resultado = Label(
            text="Ingrese su nombre y presione Saludar",
            font_size=20,
            halign="center",
            valign="middle",
            text_size=(None, None),
        )

        # ── Agregar widgets al layout ─────────────────────
        # El orden de add_widget determina el orden de aparición:
        # 1) Campo de texto (arriba)
        # 2) Botón "Saludar" (medio)
        # 3) Label con resultado (abajo)
        self.add_widget(self.input_nombre)
        self.add_widget(btn_saludar)
        self.add_widget(self.label_resultado)

    # ── Método callback: se ejecuta al presionar el botón ──
    # - instancia: referencia al botón que fue presionado.
    #   Es obligatorio recibirlo como parámetro en callbacks de on_press,
    #   aunque no lo usemos en este caso.
    def saludar(self, instancia):
        # Obtenemos el texto ingresado y eliminamos espacios al inicio y final
        # con .strip(). Esto evita que un nombre con solo espacios sea válido.
        nombre = self.input_nombre.text.strip()

        # Verificamos si el usuario ingresó algo (cadena no vacía).
        if nombre:
            # Si hay texto, mostramos un saludo personalizado con f-string.
            # f"¡Hola, {nombre}! 👋" inserta la variable nombre dentro del string.
            self.label_resultado.text = f"¡Hola, {nombre}! 👋"
        else:
            # Si el campo está vacío o solo tiene espacios, mostramos una advertencia.
            self.label_resultado.text = "⚠️ Por favor, ingrese un nombre."


# Clase de la aplicación: simplemente devuelve el layout personalizado.
# Separar el layout (SaludoLayout) de la app (SaludoApp) es una buena
# práctica que permite reutilizar el componente en otras aplicaciones.
class SaludoApp(App):
    def build(self):
        return SaludoLayout()


# Punto de entrada del programa.
# if __name__ == "__main__" asegura que el código solo se ejecute
# cuando corremos este archivo directamente (no al importarlo desde otro módulo).
if __name__ == "__main__":
    SaludoApp().run()