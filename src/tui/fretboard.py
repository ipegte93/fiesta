from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Container
from textual.message import Message
from textual.screen import Screen
from textual.widget import events
from textual.widgets import Static

from src.calc import interval
from src.guitar import notes, scale


class Fretboard(Screen):
    BINDINGS = [
        ("c", "fret_clear", "clear fret"),
        ("t", "test", "test"),
    ]

    async def action_fret_clear(self) -> None:
        for fret in self.query("Fret").results(Fret):
            fret.toggle = False

    async def action_test(self) -> None:
        test = scale("a minor", self.fret)
        test = list(map(str, test))
        print(test)
        for fret in self.query("Fret").results(Fret):
            if not str(fret.render()) in test:
                fret.disabled = True

    def __init__(
        self,
        fret: int = 11,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
    ):
        super().__init__(name=name, id=id, classes=classes)
        self.fret = fret

    def compose(self) -> ComposeResult:
        with Container():
            i = 0
            for note in notes(self.fret):
                string_num = int(i / (self.fret + 1)) + 1
                fret_num = i % (self.fret + 1)
                i += 1

                yield Fret(note, classes=f"s{string_num} f{fret_num}")

    def on_mount(self) -> None:
        container = self.get_child_by_type(Container)
        container.border_title = "fretboard"
        container.styles.grid_size_columns = 6
        container.styles.grid_size_columns = self.fret+1

        # Display fret number on bottom line
        frets = list(self.query("Fret.s6").results(Fret))
        for i in range(self.fret+1):
            frets[i].border_subtitle = str(i)

    async def on_fret_pressed(self, event: Fret.Pressed) -> None:
        event.stop()

        # Only one fret toggled per string
        string_cls = ""
        for cls in event.fret.classes:
            if cls[0] == "s":
                string_cls = cls
        for fret in self.query("Fret.-toggle").results(Fret):
            if event.fret == fret:
                continue
            if fret.has_class(string_cls):
                fret.toggle = False

        toggle = list(self.query("Fret.-toggle").results(Fret))
        if len(toggle) == 0:
            self.action_fret_clear()
            return

        root = toggle.pop(-1)
        root.border_title = "1"

        for fret in toggle:
            title = interval(str(root.render()), str(fret.render()))
            fret.border_title = title


class Fret(Static):
    class Pressed(Message, bubble=True):
        """Fret Pressed Message."""

        def __init__(self, fret: Fret) -> None:
            self.fret = fret
            super().__init__()

        @property
        def control(self) -> Fret:
            return self.fret

    async def _on_click(self, event: events.Click) -> None:
        event.stop()

        if self.toggle:
            self.toggle = False
        else:
            self.toggle = True

        self.post_message(Fret.Pressed(self))

    @property
    def toggle(self) -> bool:
        if self.has_class("-toggle"):
            return True
        return False

    @toggle.setter
    def toggle(self, value: bool | str):
        if value:
            self.add_class("-toggle")
        else:
            self.remove_class("-toggle")
            self.border_title = ""
