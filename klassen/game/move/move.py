from klassen.game.enums.notation_enum import e_notation
from klassen.game.enums.files_enum import e_files
from klassen.game.enums.ranks_enum import e_ranks
from klassen.game.move.enums.move_type_enum import e_move_type


# Diese Klasse dient als Enumeration der Farben einer Schachfigur
class c_move():

    _move = None
    _move_type = None

    # Check All Notation Charackter
    def check_if_rank_notation(char: str) -> bool:
        if char == e_ranks.r_1.value or char == e_ranks.r_2.value or char == e_ranks.r_3.value or char == e_ranks.r_4.value or char == e_ranks.r_5.value or char == e_ranks.r_6.value or char == e_ranks.r_7.value or char == e_ranks.r_8.value: 
            return 1
        return 0
    
    def check_if_roche_o_notation(char: str) -> bool:
        if char == e_notation.roche_o.value: 
            return 1
        return 0
    
    def check_if_roche_strich_notation(char: str) -> bool:
        if char == e_notation.roche_strich.value:
            return 1
        return 0
    
    def check_if_file_notation(char: str) -> bool:
        if char == e_files.a.value or char == e_files.b.value or char == e_files.c.value or char == e_files.d.value or char == e_files.e.value or char == e_files.f.value or char == e_files.g.value or char == e_files.h.value: 
            return 1
        return 0
    
    def check_if_check_notation(char: str) -> bool:
        if char == e_notation.check.value:
            return 1
        return 0
    
    def check_if_check_mate_notation(char: str) -> bool:
        if char == e_notation.check_mate.value:
            return 1
        return 0
    
    def check_if_promote_notation(char: str) -> bool:
        if char == e_notation.promote.value:
            return 1
        return 0
    
    def check_if_schlagen_notation(char:str) -> bool:
        if char == e_notation.schlagen.value:
            return 1
        return 0
    
    def check_if_piece_notation(char: str) -> bool:
        if char == e_notation.knight.value or char == e_notation.bishop.value or char == e_notation.rook.value or char == e_notation.queen.value:
            return 1
        return 0
    
    def check_if_king_notation(char: str) -> bool:
        if char == e_notation.king.value:
            return 1
        return 0

    # Schaut ob ein 2 Zeichen langer String die richtige Form für einen Zug hat
    def check_if_case2_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a3, b4, f7 usw
        # string [0] durch match case geprüft
        # string [1] durch check_if_rank_notation geprüft
        if self.check_if_rank_notation(string[1]):
            return 1, e_move_type.pawn_file_rank
        return 0, e_move_type.notdef

    # Schaut ob ein 3 Zeichen langer String die richtige Form für einen Zug hat
    def check_if_case3_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nf3
        # string [0] durch match case geprüft in check_if_correct_notation_and_return_move_type
        # string [1] durch check_if_file_notation geprüft
        # string [2] durch check_if_rank_notation geprüft
        if self.check_if_file_notation(string[1]) and self.check_if_rank_notation(string[2]):
            match notation:
                case e_notation.knight:
                    return 1, e_move_type.knight_file_rank
                case e_notation.bishop:
                    return 1, e_move_type.bishop_file_rank
                case e_notation.rook:
                    return 1, e_move_type.rook_file_rank
                case e_notation.queen:
                    return 1, e_move_type.queen_file_rank
                case e_notation.king:
                    return 1, e_move_type.king_file_rank
                case _:
                    return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    def check_if_case3_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a5+ oder a5#
        # string [0] durch match case geprüft
        # string [1] durch check_if_rank_notation
        # Alle Züge in der Form a5+
        # string [2] durch check_if_check_notation
        # Alle Züge in der Form a5#
        # string [2] durch check_if_checkmate_notation
        if self.check_if_rank_notation(string[1]):
            if self.check_if_check_notation(string[2]):
                return 1, e_move_type.pawn_file_rank_check
            if self.check_if_check_mate_notation(string[2]):
                return 1, e_move_type.pawn_file_rank_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef

    def check_if_case3_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O
        # string [0] durch match case geprüft
        # string [1] durch check_if_roche_strich_notation
        # string [2] durch check_if_roche_o_notation

        if self.check_if_roche_strich_notation(string[1]) and self.check_if_roche_o_notation(string[2]):
            return 1, e_move_type.roche
        return 0, e_move_type.notdef
    
    # Schaut ob ein 4 Zeichen langer String die richtige Form für einen Zug hat
    def check_if_case4_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nf3+, Nf3#, Nxg6, Ncb5 oder N5d4
        # string [0] durch match case geprüft in check_if_correct_notation_and_return_move_type
        # Alle Züge in der Form Nf3+, Nf3# oder Ncb5
        # string [1] durch check_if_file_notation geprüft
        # Alle Züge in der Form Nf3+ oder Nf3#
        # string [2] durch check_if_rank_notation geprüft
        # Alle Züge in der Form Nf3+
        # string [3] durch check_if_check_notation geprüft
        # Alle Züge in der Form Nf3#
        # string [3] durch check_if_check_mate_notation geprüft
        # Alle Züge in der Form Ncb5
        # string [0] durcch check_if_king_notation geprüft # nochmal string[0] testen, weil kein solcher Königszug möglich
        # string [2] durch check_if_file_notation geprüft
        # string [3] durch check_if_rank_notation geprüft
        # Alle Züge in der Form N5d4
        # string [0] durcch check_if_king_notation geprüft # nochmal string[0] testen, weil kein solcher Königszug möglich
        # string [1] durch check_if_rank_notation geprüft
        # string [2] durch check_if_file_notation geprüft
        # string [3] durch check_if_rank_notation geprüft
        # Alle Züge der Form Nxg6
        # string [1] durch check_if_schlagen_notation geprüft
        # string [2] durch check_if_file_notation geprüft
        # string [3] durch check_if_rank_notation geprüft
        if self.check_if_file_notation(string[1]):
            if self.check_if_rank_notation(string[2]):
                if self.check_if_check_notation(string[3]):
                    match notation:
                        case e_notation.knight:
                            return 1, e_move_type.knight_file_rank_check
                        case e_notation.bishop:
                            return 1, e_move_type.bishop_file_rank_check
                        case e_notation.rook:
                            return 1, e_move_type.rook_file_rank_check
                        case e_notation.queen:
                            return 1, e_move_type.queen_file_rank_check
                        case e_notation.king:
                            return 1, e_move_type.king_file_rank_check
                        case _:
                            return 0, e_move_type.notdef
                    return 0, e_move_type.notdef
                if self.check_if_check_mate_notation(string[3]):
                    match notation:
                        case e_notation.knight:
                            return 1, e_move_type.knight_file_rank_check_mate
                        case e_notation.bishop:
                            return 1, e_move_type.bishop_file_rank_check_mate
                        case e_notation.rook:
                            return 1, e_move_type.rook_file_rank_check_mate
                        case e_notation.queen:
                            return 1, e_move_type.queen_file_rank_check_mate
                        case e_notation.king:
                            return 1, e_move_type.king_file_rank_check_mate
                        case _:
                            return 0, e_move_type.notdef
                    return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            if not(self.check_if_king_notation(string[0])) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_file_file_rank
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_file_file_rank
                    case e_notation.rook:
                        return 1, e_move_type.rook_file_file_rank
                    case e_notation.queen:
                        return 1, e_move_type.queen_file_file_rank
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        if not(self.check_if_king_notation(string[0])) and self.check_if_rank_notation(string[1] and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3])):
            match notation:
                case e_notation.knight:
                    return 1, e_move_type.knight_rank_file_rank
                case e_notation.bishop:
                    return 1, e_move_type.bishop_rank_file_rank
                case e_notation.rook:
                    return 1, e_move_type.rook_rank_file_rank
                case e_notation.queen:
                    return 1, e_move_type.queen_rank_file_rank
                case _:
                    return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        if self.check_if_schlagen_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]):
            match notation:
                case e_notation.knight:
                    return 1, e_move_type.knight_schlagen_file_rank
                case e_notation.bishop:
                    return 1, e_move_type.bishop_schlagen_file_rank
                case e_notation.rook:
                    return 1, e_move_type.rook_schlagen_file_rank
                case e_notation.queen:
                    return 1, e_move_type.queen_schlagen_file_rank
                case e_notation.king:
                    return 1, e_move_type
                case _:
                    return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    def check_if_case4_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a8=Q oder exd6   
        # string [0] durch match case geprüft
        # Alle Züge in der Form a8=Q
        # string [1] durch check_if_rank_notation
        # string [2] durch check_if_promote_notation
        # string [3] durch check_if_piece_notation
        # Alle Züge in der Form exd6 
        # string [1] durch check_if_schlagen_notation
        # string [2] durch check_if_file_notation
        # string [3] durch check_if_rank_notation
        if self.check_if_rank_notation(string[1]) and self.check_if_promote_notation(string[2]) and self.check_if_piece_notation(string[3]):
            return 1, e_move_type.pawn_file_rank_promote
        if self.check_if_schlagen_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]):
            return 1, e_move_type.pawn_schlagen_file_rank
        return 0, e_move_type.notdef

    def check_if_case4_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O+ oder O-O#  
        # string [0] durch match case geprüft
        # string [1] durch check_if_roche_strich_notation
        # string [2] durch check_if_roche_o_notation
        # Alle Züge in der Form O-O+
        # string [3] durch check_if_check_notation
        # Alle Züge in der Form O-O#
        # string [3] durch check_if_check_mate_notation

        if self.check_if_roche_strich_notation(string[1]) and self.check_if_roche_o_notation(string[2]):
            if self.check_if_check_notation(string[3]):
                return 1, e_move_type.roche_check
            if self.check_if_check_mate_notation(string[3]):
                return 1, e_move_type.roche_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    # Schaut ob ein 5 Zeichen langer String die richtige Form für einen Zug hat
    def check_if_case5_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nxe5+, Nxe5#, Nbd2+, Nbd2#, N1f3+, N1f3#
        # string [0] durch match case geprüft in check_if_correct_notation_and_return_move_type
        # Alle Züge in der Form Nxe5+ oder Nxe5#
        # string [1] durch check_if_schlagen_notation geprüft
        # string [2] durch check_if_file_notation geprüft
        # string [3] durch check_if_rank_notation geprüft
        # Alle Züge in der Form Nxe5+
        # string [4] durch check_if_check_notation geprüft
        # Alle Züge in der Form Nxe5#
        # string [4] durch check_if_check_mate_notation geprüft
        # Alle Züge in der Form Nbd2+ oder Nbd2#
        # string [0] durch match case geprüft in check_if_correct_notation_and_return_move_type
        # string [1] durch check_if_file_notation
        # string [2] durch check_if_file_notation
        # string [3] durch check_of_rank_notation
        # Alle Züge in der Form Nbd2+
        # string [4] durch check_if_check_notation geprüft
        # Alle Züge in der Form Nbd2#
        # string [4] durch check_if_check_mate_notation geprüft
        # Alle Züge in der Form N1f3+ oder N1f3#
        # string [0] durch match case geprüft in check_if_correct_notation_and_return_move_type
        # string [1] durch check_if_rank_notation geprüft
        # string [2] durch check_if_file_notation geprüft
        # string [3] durch check_if_rank_notation geprüft
        # Alle Züge in der Form N1f3+
        # string [4] durch check_if_check_notation geprüft
        # Alle Züge in der Form N1f3#
        # string [4] durch check_if_check_mate_notation geprüft
        if self.check_if_schlagen_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]):
            if self.check_if_check_notation(string[4]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_schlagen_file_rank_check
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_schlagen_file_rank_check
                    case e_notation.rook:
                        return 1, e_move_type.rook_schlagen_file_rank_check
                    case e_notation.queen:
                        return 1, e_move_type.queen_schlagen_file_rank_check
                    case e_notation.king:
                        return 1, e_move_type.king_schlagen_file_rank_check
                    case _:
                        return 0, e_move_type.notdef
            if self.check_if_check_mate_notation(string[4]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_schlagen_file_rank_check_mate
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_schlagen_file_rank_check_mate
                    case e_notation.rook:
                        return 1, e_move_type.rook_schlagen_file_rank_check_mate
                    case e_notation.queen:
                        return 1, e_move_type.queen_schlagen_file_rank_check_mate
                    case e_notation.king:
                        return 1, e_move_type.king_schlagen_file_rank_check_mate
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        if not(self.check_if_king_notation(string[0])) and self.check_if_file_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]):
            if self.check_if_check_notation(string[4]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_file_file_rank_check
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_file_file_rank_check
                    case e_notation.rook:
                        return 1, e_move_type.rook_file_file_rank_check
                    case e_notation.queen:
                        return 1, e_move_type.queen_file_file_rank_check
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            if self.check_if_check_mate_notation(string[string[4]]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_file_file_rank_check_mate
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_file_file_rank_check_mate
                    case e_notation.rook:
                        return 1, e_move_type.rook_file_file_rank_check_mate
                    case e_notation.queen:
                        return 1, e_move_type.queen_file_file_rank_check_mate
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        if not(self.check_if_king_notation(string[0])) and self.check_if_rank_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]):
            if self.check_if_check_notation(string[4]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_rank_file_rank_check
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_rank_file_rank_check
                    case e_notation.rook:
                        return 1, e_move_type.rook_rank_file_rank_check
                    case e_notation.queen:
                        return 1, e_move_type.queen_rank_file_rank_check
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            if self.check_if_check_mate_notation(string[4]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_rank_file_rank_check_mate
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_rank_file_rank_check_mate
                    case e_notation.rook:
                        return 1, e_move_type.rook_rank_file_rank_check_mate
                    case e_notation.queen:
                        return 1, e_move_type.queen_rank_file_rank_check_mate
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    def check_if_case5_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a8=Q+, a8=Q#, axb6+ oder axb6#
        # string [0] durch match case geprüft
        # Alle Züge in der Form a8=Q+, a8=Q#
        # string [1] durch check_if_rank_notation
        # string [2] durch check_if_promote_notation
        # string [3] durch check_if_piece_notation
        # Alle Züge in der Form a8=Q+
        # string [4] durch check_if_check_notation
        # Alle Züge in der Form a8=Q#
        # string [4] durch check_if_check_mate_notation
        # Alle Züge in der Form exd6+, axb6#
        # string [1] durch check_if_schlagen_notation
        # string [2] durch check_if_file_notation
        # string [3] durch check_if_rank_notation
        # Alle Züge in der Form exd6+
        # string [4] durch check_if_check_notation
        # Alle Züge in der Form axb6#
        # string [4] durch check_if_check_mate_notation
        if self.check_if_rank_notation(string[1]) and self.check_if_promote_notation(string[2]) and self.check_if_piece_notation(string[3]):
            if self.check_if_check_notation(string[4]):
                return 1, e_move_type.pawn_file_rank_promote_check
            if self.check_if_check_mate_notation(string[4]):
                return 1, e_move_type.pawn_file_rank_promote_check_mate
            return 0, e_move_type.notdef
        if self.check_if_schlagen_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]):
            if self.check_if_check_notation(string[4]):
                return 1, e_move_type.pawn_schlagen_file_rank_check
            if self.check_if_check_mate_notation(string[4]):
                return 1, e_move_type.pawn_schlagen_file_rank_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    def check_if_case5_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O-O   
        # string [0] durch match case geprüft
        # string [1] durch check_if_roche_strich_notation
        # string [2] durch check_if_roche_o_notation
        # string [3] durch check_if_roche_strich_notation
        # string [4] durch check_if_roche_o_notation

        if self.check_if_roche_strich_notation(string[1]) and self.check_if_roche_o_notation(string[2]) and self.check_if_roche_strich_notation(string[3]) and self.check_if_roche_o_notation(string[4]):
            return 1, e_move_type.roche_long
        return 0, e_move_type.notdef

    # Schaut ob ein 6 Zeichen langer String die richtige Form für einen Zug hat
    def check_if_case6_knight_bishop_rook_queen(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nfxd4+, Nfxd4#, N1xd4+ oder N1xd4#
        # string [0] durch match case geprüft
        # Alle Züge in der Form Nfxd4+ oder Nfxd4#
        # string [1] durch check_if_file_notation geprüft
        # string [2] durch check_if_schlagen_notation geprüft
        # string [3] durch check_if_file_notation geprüft
        # string [4] durch check_if_rank_notation geprüft
        # Alle Züge in der Form Nfxd4+
        # string [5] durch check_if_check_notation geprüft
        # Alle Züge in der Form Nfxd4#
        # string [5] durch check_if_check_mate_notation geprüft
        # Alle Züge in der Form N1xd4+ oder N1xd4#
        # string [1] durch check_of_rank_notation geprüft
        # string [2] durch check_if_schlagen_notation geprüft
        # string [3] durch check_if_file_notation geprüft
        # string [4] durch check_if_rank_notation geprüft
        # Alle Züge in der Form N1xd4+
        # string [5] durch check_if_check_notation geprüft
        # Alle Züge in der Form N1xd4#
        # string [5] durch check_if_check_mate_notation geprüft
        if self.check_if_file_notation(string[1]) and self.check_if_schlagen_notation(string[2]) and self.check_if_file_notation(string[3]) and self.check_if_rank_notation(string[4]):
            if self.check_if_check_notation(string[5]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_file_schlagen_file_rank_check
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_file_schlagen_file_rank_check
                    case e_notation.rook:
                        return 1, e_move_type.rook_file_schlagen_file_rank_check
                    case e_notation.queen:
                        return 1, e_move_type.queen_file_schlagen_file_rank_check
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            if self.check_if_check_mate_notation(string[5]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_file_schlagen_file_rank_check_mate
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_file_schlagen_file_rank_check_mate
                    case e_notation.rook:
                        return 1, e_move_type.rook_file_schlagen_file_rank_check_mate
                    case e_notation.queen:
                        return 1, e_move_type.queen_file_schlagen_file_rank_check_mate
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        if self.check_if_rank_notation(string[1]) and self.check_if_schlagen_notation(string[2]) and self.check_if_file_notation(string[3]) and self.check_if_rank_notation(string[4]):
            if self.check_if_check_notation(string[5]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_rank_schlagen_file_rank_check
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_rank_schlagen_file_rank_check
                    case e_notation.rook:
                        return 1, e_move_type.rook_rank_schlagen_file_rank_check
                    case e_notation.queen:
                        return 1, e_move_type.queen_rank_schlagen_file_rank_check
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            if self.check_if_check_mate_notation(string[5]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_rank_schlagen_file_rank_check_mate
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_rank_schlagen_file_rank_check_mate
                    case e_notation.rook:
                        return 1, e_move_type.rook_rank_schlagen_file_rank_check_mate
                    case e_notation.queen:
                        return 1, e_move_type.queen_rank_schlagen_file_rank_check_mate
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef

    def check_if_case6_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge der Form exd8=Q
        # string [0] durch match case geprüft
        # string [1] durch check_if_schlagen_notation
        # string [2] durch check_if_file_notation
        # string [3] durch check_if_rank_notation
        # string [4] durch check_if_promote_notation
        # string [5] durch check_if_piece_notation_notation
        if self.check_if_schlagen_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]) and self.check_if_promote_notation(string[4]) and self.check_if_piece_notation(string[5]):
            return 1, e_move_type.pawn_schlagen_file_rank_promote
        return 0, e_move_type.notdef

    def check_if_case6_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O-O+ oder O-O-O#
        # string [0] durch match case geprüft
        # string [1] durch check_if_roche_strich_notation
        # string [2] durch check_if_roche_o_notation
        # string [3] durch check_if_roche_strich_notation
        # string [4] durch check_if_roche_o_notation
        # Alle Züge der Form O-O-O+
        # string [5] durch check_if_check_notation
        # Alle Züge der Form O-O-O#
        # string [5] durch check_if_check_mate_notation

        if self.check_if_roche_strich_notation(string[1]) and self.check_if_roche_o_notation(string[2]) and self.check_if_roche_strich_notation(string[3]) and self.check_if_roche_o_notation(string[4]):
            if self.check_if_check_notation(string[5]):
                return 1, e_move_type.roche_long_check
            if self.check_if_check_mate_notation(string[5]):
                return 1, e_move_type.roche_long_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    # Schaut ob ein 7 Zeichen langer String die richtige Form für einen Zug hat
    def check_if_case7_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge der Form exd8=Q+ oder exd8=Q#
        # string [0] durch match case geprüft
        # string [1] durch check_if_schlagen_notation
        # string [2] durch check_if_file_notation
        # string [3] durch check_if_rank_notation
        # string [4] durch check_if_promote_notation
        # string [5] durch check_if_piece_notation_notation
        # Alle Züge der Form exd8=Q+
        # string [6] durch check_if_check_notation
        # Alle Züge der Form exd8=Q#
        # string [6] durch check_if_check_mate_notation
        if self.check_if_schlagen_notation(string[1]) and self.check_if_file_notation(string[2]) and self.check_if_rank_notation(string[3]) and self.check_if_promote_notation(string[4]) and self.check_if_piece_notation(string[5]):
            if self.check_if_check_notation(string[6]):
                return 1, e_move_type.pawn_schlagen_file_rank_promote_check
            if self.check_if_check_mate_notation(string[6]):
                return 1, e_move_type.pawn_schlagen_file_rank_promote_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    # Match case für move Typen nach Länge
    def match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        match len(string):
            case 3:
                check, move_type = self.check_if_case3_knight_bishop_rook_queen_king(string, notation)
                if check:
                    return check, move_type
                return 0, move_type
                    
            case 4:
                check, move_type = self.check_if_case4_knight_bishop_rook_queen_king(string, notation)
                if check:
                    return check, move_type
                return 0, move_type
                    
            case 5:
                check, move_type = self.check_if_case5_knight_bishop_rook_queen_king(string, notation)
                if check:
                    return check, move_type
                return 0, move_type

            case 6:
                if notation != e_notation.king: # es existiert kein case 6 für Königszüge
                    check, move_type = self.check_if_case6_knight_bishop_rook_queen(string, notation)
                    if check:
                        return check, move_type
                    return check, move_type
                return 0, e_move_type.notdef

            case _:
                return 0, e_move_type.notdef

        return 0, e_move_type.notdef

    def match_case_string_length_for_notation_and_move_type_pawn(self, string: str) -> tuple[bool, e_move_type]:
        match len(string):
            case 2:
                check, move_type = self.check_if_case2_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 3:
                check, move_type = self.check_if_case3_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 4:
                check, move_type = self.check_if_case4_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 5:
                check, move_type = self.check_if_case5_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 6:
                check, move_type = self.check_if_case6_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 7:
                check, move_type = self.check_if_case7_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case _:
                return 0, e_move_type.notdef

        return 0, e_move_type.notdef

    def match_case_string_length_for_notation_and_move_type_roche(self, string: str) -> tuple[bool, e_move_type]:
        match len(string):
            case 3:
                check, move_type = self.check_if_case3_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 4:
                check, move_type = self.check_if_case4_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 5:
                check, move_type = self.check_if_case5_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 6:
                check, move_type = self.check_if_case6_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case _:
                return 0, e_move_type.notdef

        return 0, e_move_type.notdef
    
    # Schaut ob der Move die richtige Form hat
    # Wenn korrekt True
    def check_if_correct_notation_and_return_move_type(self, string: str) -> tuple[bool, e_move_type]:
        
        match string[0]:
            # Alle Bauernzüge fangen mit einem File an
            case e_files.a.value | e_files.b.value | e_files.c.value | e_files.d.value | e_files.e.value | e_files.f.value | e_files.g.value:  
                check, move_type = self.match_case_string_length_for_notation_and_move_type_pawn(string)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Springerzüge fangen mit "N" an
            case e_notation.knight.value:
                check, move_type = self.match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.knight)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Läuferzüge fangen mit "B" an
            case e_notation.bishop.value:
                check, move_type = self.match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.bishop)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Turmzüge fangen mit "R" an
            case e_notation.rook.value:
                check, move_type = self.match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.rook)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Damenzüge fangen mit "Q" an
            case e_notation.queen.value:
                check, move_type = self.match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.queen)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Königzüge fangen mit "K" an
            case e_notation.king.value:
                check, move_type = self.match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.king)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Rochezüge fangen mit "O" an
            case e_notation.roche_o.value:
                check, move_type = self.match_case_string_length_for_notation_and_move_type_roche(string)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Falsche Eingabe
            case _:
                return 0, e_move_type.notdef
            
        return 0, move_type



    def set_move(self, string: str) -> bool:
        check, move_type = self.check_if_correct_notation_and_return_move_type(string)
        if check:
            self._move = string
            self._move_type = move_type
            return True
        return False

    def get_move(self) -> str:
        return self._move
            
    def get_move_type(self) -> str:
        return self._move_type