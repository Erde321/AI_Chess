from enum import Enum
from klassen.enums.notation_enum import e_notation

# Diese Klasse dient als Enumeration der verschiedenen Schachfiguren auf dem Board
class e_chess_piece(Enum):
    w_pawn1_e = e_notation.pawn
    w_pawn2_e = e_notation.pawn
    w_pawn3_e = e_notation.pawn
    w_pawn4_e = e_notation.pawn
    w_pawn5_e = e_notation.pawn
    w_pawn6_e = e_notation.pawn
    w_pawn7_e = e_notation.pawn
    w_pawn8_e = e_notation.pawn

    b_pawn1_e = e_notation.pawn
    b_pawn2_e = e_notation.pawn
    b_pawn3_e = e_notation.pawn
    b_pawn4_e = e_notation.pawn
    b_pawn5_e = e_notation.pawn
    b_pawn6_e = e_notation.pawn
    b_pawn7_e = e_notation.pawn
    b_pawn8_e = e_notation.pawn

    w_knight1_e = e_notation.knight
    w_knight2_e = e_notation.knight

    b_knight1_e = e_notation.knight
    b_knight2_e = e_notation.knight

    w_bishop1_e = e_notation.bishop
    w_bishop2_e = e_notation.bishop
    
    b_bishop1_e = e_notation.bishop
    b_bishop2_e = e_notation.bishop

    w_rook1_e = e_notation.rook
    w_rook2_e = e_notation.rook

    b_rook1_e = e_notation.rook
    b_rook2_e = e_notation.rook

    w_queen_e = e_notation.queen
    b_queen_e = e_notation.queen

    w_king_e = e_notation.king
    b_king_e = e_notation.king