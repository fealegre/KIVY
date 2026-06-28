# ─────────────────────────────────────────────────────────
# contador_clicks.py — Ejercicio 2: Contador de Clics
# ─────────────────────────────────────────────────────────
# App con un contador que aumenta al presionar "Sumar" y vuelve a 0
# al presionar "Reiniciar". Usa NumericProperty para sincronizar
# automáticamente el estado del contador con la interfaz.
#
# Conceptos clave: NumericProperty, bind(), widget personalizado,
#                  __init__, super(), color dinámico
# ─────────────────────────────────────────────────────────

# Clase base para cualquier aplicación Kivy
from kivy.app import App

# BoxLayout organiza los widgets en una dirección
from kivy.uix.boxlayout import BoxLayout

# Label: etiqueta de texto no editable
from kivy.uix.label import Label

# Button: botón interactivo que responde a clics
from kivy.uix.button import Button

# NumericProperty: propiedad observable de tipo numérico.
# Cuando su valor cambia, notifica automáticamente a quienes la observan.
# Esto es fundamental para el patrón MVC (Modelo-Vista-Controlador) en Kivy.
from kivy.properties import NumericProperty


# Creamos un widget personalizado heredando de BoxLayout.
# En lugar de crear el layout en build(), definimos una clase reutilizable.
class ContadorLayout(BoxLayout):

    # NumericProperty(0): declaramos "contador" como una propiedad observable
    # con valor inicial 0. Cuando el valor de "contador" cambie, Kivy
    # disparará automáticamente cualquier función vinculada con bind().
    # Esto es más eficiente que actualizar manualmente el label cada vez.
    contador = NumericProperty(0)

    # __init__ es el constructor de la clase. Se ejecuta al crear una instancia.
    # **kwargs permite pasar argumentos nombrados adicionales a la clase padre.
    def __init__(self, **kwargs):
        # super().__init__() llama al constructor de BoxLayout.
        # Siempre debemos llamar a super() antes de agregar widgets.
        super().__init__(**kwargs)

        # Configuración del layout principal
        self.orientation = "vertical"  # Widgets apilados verticalmente
        self.padding = 30              # Margen interno de 30 píxeles
        self.spacing = 20              # Espacio de 20 píxeles entre widgets

        # ── Label grande que muestra el número del contador ──
        self.label_contador = Label(
            text="0",                          # Texto inicial
            font_size=72,                       # Tamaño de fuente grande
            bold=True,                          # Texto en negrita
            color=(0.2, 0.8, 0.4, 1),          # Color verde en RGBA
        )

        # ── Label pequeño con texto descriptivo ──
        self.label_info = Label(
            text="Clics realizados",
            font_size=20,
            color=(0.7, 0.7, 0.7, 1),          # Color gris claro
        )

        # ── Fila de botones (layout horizontal dentro del vertical) ──
        # Creamos un BoxLayout horizontal para poner los botones uno al lado del otro.
        # - size_hint_y=None: desactiva el tamaño proporcional vertical.
        # - height=60: altura fija de 60 píxeles para la fila.
        fila_botones = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=60,
            spacing=10,
        )

        # Botón "Sumar": incrementa el contador al presionarlo
        btn_sumar = Button(
            text="➕ Sumar",
            background_color=(0.2, 0.7, 0.3, 1),  # Color verde
            font_size=18,
        )
        # Vinculamos el evento on_press del botón con el método self.sumar
        btn_sumar.bind(on_press=self.sumar)

        # Botón "Reiniciar": pone el contador en 0 al presionarlo
        btn_reiniciar = Button(
            text="🔄 Reiniciar",
            background_color=(0.8, 0.3, 0.3, 1),  # Color rojo
            font_size=18,
        )
        # Vinculamos el evento on_press del botón con el método self.reiniciar
        btn_reiniciar.bind(on_press=self.reiniciar)

        # Agregamos los botones a la fila horizontal
        fila_botones.add_widget(btn_sumar)
        fila_botones.add_widget(btn_reiniciar)

        # Agregamos todos los widgets al layout principal (de arriba a abajo):
        # 1) Número grande del contador
        # 2) Texto "Clics realizados"
        # 3) Fila con los dos botones
        self.add_widget(self.label_contador)
        self.add_widget(self.label_info)
        self.add_widget(fila_botones)

        # ── Vinculación de la propiedad observable ──
        # bind(contador=self.actualizar_label) significa:
        # "Cada vez que cambie el valor de self.contador, ejecuta
        #  self.actualizar_label() automáticamente."
        # Esto es el corazón del patrón reactivo de Kivy:
        # el modelo (contador) cambia → la vista (label) se actualiza sola.
        self.bind(contador=self.actualizar_label)

    # ── Métodos de la clase ──────────────────────────────

    # Método callback para el botón "Sumar".
    # - instancia: referencia al botón que fue presionado (no la usamos aquí,
    #   pero es obligatorio recibirlo como parámetro en callbacks de on_press).
    def sumar(self, instancia):
        # Al incrementar self.contador, NumericProperty notifica el cambio
        # y se ejecuta automáticamente actualizar_label().
        self.contador += 1

    # Método callback para el botón "Reiniciar".
    def reiniciar(self, instancia):
        # Al asignar 0 a self.contador, se dispara actualizar_label().
        self.contador = 0

    # Método que se ejecuta automáticamente cuando cambia "contador".
    # - instancia: referencia al objeto que cambió (self, el layout).
    # - valor: el nuevo valor de la propiedad "contador".
    def actualizar_label(self, instancia, valor):
        # Actualizamos el texto del label con el nuevo valor
        self.label_contador.text = str(valor)

        # Cambiamos el color del número según el valor del contador:
        # - 0: verde (estado inicial)
        # - 1 a 9: amarillo (pocos clics)
        # - 10 o más: rojo (muchos clics)
        # Esto demuestra cómo la interfaz puede reaccionar dinámicamente
        # al estado de la aplicación.
        if valor == 0:
            self.label_contador.color = (0.2, 0.8, 0.4, 1)   # Verde
        elif valor < 10:
            self.label_contador.color = (1, 0.8, 0.2, 1)      # Amarillo
        else:
            self.label_contador.color = (0.9, 0.3, 0.3, 1)    # Rojo


# Clase de la aplicación: simplemente devuelve el layout personalizado.
# Separar el layout de la app es una buena práctica que permite
# reutilizar el componente en otras aplicaciones.
class ContadorApp(App):
    def build(self):
        return ContadorLayout()


# Punto de entrada del programa.
# if __name__ == "__main__" asegura que el código solo se ejecute
# cuando corremos este archivo directamente (no al importarlo).
if __name__ == "__main__":
    ContadorApp().run()