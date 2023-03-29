import re

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from src.gui.fretboard._fret import Fret
from src import Guitar


class Fretboard(Static):
    DEFAULT_CSS = """
    Fretboard {
        layout: vertical;
        border: solid white;
        border-title-align: left;
    }
    """

    FRET_LENGTH = 11
    border_title = "Fretboard"
    guitar = Guitar(fret=FRET_LENGTH)

    def on_fret_pressed(self, event: Fret.Pressed) -> None:
        event.stop()

        # s = re.search(r"s([0-9])-([0-9]{1,2})", event.fret.id)
        # note = self.guitar.fretboard[int(s.group(1))-1][int(s.group(2))]

    def on_mount(self) -> None:
        for i in range(self.FRET_LENGTH+1):
            f = self.query_one(f"#s5-{i}")
            f.border_subtitle = str(i)

    def compose(self) -> ComposeResult:
        fb = self.guitar.fretboard

        for s in fb:
            with Horizontal():
                for i in s:
                    yield Fret(str(i), id=f"s{fb.index(s)}-{s.index(i)}")


class Horizontal(Widget):
    DEFAULT_CSS = """
    Horizontal {
        layout: horizontal;
        height: 3;
    }
    """

    def on_fret_pressed(self, event: Fret.Pressed) -> None:
        for f in self.children:
            if f == event.fret:
                continue
            f.remove_class("-toggle")
