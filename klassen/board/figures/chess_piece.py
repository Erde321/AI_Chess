from abc import ABC, abstractmethod
from board.position_and_position_enum import c_position
from board.figures.enums.chess_captured_enum import e_chess_captured
from board.figures.enums.chess_char_enum import e_chess_char
from board.figures.enums.chess_color_enum import e_chess_color
from board.figures.enums.chess_typ_enum import e_chess_typ


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

    def __init__(self, position, farbe=None, typ=None,captured=None):
        #---------------------------------------------------------------
        # Variablen Typen prüfen
        #---------------------------------------------------------------

        if (not(isinstance(position, c_position))):
            raise TypeError("Ungültige Position eingegeben")
        
        if (farbe == None): # type: ignore 
            raise NameError("Unterklasse muss Farbe definieren")
        
        if (typ == None): # type: ignore 
            raise NameError("Unterklasse muss Typ definieren")
        
        if (captured == None): # type: ignore
            raise NameError("Unterklasse muss Capture definieren")
        
        if (not(isinstance(farbe, e_chess_color))): # type: ignore 
            raise TypeError("Ungültige Farbe eingegeben")
        
        if (not(isinstance(typ, e_chess_typ))): # type: ignore 
            raise TypeError("Ungültiger Typ eingegeben")
        
        if (not(isinstance(captured, e_chess_captured))): # type: ignore 
            raise TypeError("Ungültiger Capture eingegeben")
        
        self._farbe = farbe
        self._typ = typ
        self._captured

        self._position = position

    #-------------------------------------------------------------------
    # Set und Get Funktionen
    #-------------------------------------------------------------------

    def set_captured(self, chess_captured_enum):
        self._captured = chess_captured_enum

    def get_captured(self):
        return self._captured
    
    def set_position(self, position_enums):
        self._position = position_enums

    def get_position(self):
        return self._position
    
    def get_farbe(self):
        return self._farbe
    
    def get_typ(self):
        return self._typ
    
    

    @abstractmethod
    def laufen_possible(self):
        pass