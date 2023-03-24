from textual.app import App, ComposeResult
from src.gui import Fretboard

class Test(App):
    def compose(self) -> ComposeResult:
        yield Fretboard()

if __name__ == "__main__":
    app = Test()
    app.run()