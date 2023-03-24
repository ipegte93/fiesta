import re

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from src.gui._fret import Fret
from src.guitar import Guitar


class Fretboard(Static):
    DEFAULT_CSS = """
    Fretboard {
        layout: vertical;
    }
    """

    guitar = Guitar(fret=12)

    def on_fret_pressed(self, event: Fret.Pressed) -> None:
        event.stop()

        # Find pressed fret's note.
        s = re.search(r"fret([0-9])-([0-9]{1,2})", event.fret.id)
        note = self.guitar.fretboard[int(s.group(1))-1][int(s.group(2))]

        # Toggle all if same note.
        for l in self.guitar.note_to_locations(note):
            fret = self.query_one(f"#fret{l[0]}-{l[1]}")
            fret.toggle_class("-toggle")

    def compose(self) -> ComposeResult:
        fb = self.guitar.fretboard

        yield Horizontal(*[
            Fret(f"{str(i)}", id=f"fret1-{fb[0].index(i)}") for i in fb[0]
        ])
        yield Horizontal(*[
            Fret(f"{str(i)}", id=f"fret2-{fb[1].index(i)}") for i in fb[1]
        ])
        yield Horizontal(*[
            Fret(f"{str(i)}", id=f"fret3-{fb[2].index(i)}") for i in fb[2]
        ])
        yield Horizontal(*[
            Fret(f"{str(i)}", id=f"fret4-{fb[3].index(i)}") for i in fb[3]
        ])
        yield Horizontal(*[
            Fret(f"{str(i)}", id=f"fret5-{fb[4].index(i)}") for i in fb[4]
        ])
        yield Horizontal(*[
            Fret(f"{str(i)}", id=f"fret6-{fb[5].index(i)}") for i in fb[5]
        ])
        yield Horizontal(*[
            Number(f"{i}") for i in range(0, 13)
        ])
        # yield Horizontal(*[
        #     FretNew(f"{str(i)}") for i in fb[5]
        # ])



class Horizontal(Widget):
    DEFAULT_CSS = """
    Horizontal {
        layout: horizontal;
        height: 3;
    }
    """


class Number(Static):
    DEFAULT_CSS = """
    Number {
        width: 1fr;
        min-width: 2;
        max-width: 9;
        height: 1;
        content-align-horizontal: center;
        content-align-vertical: middle;
    }
    """
