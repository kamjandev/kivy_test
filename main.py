from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
class TutorialApp(App):
    user_name = ""  # Shared variable to pass data between different screens/widgets
    background_sound = None  # Placeholder for the SoundLoader object

    def build(self):
        self.background_sound = SoundLoader.load("t5.mp3")
        if not self.background_sound:
            print("Error in App.build(): Audio file 't5.mp3' not found or unsupported.")
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hello!',
                  font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == '__main__':
    TutorialApp().run()
