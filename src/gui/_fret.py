from __future__ import annotations

from functools import partial
from typing import cast

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

        @property
        def fret(self) -> Fret:
            return cast(Fret, self.sender)

    async def _on_click(self, event: events.Click) -> None:
        event.stop()
        self.post_message_no_wait(Fret.Pressed(self))
