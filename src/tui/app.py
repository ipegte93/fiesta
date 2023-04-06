from textual.app import App as Textual
from textual.app import ComposeResult

from src.tui.fretboard import Fret, Fretboard


class App(Textual):

    CSS_PATH = "app.css"
    BINDINGS = [("c", "fret_clear", "clear fret")]

    def action_fret_clear(self) -> None:
        for f in self.query("Fret.-toggle").results(Fret):
            f.remove_class("-toggle")
            f.border_title = ""

    def compose(self) -> ComposeResult:
        yield Fretboard()
