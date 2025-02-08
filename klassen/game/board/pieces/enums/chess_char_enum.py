from enum import Enum

# Diese Klasse dient als Enumeration der Farben einer Schachfigur
class e_chess_char(Enum):
    white_pawn = "♙"
    black_pawn = "♟"
    white_knight = "♘"
    black_knight = "♞"
    white_bishop = "♗"
    black_bishop = "♝"
    white_rook = "♖"
    black_rook = "♜"
    white_queen = "♕"
    black_queen = "♛"
    white_king = "♔"
    black_king = "♚"