from abc import ABC, abstractmethod
from board.position_and_position_enum import c_position
from board.pieces.enums.chess_captured_enum import e_chess_captured
from board.pieces.enums.chess_char_enum import e_chess_char
from board.pieces.enums.chess_color_enum import e_chess_color
from board.pieces.enums.chess_typ_enum import e_chess_typ


# Eine abstracte Klasse mit abstracten Methoden
# Die Klasse dient als Vaterklasse für alle Schachfiguren

class c_chess_piece(ABC):

    #-------------------------------------------------------------------
    # Variablen
    #-------------------------------------------------------------------

    # Beinhaltet die Farbe der Schachfigur
    # _farbe

    # Beinhaltet den Typ der Figur z.B. Dame
    # _typ

    # Beinhaltet, ob die Figur im Spiel ist
    # _captured

    # _position ist auch eine Variable davon

    #-------------------------------------------------------------------
    # Konstruktor
    #-------------------------------------------------------------------

    def __init__(self, position: c_position, farbe: e_chess_color, typ: e_chess_typ, captured: e_chess_captured):
        
        self._farbe = farbe
        self._typ = typ
        self._captured

        self._position = position

    #-------------------------------------------------------------------
    # Set und Get Funktionen
    #-------------------------------------------------------------------

    def set_captured(self, captured: e_chess_captured):
        self._captured = captured

    def get_captured(self) -> e_chess_captured:
        return self._captured
    
    def set_position(self, position: c_position):
        self._position = position

    def get_position(self) -> c_position:
        return self._position
    
    def get_farbe(self) -> e_chess_color:
        return self._farbe
    
    def get_typ(self) -> e_chess_typ:
        return self._typ
    
    @abstractmethod
    def get_char(self) -> e_chess_char:
        pass
    

    @abstractmethod
    def laufen_possible(self) -> bool:
        pass