from enum import Enum

# Diese Klasse dient als Enumeration der Farben einer Schachfigur
class e_notation(Enum):
    pawn = ""
    knight = "N"
    bishop = "B"
    rook = "R"
    queen = "Q"
    king = "K"
    roche_o = "O"
    roche_strich = "-"
    check = "+"
    check_mate = "#"
    promote = "="
    schlagen = "x"