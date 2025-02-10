from enums.chess_typ_enum import e_chess_typ
from enums.chess_captured_enum import e_chess_captured
from enums.chess_color_enum import e_chess_color
from enums.chess_char_enum import e_chess_char
from chess_piece import c_chess_piece
from board.position_and_position_enum import c_position
from board.position_and_position_enum import e_zeile
from board.position_and_position_enum import e_spalte



class c_king(c_chess_piece):
    
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
    _typ = e_chess_typ.king

    #-------------------------------------------------------------------
    # Konstruktor
    #-------------------------------------------------------------------
    def __init__(self, position: c_position, farbe: e_chess_color):

        self._captured = e_chess_captured.no

        super().__init__(position, farbe, self._typ, self._captured)

        if self._farbe == e_chess_color.white:
            self._char = e_chess_char.white_king
        elif self._farbe == e_chess_color.black:
            self._char = e_chess_char.black_king
        else:
            raise TypeError("Ungültige Farbe eingegeben")

    #-------------------------------------------------------------------
    # Set und Get Funktionen
    #-------------------------------------------------------------------
    def get_char(self) -> e_chess_char:
        return self._char  


    #-------------------------------------------------------------------
    # Ist der Zug möglich Funktion
    #-------------------------------------------------------------------
    def laufen_possible(self, new_position: c_position) -> bool:
        match (new_position._zeile, new_position._spalte):
            case (e_zeile.r_8, _):
                if new_position._zeile == self._position._zeile + 1:
                    return 0
                return 1

            case (e_zeile.r_1, _):
                if new_position._zeile == self._position._zeile - 1:
                    return 0
                return 1

            case (_, e_spalte.l_a):
                if new_position._spalte == self._position._spalte - 1:
                    return 0
                return 1

            case (_, e_spalte.l_h):
                if new_position._spalte == self._position._spalte + 1:
                    return 0
                return 1

            case _:
                return 0
        return 0

            
