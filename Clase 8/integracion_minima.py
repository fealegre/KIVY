from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import json
from pathlib import Path

ARCHIVO = Path("preferencias.json")


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.input = TextInput(
            hint_text="Escribe tu nombre",
            multiline=False,
            size_hint=(1, None),
            height=40,
        )

        self.btn = Button(size_hint=(1, None), height=40, text="Guardar")

        self.btn.bind(on_press=self.guardar)
        self.add_widget(self.input)
        self.add_widget(self.btn)

    def guardar(self, instance):
        datos = {"nombre": self.input.text}
        ARCHIVO.write_text(json.dumps(datos), encoding="utf-8")


class MiApp(App):
    def build(self):
        return Root()


MiApp().run()
