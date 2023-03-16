from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder

Builder.load_file("fret.kv")

class Fret(ToggleButton):
    def __init__(self, **kwargs):
        super(Fret, self).__init__(**kwargs)

    # def on_press(self):
        # self.background_color = (1, 1, 1, 1)
        # return super().on_press()
