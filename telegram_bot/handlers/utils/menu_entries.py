from enum import auto, unique, IntEnum


@unique
class MenuEntry(IntEnum):
    START_MENU = auto()
    MANUAL_REQUEST = auto()
    INTEGRAL = auto()
    DERIVATIVE = auto()
    LIMIT = auto()
    SUM = auto()
    PLOT = auto()
    EQUATION = auto()
    TAYLOR_SERIES = auto()
    EXTREMA = auto()


if __name__ == '__main__':
    for entry in MenuEntry:
        print("%s = %s" % (entry, entry.value))
