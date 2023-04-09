from pathlib import Path

from textual.app import App as Textual

from src.tui.fretboard import Fretboard


class App(Textual):

    CSS_PATH = Path(__file__).parent / "app.css"

    def on_mount(self) -> None:
        self.push_screen(Fretboard())
