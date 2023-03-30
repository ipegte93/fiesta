from __future__ import annotations

import re
from collections import deque
import copy


# Alteration
SHARP = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
FLAT = ('C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B')


class Note():

    def __init__(
            self,
            note: str,
            alteration: str = None,
    ) -> None:
        """
        alteration:
            sharp: C, C#, D, D#, ...
            flat: C, Db, D, Eb, ...
        """

        if type(alteration) is str:
            alteration = alteration.lower()

        if alteration not in {"sharp", "flat", None}:  # from parameter `alteration`
            raise ValueError("parameter alteration")
        notes = {"sharp": SHARP, "flat": FLAT}.get(alteration, None)

        if not notes:  # from parameter `note`
            search = re.search(r"^[a-gA-G](#|b)?", note)
            notes = {"b": FLAT, "#": SHARP}.get(search.group())

        if not notes:  # if can't get from above
            notes = SHARP

        self.notes = notes
        self.note = note

    def rotate(self, num: int) -> None:
        notes = self.notes
        notes = deque(notes)
        notes.rotate(num)
        self.notes = tuple(notes)

    def interval(self, note: Note | str) -> int:
        search = re.search(r"^([a-gA-G])(#|b)?", str(note))
        interval = self.notes.index(search.group(1).upper())
        interval += {"b": -1, "#": 1}.get(search.group(2), 0)
        return interval % 12

    @property
    def note(self) -> str:
        return self.notes[0]

    @note.setter
    def note(self, note: str) -> None:
        rotate = self.interval(note) * -1
        self.rotate(rotate)

    def __str__(self) -> str:
        return self.note

    def __repr__(self) -> str:
        return f"<Note: {self.__str__()}>"

    def __add__(self, value: int) -> Note:
        ret = copy.deepcopy(self)
        ret.rotate(value * -1)
        return ret

    def __sub__(self, value: Note | str):
        return self.interval(value)
