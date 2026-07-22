from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        btn = Button(text="Go to Settings")
        btn.bind(on_press=self.go_to_settings)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = "settings"


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
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
