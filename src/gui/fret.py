from kivy.uix.togglebutton import ToggleButton

from src.gui import color


class Fret(ToggleButton):
    def __init__(self, **kwargs):
        super(Fret, self).__init__(**kwargs)
        self.color = color.BLACK
        self.background_down = ""
        self.background_normal = ""
        self.background_disabled_down = ""
        self.background_disabled_normal = ""

    def on_press(self):
        if self.state == "normal":
            self.background_color = color.BTN_BG_NORMAL
        else:
            self.background_color = color.BTN_BG_DOWN

    def on_disabled(self, instance, value):
        if value:
            self.background_color = color.BTN_DISABLED
            self.disabled_color = color.BTN_DISABLED  # fonts color
        else:
            self.change_background_color()
