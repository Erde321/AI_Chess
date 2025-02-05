from enum import Enum

# Diese Klasse dient als Enumeration der Schachfigur Typen und deren Wert im Spiel
class e_chess_typ(Enum):
    pawn = 1
    knight = 3
    bishop = 3
    rock = 5
    queen = 9
    king = 100