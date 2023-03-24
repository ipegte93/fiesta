from __future__ import annotations

from textual.message import Message
from textual.widget import events
from textual.widgets import Static


class Fret(Static):
    DEFAULT_CSS = """
    Fret {
        width: 1fr;
        min-width: 2;
        max-width: 9;
        height: 3;
        content-align-horizontal: center;
        content-align-vertical: middle;
        border: solid gold;
    }
    Fret:disabled {
        border: solid grey;
    }
    Fret.-toggle {
        border: solid white;
    }
    Fret.-ToggleAlt {
        border: solid lightpink;
    }
    """

    class Pressed(Message, bubble=True):
        """Fret Pressed Message."""

        def __init__(self, fret: Fret) -> None:
            self.fret = fret
            super().__init__()

        @property
        def control(self) -> Fret:
            return self.fret

    def _on_click(self, event: events.Click) -> None:
        event.stop()
        self.post_message(Fret.Pressed(self))
