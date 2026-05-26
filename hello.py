# ─────────────────────────────────────────────────────────
# hello.py — Mi primera app en Kivy
# ─────────────────────────────────────────────────────────
# Este es el ejemplo más simple posible de una aplicación Kivy.
# Muestra una etiqueta (Label) con el texto "Hola, Mundo!" en pantalla.
# Conceptos clave: App, Label, método build()
# ─────────────────────────────────────────────────────────

# Importamos la clase base App: toda app Kivy debe heredar de ella.
# App se encarga de crear la ventana, manejar el bucle de eventos, etc.
from kivy.app import App

# Importamos Label: un widget que muestra texto no editable en pantalla.
from kivy.uix.label import Label


# Creamos nuestra propia clase de aplicación heredando de App.
# Por convención, el nombre de la clase termina en "App" (ej: HelloApp).
# Kivy usa el nombre de la clase (sin "App") para buscar un archivo .kv
# asociado, pero en este caso no usamos uno.
class HelloApp(App):

    # El método build() es obligatorio: devuelve el widget raíz de la app.
    # Kivy lo llama automáticamente al iniciar la aplicación.
    def build(self):
        # Creamos una etiqueta con el texto que queremos mostrar.
        # Label es el widget más sencillo de Kivy para mostrar texto.
        return Label(text="Hola, Mundo!")


# Punto de entrada del programa.
# Creamos una instancia de nuestra app y llamamos a .run()
# para iniciar el bucle principal de eventos de Kivy.
HelloApp().run()