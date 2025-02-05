from abc import ABC, abstractmethod
from board.position_and_position_enum import c_position
from board.figures.enums.chess_captured_enum import e_chess_captured
from board.figures.enums.chess_char_enum import e_chess_char
from board.figures.enums.chess_color_enum import e_chess_color
from board.figures.enums.chess_typ_enum import e_chess_typ


# Eine abstracte Klasse mit abstracten Methoden und Variablen
# Die Klasse dient als Vaterklasse für alle Schachfiguren

class c_chess_piece(ABC):

    #-------------------------------------------------------------------
    # Variablen
    #-------------------------------------------------------------------

    # Beinhaltet die Farbe der Schachfigur
    _farbe = None

    # Beinhaltet den Typ der Figur z.B. Dame
    _typ = None

    # Beinhaltet den Character-Zeichen der Figur z.B. 
    _char = None

    # Beinhaltet, ob die Figur im Spiel ist
    _captured = None

    # _position ist auch eine Variable davon

    #-------------------------------------------------------------------
    # Konstruktor
    #-------------------------------------------------------------------

    def __init__(self, position):
        #---------------------------------------------------------------
        # Variablen Typen prüfen
        #---------------------------------------------------------------

        if (not(isinstance(position, c_position))):
            raise TypeError("Ungültige Position eingegeben")
        
        if (_farbe == None):
            raise NameError("Unterklasse muss Farbe definieren")
        
        if (_typ == None):
            raise NameError("Unterklasse muss Typ definieren")
        
        if (_char == None):
            raise NameError("Unterklasse muss Char definieren")
        
        if (_captured == None):
            raise NameError("Unterklasse muss Capture definieren")
        
        if (not(isinstance(_farbe, e_chess_color))):
            raise TypeError("Ungültige Farbe eingegeben")
        
        if (not(isinstance(_typ, e_chess_typ))):
            raise TypeError("Ungültiger Typ eingegeben")
        
        if (not(isinstance(_char, e_chess_char))):
            raise TypeError("Ungültiger Char eingegeben")
        
        if (not(isinstance(_captured, e_chess_captured))):
            raise TypeError("Ungültiger Capture eingegeben")
        


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
    
    def get_char(self):
        return self._char
    



    @abstractmethod
    def laufen(self):
        pass