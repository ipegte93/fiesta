from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder

from src.path import BASE

Path = str(BASE/"gui"/"fret.kv")

Builder.load_file(Path)

NORMAL = (1, 1, 1, 1)
DOWN = (0, 1, 0, 1)


class Fret(ToggleButton):
    def __init__(self, **kwargs):
        super(Fret, self).__init__(**kwargs)

    def on_press(self):
        if self.state == "normal":
            self.background_color = NORMAL
        else:
            self.background_color = DOWN

    def on_disabled(self, instance, value):
        if value:
            self.background_color = self.disabled_color
        else:
            self.change_background_color()
