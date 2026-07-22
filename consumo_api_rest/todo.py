from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest
import json


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.input = TextInput(hint_text="Escribe una tarea", multiline=False)
        self.boton = Button(text="Agregar tarea")
        self.boton.bind(on_press=self.enviar_tarea)

        self.lista = GridLayout(cols=1, size_hint_y=None)
        self.lista.bind(minimum_height=self.lista.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.lista)

        self.add_widget(self.input)
        self.add_widget(self.boton)
        self.add_widget(scroll)

    def enviar_tarea(self, instance):
        texto = self.input.text.strip()
        if not texto:
            return

        url = "https://jsonplaceholder.typicode.com/posts"
        datos = {"title": texto, "body": "Tarea desde Kivy", "userId": 1}
        headers = {"Content-Type": "application/json"}

        UrlRequest(
            url,
            req_body=json.dumps(datos).encode("utf-8"),
            req_headers=headers,
            method="POST",
            on_success=self.agregar_a_lista,
            on_failure=self.error_tarea,
            on_error=self.error_tarea,
        )  # type: ignore

        self.input.text = ""

    def agregar_a_lista(self, request, result):
        titulo = result.get("title", "Sin título")
        self.lista.add_widget(Label(text=titulo, size_hint_y=None, height=40))

    def error_tarea(self, request, error):
        print("Error al enviar la tarea:", error)


class MiApp(App):
    def build(self):
        return Root()


MiApp().run()
