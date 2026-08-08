from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class Formulario(BoxLayout):
    resultado = StringProperty("Completa el formulario")

    def validar(self):
        nombre = self.ids.nombre.text.strip()
        edad = self.ids.edad.text.strip()

        if not nombre or not edad:
            self.resultado = "Todos los campos son obligatorios"
            return

        if not edad.isdigit():
            self.resultado = "La edad debe ser numerica"
            return

        self.resultado = f"Datos correctos: {nombre}, {edad} anos"


class FormularioApp(App):
    pass


FormularioApp().run()
