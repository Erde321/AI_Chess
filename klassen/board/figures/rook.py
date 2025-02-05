from enums.chess_typ_enum import e_chess_typ
from enums.chess_captured_enum import e_chess_captured
from enums.chess_color_enum import e_chess_color
from enums.chess_char_enum import e_chess_char
from chess_piece import c_chess_piece


class c_rook(c_chess_piece):

    #-------------------------------------------------------------------
    # Variablen
    #-------------------------------------------------------------------

    # Beinhaltet die Farbe der Schachfigur
    # _farbe

    # Beinhaltet den Typ der Figur z.B. Dame
    # _typ

    # Beinhaltet, ob die Figur im Spiel ist
    # _captured

    # Beinhaltet die Position der Figur
    # _position

    # Beinhaltet den Character der Figur
    # _char


    #-------------------------------------------------------------------
    # Klassenübergreifende Variable
    #-------------------------------------------------------------------
    _typ = e_chess_typ.rock


    #-------------------------------------------------------------------
    # Konstruktor
    #-------------------------------------------------------------------
    def __init__(self, position, farbe):

        self._captured = e_chess_captured.no

        super().__init__(position, farbe, self._typ, self._captured)

        if self._farbe == e_chess_color.white:
            self._char = e_chess_char.white_rook
        elif self._farbe == e_chess_color.black:
            self._char = e_chess_char.black_rook
        else:
            raise TypeError("Ungültiges Character eingegeben")
        
    #-------------------------------------------------------------------
    # Set und Get Funktionen
    #-------------------------------------------------------------------
    def get_char(self):
        return self._char  


    #-------------------------------------------------------------------
    # Ist der Zug möglich Funktion
    #-------------------------------------------------------------------
    def laufen_possible(self):
        # TODO
        return 0