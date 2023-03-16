import re

from .note import Note


def chord_tones(chord: str) -> tuple[Note]:
    d = re.fullmatch(r"([a-gA-G])(#|b)?(m)?(7)?", chord)
    if not d:
        raise ValueError("chord")
    d = d.groups()
    ret = list()

    # root
    root = Note(d[0])
    if d[1] == "#":  # sharp
        root += 1
    elif d[1] == "b":  # flat
        root -= 1
    ret.append(root)

    # third
    if d[2] and d[2] == "m":
        third = root + 3  # minor
    else:
        third = root + 4  # major
    ret.append(third)

    # fifth
    fifth = root + 7
    ret.append(fifth)

    # seventh
    if d[3]:
        seventh = root + 11
        ret.append(seventh)

    return tuple(ret)


def notes_to_chords():
    pass


def notes_to_scale():
    pass
