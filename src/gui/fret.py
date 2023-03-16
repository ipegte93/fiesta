from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder

from src.path import BASE

Path = str(BASE/"gui"/"fret.kv")

Builder.load_file(Path)


class Fret(ToggleButton):
    def __init__(self, **kwargs):
        super(Fret, self).__init__(**kwargs)

    # def on_press(self):
        # self.background_color = (1, 1, 1, 1)
        # return super().on_press()
