import re

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from src import Guitar
from src.calc import interval
from src.tui.fretboard import Fret


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

        toggled_list = self.query("Fret.-toggle")
        toggled_list = toggled_list.results(Fret)
        toggled_list = list(toggled_list)

        if len(toggled_list) == 0:
            return

        root = toggled_list.pop(-1)
        root.border_title = str(1)

        if len(toggled_list) == 0:
            return

        for toggled_fret in toggled_list:
            title = interval(str(root.render()), str(toggled_fret.render()))
            toggled_fret.border_title = title

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
        for fret in self.children:
            if fret == event.fret:
                continue
            elif fret.has_class("-toggle"):
                fret.remove_class("-toggle")
                fret.border_title = ""
