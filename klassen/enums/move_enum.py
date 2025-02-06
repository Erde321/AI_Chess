from enum import Enum
from klassen.enums.notation_enum import e_notation
from klassen.enums.files_enum import e_files
from klassen.enums.ranks_enum import e_ranks
from klassen.enums.move_type_enum import e_move_type


# Diese Klasse dient als Enumeration der Farben einer Schachfigur
class e_move(Enum):

    _move = None

    def check_if_rank_notation(char: str) -> bool:
        return 0
    
    def check_if_file_notation(char: str) -> bool:
        return 0
    
    def check_if_check_notation(char: str) -> bool:
        return 0
    
    def check_if_checkmate_notation(char: str) -> bool:
        return 0
    
    def check_if_promote_notation(char: str) -> bool:
        return 0

    # Schaut ob der Move die richtige Form hat
    # Wenn korrekt True
    def check_if_correct_notation_and_return_move_type(string: str) -> (bool, e_move_type):
        move_type = e_move_type.notdef
        
        match string[0]:
            # Alle Bauernzüge fangen mit einem File an
            case e_files.a.value | e_files.b.value | e_files.c.value | e_files.d.value | e_files.e.value | e_files.f.value | e_files.g.value:  
                
                match len(string):

                    # Alle Züge in der Form a3, b4, f7 usw
                    case 2:
                        if string[1] == e_ranks.r_1 or string[1] == e_ranks.r_2 or string[1] == e_ranks.r_3 or string[1] == e_ranks.r_4 or string[1] == e_ranks.r_5 or string[1] == e_ranks.r_6 or string[1] == e_ranks.r_7 or string[1] == e_ranks.r_8:
                            return 1, move_type
                        
                    # Alle Züge in der Form a5+ oder a5#
                    case 3:
                        return 0, move_type

                    # Alle Züge in der Form a8=Q oder exd6    
                    case 4:
                        return 0, move_type
                    
                    # Alle Züge in der Form a8=Q+ oder a8=Q# oder axb6+ oder axb6#
                    case 5:
                        return 0, move_type

                    # Alle Züge der Form exd8=Q
                    case 6:
                        return 0, move_type
                    
                    # Alle Züge der Form exd8=Q#
                    case 7:
                        return 0, move_type
                    
                    case _:
                        return 0, move_type
                    
                return 0, move_type
            
            # Alle Springerzüge fangen mit "N" an
            case e_notation.knight.value:
                return 0, move_type
            
            # Alle Läuferzüge fangen mit "B" an
            case e_notation.bishop.value:
                return 0, move_type
            
            # Alle Turmzüge fangen mit "B" an
            case e_notation.rook.value:
                return 0, move_type
            
            # Alle Damenzüge fangen mit "B" an
            case e_notation.queen.value:
                return 0, move_type
            
            case e_notation.king | e_notation.roche | e_notation.long_roche:
                return 0, move_type
            
            # Falsche Eingabe
            case _:
                return 0, move_type
            
        return 0, move_type
            
    
    def set_move(self, string: str) -> bool:
        if self.check_if_correct_notation(string):
            self._move = string
            return True
        return False

    def get_move(self) -> str:
        return self._move
            