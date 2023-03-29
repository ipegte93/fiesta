from textual.app import App as Textual
from textual.app import ComposeResult

from src.cli.fretboard import Fretboard


class App(Textual):
    def compose(self) -> ComposeResult:
        yield Fretboard()
