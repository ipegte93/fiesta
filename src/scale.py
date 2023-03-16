from src import Note


def scale(note: str | Note, scale: str) -> tuple[str]:
    if scale == "major":
        s = (2, 2, 1, 2, 2, 2, 1)
    elif scale == "minor" or scale == "natural minor":
        s = (2, 1, 2, 2, 1, 2, 2)
    elif scale == "harmonic minor":
        s = (2, 1, 2, 2, 1, 3, 1)
    else:
        raise ValueError

    if type(note) == str:
        n = Note(note)
    elif type(note) == Note:
        n = note
    else:
        raise ValueError

    ret = list()
    ret.append(n.__str__())
    for i in s:
        n = n + i
        ret.append(n.__str__())

    return tuple(ret)
