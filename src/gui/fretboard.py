from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from fret import Fret

class FretBoard(BoxLayout):
    def __init__(self, fret_length: int = 12, number_of_string: int = 6, **kwargs):
        super(FretBoard, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.padding = 15

        buttons = _FretBoardButtons(fret_length, number_of_string)
        # buttons.size_hint_max_y = 0.9
        self.add_widget(buttons)

        numbers = _FretBoardNumbers(fret_length)
        numbers.size_hint_y = 0.1
        self.add_widget(numbers)

class _FretBoardButtons(GridLayout):
    def __init__(self, fret_length: int, number_of_string: int, **kwargs):
        super(_FretBoardButtons, self).__init__(**kwargs)

        self.spacing = 4
        self.cols = fret_length+1

        for string in range(number_of_string):
            for fret in range(fret_length+1):
                self.add_widget(Fret())

class _FretBoardNumbers(GridLayout):
    def __init__(self, fret_length: int, **kwargs):
        super(_FretBoardNumbers, self).__init__(**kwargs)

        self.spacing = 4
        self.cols = fret_length+1
        self.height = 10

        for fret in range(fret_length+1):
            self.add_widget(Label(text=f"{fret}"))
