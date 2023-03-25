from textual.app import App, ComposeResult

from src.gui.fretboard import Fretboard


class Test(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Fretboard("ye")


if __name__ == "__main__":
    app = Test()
    app.run()
