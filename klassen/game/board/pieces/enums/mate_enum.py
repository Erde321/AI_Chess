from enum import Enum

# Diese Klasse dient als Enumeration der Farben einer Schachfigur
class e_mate(Enum):
    not_mate = 0
    mate = 1
    stale_mate = 2
    check_mate = 3