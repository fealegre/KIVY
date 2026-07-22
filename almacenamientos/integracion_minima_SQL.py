from pathlib import Path

from kivy.app import App, platform
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import sqlite3

Window.size = (480, 680)
Window.clearcolor = (0.96, 0.97, 1, 1)

conn = sqlite3.connect(Path(__file__).parent / "agenda.db")
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


class FormularioAgenda(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = dp(24)
        self.spacing = dp(16)

        with self.canvas.before:
            Color(0.96, 0.97, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._actualizar_fondo, size=self._actualizar_fondo)

        titulo = Label(
            text="Agenda de contactos",
            font_size=sp(24),
            bold=True,
            size_hint_y=None,
            height=dp(42),
            color=(0.15, 0.25, 0.45, 1),
        )
        self.add_widget(titulo)

        self.formulario = GridLayout(
            cols=2, spacing=dp(10), size_hint_y=None, height=dp(220)
        )
        self.formulario.row_default_height = dp(42)
        self.formulario.row_force_default = True
        self.formulario.padding = [0, dp(8), 0, 0]

        self.inputs = {}
        campos = [
            ("Nombre", "nombre"),
            ("Dirección", "direccion"),
            ("Email", "email"),
            ("Teléfono", "telefono"),
        ]

        for label_text, key in campos:
            etiqueta = Label(
                text=label_text,
                size_hint_x=0.35,
                halign="left",
                valign="middle",
                color=(0.2, 0.2, 0.2, 1),
            )
            entrada = TextInput(
                multiline=False,
                write_tab=False,
                hint_text=f"Ingrese {label_text.lower()}",
                padding=[dp(8), dp(8)],
                size_hint_x=0.65,
            )
            self.inputs[key] = entrada
            self.formulario.add_widget(etiqueta)
            self.formulario.add_widget(entrada)

        self.add_widget(self.formulario)

        botones = BoxLayout(size_hint_y=None, height=dp(46), spacing=dp(12))
        self.btn_cancelar = Button(
            text="Limpiar",
            padding=[dp(8), dp(8)],
            height=dp(46),
            font_size=sp(16),
            background_color=(0.85, 0.35, 0.35, 1),
            color=(1, 1, 1, 1),
        )
        self.btn_cancelar.bind(on_press=self.cancelar)
        botones.add_widget(self.btn_cancelar)

        self.btn_guardar = Button(
            text="Guardar",
            padding=[dp(8), dp(8)],
            height=dp(46),
            font_size=sp(16),
            background_color=(0.22, 0.58, 0.86, 1),
            color=(1, 1, 1, 1),
        )
        self.btn_guardar.bind(on_press=self.guardar)
        botones.add_widget(self.btn_guardar)
        self.add_widget(botones)

        self.estado = Label(
            text="Completa los datos y guarda un nuevo contacto.",
            size_hint_y=None,
            height=dp(36),
            color=(0.3, 0.3, 0.3, 1),
            halign="center",
        )
        self.add_widget(self.estado)

    def _actualizar_fondo(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def limpiar_campos(self):
        for entrada in self.inputs.values():
            entrada.text = ""

    def cancelar(self, instance):
        self.limpiar_campos()
        self.estado.text = "Formulario limpiado."
        self.estado.color = (0.35, 0.55, 0.35, 1)

    def guardar(self, instance):
        datos = {key: entrada.text.strip() for key, entrada in self.inputs.items()}

        if any(not valor for valor in datos.values()):
            self.estado.text = "Todos los campos son obligatorios."
            self.estado.color = (0.85, 0.25, 0.25, 1)
            return

        cur.execute(
            "INSERT INTO agenda (nombre, direccion, email, telefono) VALUES (?, ?, ?, ?)",
            (datos["nombre"], datos["direccion"], datos["email"], datos["telefono"]),
        )
        conn.commit()

        self.limpiar_campos()
        self.estado.text = "Contacto guardado correctamente."
        self.estado.color = (0.18, 0.58, 0.28, 1)


class MiApp(App):
    def build(self):
        self.title = "Agenda Kivy"
        if platform in ("android", "ios"):
            from kivy.core.window import Window

            Window.maximize()
        return FormularioAgenda()


if __name__ == "__main__":
    MiApp().run()
