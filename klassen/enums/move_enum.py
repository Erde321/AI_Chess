from enum import Enum
from klassen.enums.notation_enum import e_notation


# Diese Klasse dient als Enumeration der Farben einer Schachfigur
class e_move(Enum):

    _move = None


    def check_if_correct(self, string: str) -> bool:
        if string[0].islower():
            return True
        return False
    
    def set_move(self, string: str) -> bool:
        if self.check_if_correct(string):
            self._move = string
            return True
        return False

    def get_move(self) -> str:
        return self._move
            