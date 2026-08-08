from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Root(BoxLayout):
    def saludar(self):
        self.ids.mensaje.text = "Hola desde Python"


class MiApp(App):
    pass


MiApp().run()
