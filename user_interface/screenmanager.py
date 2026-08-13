from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button, Label
from kivy.uix.boxlayout import BoxLayout


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        btn = Button(text="Go to Settings")
        lbl = Label(text="Home Screen", size_hint=(1, 0.2))
        btn.bind(on_press=self.go_to_settings)
        layout.add_widget(lbl)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = "settings"


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        lbl = Label(text="Settings Screen", size_hint=(1, 0.2))
        layout.add_widget(lbl)
        btn = Button(text="Back Home")
        btn.bind(on_press=self.go_home)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_home(self, instance):
        self.manager.current = "home"


class MultiScreenApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SettingsScreen(name="settings"))
        return sm


MultiScreenApp().run()
