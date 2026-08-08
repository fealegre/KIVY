from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp, sp
import json
from pathlib import Path

ARCHIVO = Path(__file__).parent / "preferencias.json"


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = dp(24)
        self.spacing = dp(16)

        self.input = TextInput(
            hint_text="Escribe lo que estás pensando...",
            multiline=True,
            size_hint=(1, None),
            height=dp(100),
        )

        self.btn = Button(
            size_hint=(1, None), height=dp(46), text="Guardar", font_size=sp(16)
        )

        self.btn.bind(on_press=self.guardar)
        self.add_widget(self.input)
        self.add_widget(self.btn)

    def guardar(self, instance):
        datos = {"Pensamiento": self.input.text}
        ARCHIVO.write_text(json.dumps(datos), encoding="utf-8")
        print(f"Guardado en {ARCHIVO}: {datos}")


class MiApp(App):
    def build(self):
        return Root()


MiApp().run()
