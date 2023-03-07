from __future__ import annotations

import re


class Note():
    # Alteration
    Sharp = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
    Flat = ('C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B')

    OCTAVE: bool = False

    def __init__(
        self, note: str | int,
        alteration: str = "Flat",
        show_octave: bool = False
    ) -> None:
        """
        alteration : `Sharp`, `Flat`\n
        Sharp -> C, C#, D, D#, ...\n
        Flat -> C, Db, D, Eb, ...
        """
        self.SHOW_OCTAVE = show_octave

        if alteration == "Sharp" or alteration == "Flat":
            self.ALTERATION = alteration
        else:
            raise ValueError("alteration")

        # note is int
        if type(note) is int:
            if note > 11:
                self.OCTAVE = True
            self.note: int = note
        # note is str
        elif type(note) is str:
            search = re.search(r"^([a-gA-G])(#|b)?([0-9])?", note)
            # group 1
            self.note: int = getattr(self, self.ALTERATION).index(
                search.group(1).upper())
            # group 2
            if search.group(2) == "b":
                self.note -= 1
            elif search.group(2) == "#":
                self.note += 1
            # group 3
            if search.group(3) is not None:
                self.note += int(search.group(3)) * 12
        # note is neither
        else:
            raise TypeError

    @property
    def note(self) -> int:
        return self.__note

    @note.setter
    def note(self, note: int) -> None:
        if self.OCTAVE:
            self.__note = note
        else:
            self.__note = note % 12

    def __str__(self) -> str:
        ret = getattr(self, self.ALTERATION)[self.note % 12]
        if self.SHOW_OCTAVE and self.OCTAVE:
            ret += str(int(self.note/12)+1)
        return ret

    def __repr__(self) -> str:
        return f"<Note: {self.__str__()}>"

    def __add__(self, num: int) -> Note:
        new = Note(
            self.note, alteration=self.ALTERATION,
            show_octave=self.SHOW_OCTAVE
        )
        new.OCTAVE = self.OCTAVE
        new.note += num
        return new

    def __sub__(self, num: int) -> Note:
        new = Note(
            self.note, alteration=self.ALTERATION,
            show_octave=self.SHOW_OCTAVE
        )
        new.OCTAVE = self.OCTAVE
        new.note -= num
        return new
