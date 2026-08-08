from kivy.app import App
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout


class AnimatedButton(Button):
    def on_press(self):
        anim = Animation(x=300, y=200, duration=1) + Animation(
            size=(200, 200), duration=1
        )
        anim.start(self)


class AnimationApp(App):
    def build(self):
        layout = BoxLayout(padding=50)
        btn = AnimatedButton(text="Animate Me!")
        layout.add_widget(btn)
        return layout


AnimationApp().run()
