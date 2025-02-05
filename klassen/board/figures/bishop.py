from enums.chess_typ_enum import e_chess_typ
from enums.chess_captured_enum import e_chess_captured
from chess_piece import c_chess_piece


class c_bishop(c_chess_piece):

    typ = e_chess_typ.bishop

    def __init__(self, position, farbe):
        self.farbe = farbe
        self.captured = e_chess_captured.no
        super().__init__(position)
        

    def laufen(self):
        # TODO
        return 0