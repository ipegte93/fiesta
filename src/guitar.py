from src import Note


def notes(fret: int, tuning: str = "EADGBE"):
    ret = list()
    for note in list(tuning).__reversed__():
        for i in range(fret+1):
            ret.append(str(Note(note)+i))
    return ret


def scale(scale: str, fret: int, tuning: str = "EADGBE"):
    scale = scale.split(" ")
    note = Note(scale[0])
    scale = scale[1]
    if scale.lower() == "major":
        scale = (2, 2, 1, 2, 2, 2, 1)
    elif scale.lower() == "minor":
        scale = (2, 1, 2, 2, 1, 2, 2)
    else:
        raise ValueError("scale")

    ret = list()
    ret.append(note)
    for i in scale:
        note += i
        ret.append(note)

    return ret
