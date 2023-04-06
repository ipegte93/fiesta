from src import Note
import re

class Guitar:
    def __init__(
            self,
            pitches: str = "EADGBE",
            fret: int = 22
    ):
        self.__pitches = pitches
        self.__fret = fret
        self.__tuning()

    def note_to_locations(self, note: Note | str) -> list[tuple[int, int]]:
        ret = list()
        for s, string in enumerate(self.fretboard, start=1):
            for n, _note in enumerate(string):
                if str(_note) == str(note):
                    ret.append((s,n))
        return ret

    @property
    def pitches(self) -> str:
        return self.__pitches

    @pitches.setter
    def pitches(self, pitches: str) -> None:
        self.__pitches = pitches
        self.__tuning()

    @property
    def fret(self) -> int:
        return self.__fret

    @fret.setter
    def fret(self, fret: int) -> None:
        self.__fret = fret
        self.__tuning()

    def __tuning(self) -> None:
        self.fretboard = list()

        for note in list(self.pitches):
            gs = list()
            for i in range(self.fret+1):
                gs.append(Note(note)+i)
            self.fretboard.append(gs)

        self.fretboard.reverse()

def notes(fret: int, tuning: str = "EADGBE"):
    ret = list()
    for note in list(tuning).reverse():
        for i in range(fret+1):
            ret.append(Note(note)+i)
    return ret

def scale(scale, fret: int, tuning: str = "EADGBE"):
    pass
  
