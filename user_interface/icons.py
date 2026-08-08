from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class ImageApp(App):
    def build(self):
        layout = BoxLayout()
        img = Image(source="FA.png", size_hint=(1, 0.8))
        layout.add_widget(img)
        return layout


ImageApp().run()
