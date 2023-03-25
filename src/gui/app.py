from textual.app import App as Textual
from textual.app import ComposeResult

from src.gui.fretboard import Fretboard


class App(Textual):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Fretboard("ye")