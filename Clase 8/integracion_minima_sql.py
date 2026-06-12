# GridLayout
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import sqlite3

conn = sqlite3.connect("agenda.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS agenda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
)
""")


class MiGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        campos = ["Nombre", "Dirección", "Email", "Teléfono"]
        for campo in campos:
            self.add_widget(Label(text=campo, size_hint=(1, None), height=30))
            self.add_widget(TextInput(multiline=False, size_hint=(1, None), height=30))
        self.btn_cancelar = Button(text="Cancelar", size_hint=(1, None), height=40)
        self.add_widget(self.btn_cancelar)
        self.btn_cancelar.bind(on_press=self.cancelar)
        self.btn_guardar = Button(text="Guardar", size_hint=(1, None), height=40)
        self.btn_guardar.bind(on_press=self.guardar)
        self.add_widget(self.btn_guardar)

    def cancelar(self, instance):
        for widget in self.children:
            if isinstance(widget, TextInput):
                widget.text = ""

    def guardar(self, instance):
        nombre = self.children[7].text
        direccion = self.children[5].text
        email = self.children[3].text
        telefono = self.children[1].text
        cur.execute(
            "INSERT INTO agenda (nombre, direccion, email, telefono) VALUES (?, ?, ?, ?)",
            (nombre, direccion, email, telefono),
        )
        conn.commit()


class MiApp(App):
    def build(self):
        return MiGridLayout()


MiApp().run()
