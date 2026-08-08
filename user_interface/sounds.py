from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class SoundApp(App):
    def build(self):
        self.sound = SoundLoader.load("star_trek_sonar.mp3")
        btn = Button(text="Play Sound")
        btn.bind(on_press=self.play_sound)
        return btn

    def play_sound(self, instance):
        if self.sound:
            self.sound.play()
            print("🎵 Beep played!")


SoundApp().run()
