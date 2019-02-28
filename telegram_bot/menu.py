from itertools import count
from enum import Enum


MenuEntry = Enum(
    'MenuEntry',
    zip(
        [
            'START_MENU',
            'MANUAL_QUERY',
            'INTEGRAL',
            'DERIVATIVE',
            'LIMIT',
            'SUM',
            'PLOT',
            'EQUATION',
            'TAYLOR_SERIES',
            'EXTREMA',
        ],
        count()
    )
)


if __name__ == '__main__':
    for entry in MenuEntry:
        print("%s = %s" % (entry, entry.value))
