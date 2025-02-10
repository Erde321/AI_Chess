from klassen.game.enums.notation_enum import e_notation
from klassen.game.enums.files_enum import e_files
from klassen.game.enums.ranks_enum import e_ranks
from klassen.game.move.enums.move_type_enum import e_move_type
from klassen.game.move.enums.move_player_enum import e_move_player
from board.position_and_position_enum import c_position
from board.position_and_position_enum import e_spalte
from board.position_and_position_enum import e_zeile
from board.pieces.chess_piece import c_chess_piece
from game.board.board import c_board

# Diese Klasse dient als Enumeration der Farben einer Schachfigur
class c_move():
    #-------------------------------------------------------------------
    # Beschreibung
    #-------------------------------------------------------------------
    # Instanziiert ein String, ein e_move_type und ein e_move_player mit default-Werten (_move = "", _move_type = e_move_type.notdef, _move_player = e_move_type.notdef)
    # _move beinhaltet einen validen Zug
    # _move_type beinhaltet den Zugtypen (kann detailliert sein, muss aber nicht | a5 kann der selbe Zug sein wie a5+, beides wird akzeptiert) 
    # _move_player beinhaltet wer den Zug macht
    # Setzt _move, _move_type und player mit und set_move_and_type_and_player() (_move_type ergibt sich aus _move)

    #-------------------------------------------------------------------
    # Variablen
    #-------------------------------------------------------------------

    #-------------------------------------------------------------------
    # _move
    # _move_type
    # _move_player
    # _new_position
    # _old_position
    # _piece

    #-------------------------------------------------------------------
    # Funktionen
    #-------------------------------------------------------------------
    # Public
    #-------------------------------------------------------------------

    #-------------------------------------------------------------------
    # Get und Set Funktionen
    #-------------------------------------------------------------------

    #-------------------------------------------------------------------
    # get_move()            # set_move_and_type_and_player()
    # get_move_type()       
    # get_move_player()     
    # get_old_position()
    # get_new_position()

    #--------------------------------------------------------------------
    # Private
    #-------------------------------------------------------------------
    # __check_if_rank_notation()
    # __check_if_roche_o_notation()
    # __check_if_roche_strich_notation()
    # __check_if_file_notation()
    # __check_if_check_notation()
    # __check_if_check_mate_notation()
    # __check_if_promote_notation()
    # __check_if_schlagen_notation()
    # __check_if_piece_notation()
    # __check_if_king_notation()

    # __check_if_case2_pawn

    # __check_if_case3_knight_bishop_rook_queen_king()
    # __check_if_case3_pawn()
    # __check_if_case3_roche()

    # __check_if_case4_knight_bishop_rook_queen_king()
    # __check_if_case4_pawn()
    # __check_if_case4_roche()

    # __check_if_case5_knight_bishop_rook_queen_king()
    # __check_if_case5_pawn()
    # __check_if_case5_roche()

    # __check_if_case6_knight_bishop_rook_queen()
    # __check_if_case6_pawn()
    # __check_if_case6_roche()

    # __check_if_case7_pawn()

    # __match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king()
    # __match_case_string_length_for_notation_and_move_type_pawn()
    # __match_case_string_length_for_notation_and_move_type_roche()

    # __check_if_correct_notation_and_return_move_type()


    # Konstruktor
    def __init__(self, move_player: e_move_player):
        self._move = ""
        self._move_type = e_move_type.notdef
        self._move_player = move_player
        self._old_position = c_position(e_spalte.notdef, e_zeile.notdef)
        self._new_position = c_position(e_spalte.notdef, e_zeile.notdef)
        self._piece = None
        

    # Check All Notation Charackter
    def __check_if_rank_notation(char: str) -> bool:
        if char == e_ranks.r_1.value or char == e_ranks.r_2.value or char == e_ranks.r_3.value or char == e_ranks.r_4.value or char == e_ranks.r_5.value or char == e_ranks.r_6.value or char == e_ranks.r_7.value or char == e_ranks.r_8.value: 
            return 1
        return 0
    
    def __check_if_roche_o_notation(char: str) -> bool:
        if char == e_notation.roche_o.value: 
            return 1
        return 0
    
    def __check_if_roche_strich_notation(char: str) -> bool:
        if char == e_notation.roche_strich.value:
            return 1
        return 0
    
    def __check_if_file_notation(char: str) -> bool:
        if char == e_files.a.value or char == e_files.b.value or char == e_files.c.value or char == e_files.d.value or char == e_files.e.value or char == e_files.f.value or char == e_files.g.value or char == e_files.h.value: 
            return 1
        return 0
    
    def __check_if_check_notation(char: str) -> bool:
        if char == e_notation.check.value:
            return 1
        return 0
    
    def __check_if_check_mate_notation(char: str) -> bool:
        if char == e_notation.check_mate.value:
            return 1
        return 0
    
    def __check_if_promote_notation(char: str) -> bool:
        if char == e_notation.promote.value:
            return 1
        return 0
    
    def __check_if_schlagen_notation(char:str) -> bool:
        if char == e_notation.schlagen.value:
            return 1
        return 0
    
    def __check_if_piece_notation(char: str) -> bool:
        if char == e_notation.knight.value or char == e_notation.bishop.value or char == e_notation.rook.value or char == e_notation.queen.value:
            return 1
        return 0
    
    def __check_if_king_notation(char: str) -> bool:
        if char == e_notation.king.value:
            return 1
        return 0

    # Schaut ob ein 2 Zeichen langer String die richtige Form für einen Zug hat
    def __check_if_case2_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a3, b4, f7 usw
        # string [0] durch match case geprüft
        # string [1] durch __check_if_rank_notation geprüft
        if self.__check_if_rank_notation(string[1]):
            return 1, e_move_type.pawn_file_rank
        return 0, e_move_type.notdef

    # Schaut ob ein 3 Zeichen langer String die richtige Form für einen Zug hat
    def __check_if_case3_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nf3
        # string [0] durch match case geprüft in __check_if_correct_notation_and_return_move_type
        # string [1] durch __check_if_file_notation geprüft
        # string [2] durch __check_if_rank_notation geprüft
        if self.__check_if_file_notation(string[1]) and self.__check_if_rank_notation(string[2]):
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
    
    def __check_if_case3_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a5+ oder a5#
        # string [0] durch match case geprüft
        # string [1] durch __check_if_rank_notation
        # Alle Züge in der Form a5+
        # string [2] durch __check_if_check_notation
        # Alle Züge in der Form a5#
        # string [2] durch check_if_checkmate_notation
        if self.__check_if_rank_notation(string[1]):
            if self.__check_if_check_notation(string[2]):
                return 1, e_move_type.pawn_file_rank_check
            if self.__check_if_check_mate_notation(string[2]):
                return 1, e_move_type.pawn_file_rank_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef

    def __check_if_case3_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O
        # string [0] durch match case geprüft
        # string [1] durch __check_if_roche_strich_notation
        # string [2] durch __check_if_roche_o_notation

        if self.__check_if_roche_strich_notation(string[1]) and self.__check_if_roche_o_notation(string[2]):
            return 1, e_move_type.roche
        return 0, e_move_type.notdef
    
    # Schaut ob ein 4 Zeichen langer String die richtige Form für einen Zug hat
    def __check_if_case4_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nf3+, Nf3#, Nxg6, Ncb5 oder N5d4
        # string [0] durch match case geprüft in __check_if_correct_notation_and_return_move_type
        # Alle Züge in der Form Nf3+, Nf3# oder Ncb5
        # string [1] durch __check_if_file_notation geprüft
        # Alle Züge in der Form Nf3+ oder Nf3#
        # string [2] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form Nf3+
        # string [3] durch __check_if_check_notation geprüft
        # Alle Züge in der Form Nf3#
        # string [3] durch __check_if_check_mate_notation geprüft
        # Alle Züge in der Form Ncb5
        # string [0] durcch __check_if_king_notation geprüft # nochmal string[0] testen, weil kein solcher Königszug möglich
        # string [2] durch __check_if_file_notation geprüft
        # string [3] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form N5d4
        # string [0] durcch __check_if_king_notation geprüft # nochmal string[0] testen, weil kein solcher Königszug möglich
        # string [1] durch __check_if_rank_notation geprüft
        # string [2] durch __check_if_file_notation geprüft
        # string [3] durch __check_if_rank_notation geprüft
        # Alle Züge der Form Nxg6
        # string [1] durch __check_if_schlagen_notation geprüft
        # string [2] durch __check_if_file_notation geprüft
        # string [3] durch __check_if_rank_notation geprüft
        if self.__check_if_file_notation(string[1]):
            if self.__check_if_rank_notation(string[2]):
                if self.__check_if_check_notation(string[3]):
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
                if self.__check_if_check_mate_notation(string[3]):
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
            if not(self.__check_if_king_notation(string[0])) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]):
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
        if not(self.__check_if_king_notation(string[0])) and self.__check_if_rank_notation(string[1] and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3])):
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
        if self.__check_if_schlagen_notation(string[1]) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]):
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
    
    def __check_if_case4_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a8=Q oder exd6   
        # string [0] durch match case geprüft
        # Alle Züge in der Form a8=Q
        # string [1] durch __check_if_rank_notation
        # string [2] durch __check_if_promote_notation
        # string [3] durch __check_if_piece_notation
        # Alle Züge in der Form exd6 
        # string [1] durch __check_if_schlagen_notation
        # string [2] durch __check_if_file_notation
        # string [3] durch __check_if_rank_notation
        if self.__check_if_rank_notation(string[1]) and self.__check_if_promote_notation(string[2]) and self.__check_if_piece_notation(string[3]):
            return 1, e_move_type.pawn_file_rank_promote
        if self.__check_if_schlagen_notation(string[1]) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]):
            return 1, e_move_type.pawn_schlagen_file_rank
        return 0, e_move_type.notdef

    def __check_if_case4_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O+ oder O-O#  
        # string [0] durch match case geprüft
        # string [1] durch __check_if_roche_strich_notation
        # string [2] durch __check_if_roche_o_notation
        # Alle Züge in der Form O-O+
        # string [3] durch __check_if_check_notation
        # Alle Züge in der Form O-O#
        # string [3] durch __check_if_check_mate_notation

        if self.__check_if_roche_strich_notation(string[1]) and self.__check_if_roche_o_notation(string[2]):
            if self.__check_if_check_notation(string[3]):
                return 1, e_move_type.roche_check
            if self.__check_if_check_mate_notation(string[3]):
                return 1, e_move_type.roche_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    # Schaut ob ein 5 Zeichen langer String die richtige Form für einen Zug hat
    def __check_if_case5_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nxe5+, Nxe5#, Nbd2+, Nbd2#, N1f3+, N1f3#, Nf1d4
        # string [0] durch match case geprüft in __check_if_correct_notation_and_return_move_type
        # Alle Züge in der Form Nxe5+ oder Nxe5#
        # string [1] durch __check_if_schlagen_notation geprüft
        # string [2] durch __check_if_file_notation geprüft
        # string [3] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form Nxe5+
        # string [4] durch __check_if_check_notation geprüft
        # Alle Züge in der Form Nxe5#
        # string [4] durch __check_if_check_mate_notation geprüft
        # Alle Züge in der Form Nbd2+, Nbd2# oder Nf1d4
        # string [0] durch match case geprüft in __check_if_correct_notation_and_return_move_type
        # string [1] durch __check_if_file_notation
        # Alle Züge in der Form Nbd2+, Nbd2#
        # string [2] durch __check_if_file_notation
        # string [3] durch check_of_rank_notation
        # Alle Züge in der Form Nbd2+
        # string [4] durch __check_if_check_notation geprüft
        # Alle Züge in der Form Nbd2#
        # string [4] durch __check_if_check_mate_notation geprüft
        # Alle Züge in der Form Nf1d4
        # string [2] durch __check_of_rank_notation
        # string [3] durch __check_if_file_notation
        # string [4] durch check_of_rank_notation
        # Alle Züge in der Form N1f3+ oder N1f3#
        # string [0] durch match case geprüft in __check_if_correct_notation_and_return_move_type
        # string [1] durch __check_if_rank_notation geprüft
        # string [2] durch __check_if_file_notation geprüft
        # string [3] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form N1f3+
        # string [4] durch __check_if_check_notation geprüft
        # Alle Züge in der Form N1f3#
        # string [4] durch __check_if_check_mate_notation geprüft
        if self.__check_if_schlagen_notation(string[1]) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]):
            if self.__check_if_check_notation(string[4]):
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
            if self.__check_if_check_mate_notation(string[4]):
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
        if not(self.__check_if_king_notation(string[0])) and self.__check_if_file_notation(string[1]): 
            if self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]):
                if self.__check_if_check_notation(string[4]):
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
                if self.__check_if_check_mate_notation(string[string[4]]):
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
            if self.__check_if_rank_notation(string[2]) and self.__check_if_file_notation(string[3]) and self.__check_if_rank_notation(string[4]):
                match notation:
                        case e_notation.knight:
                            return 1, e_move_type.knight_file_rank_file_rank
                        case e_notation.bishop:
                            return 1, e_move_type.bishop_file_rank_file_rank
                        case e_notation.rook:
                            return 1, e_move_type.rook_file_rank_file_rank
                        case e_notation.queen:
                            return 1, e_move_type.queen_file_rank_file_rank
                        case _:
                            return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        if not(self.__check_if_king_notation(string[0])) and self.__check_if_rank_notation(string[1]) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]):
            if self.__check_if_check_notation(string[4]):
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
            if self.__check_if_check_mate_notation(string[4]):
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
    
    def __check_if_case5_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form a8=Q+, a8=Q#, axb6+ oder axb6#
        # string [0] durch match case geprüft
        # Alle Züge in der Form a8=Q+, a8=Q#
        # string [1] durch __check_if_rank_notation
        # string [2] durch __check_if_promote_notation
        # string [3] durch __check_if_piece_notation
        # Alle Züge in der Form a8=Q+
        # string [4] durch __check_if_check_notation
        # Alle Züge in der Form a8=Q#
        # string [4] durch __check_if_check_mate_notation
        # Alle Züge in der Form exd6+, axb6#
        # string [1] durch __check_if_schlagen_notation
        # string [2] durch __check_if_file_notation
        # string [3] durch __check_if_rank_notation
        # Alle Züge in der Form exd6+
        # string [4] durch __check_if_check_notation
        # Alle Züge in der Form axb6#
        # string [4] durch __check_if_check_mate_notation
        if self.__check_if_rank_notation(string[1]) and self.__check_if_promote_notation(string[2]) and self.__check_if_piece_notation(string[3]):
            if self.__check_if_check_notation(string[4]):
                return 1, e_move_type.pawn_file_rank_promote_check
            if self.__check_if_check_mate_notation(string[4]):
                return 1, e_move_type.pawn_file_rank_promote_check_mate
            return 0, e_move_type.notdef
        if self.__check_if_schlagen_notation(string[1]) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]):
            if self.__check_if_check_notation(string[4]):
                return 1, e_move_type.pawn_schlagen_file_rank_check
            if self.__check_if_check_mate_notation(string[4]):
                return 1, e_move_type.pawn_schlagen_file_rank_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    def __check_if_case5_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O-O   
        # string [0] durch match case geprüft
        # string [1] durch __check_if_roche_strich_notation
        # string [2] durch __check_if_roche_o_notation
        # string [3] durch __check_if_roche_strich_notation
        # string [4] durch __check_if_roche_o_notation

        if self.__check_if_roche_strich_notation(string[1]) and self.__check_if_roche_o_notation(string[2]) and self.__check_if_roche_strich_notation(string[3]) and self.__check_if_roche_o_notation(string[4]):
            return 1, e_move_type.roche_long
        return 0, e_move_type.notdef

    # Schaut ob ein 6 Zeichen langer String die richtige Form für einen Zug hat
    def __check_if_case6_knight_bishop_rook_queen(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nfxd4+, Nfxd4#, N1xd4+, N1xd4#, Nf1xd4, Nf1d4+ oder Nf1d4#
        # string [0] durch match case geprüft
        # Alle Züge in der Form Nfxd4+, Nfxd4#, Nf1xd4, Nf1d4+ oder Nf1d4#
        # string [1] durch __check_if_file_notation geprüft
        # Alle Züge in der Form Nfxd4+ oder Nfxd4#
        # string [2] durch __check_if_schlagen_notation geprüft
        # string [3] durch __check_if_file_notation geprüft
        # string [4] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form Nfxd4+
        # string [5] durch __check_if_check_notation geprüft
        # Alle Züge in der Form Nfxd4#
        # string [5] durch __check_if_check_mate_notation geprüft
        # Alle Züge in der Form Nf1xd4, Nf1d4+ oder Nf1d4#
        # string [2] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form Nf1d4+ oder Nf1d4#
        # string [3] durch __check_if_file_notation geprüft
        # string [4] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form Nf1d4+
        # string [5] durch __check_if_check_notation geprüft
        # Alle Züge in der Form Nf1d4#
        # string [5] durch __check_if_check_mate_notation geprüft
        # Alle Züge in der Form Nf1xd4
        # string [3] durch __check_if_schlagen_notation geprüft
        # string [4] durch __check_if_file_notation geprüft
        # string [5] durch __check_of_rank_notation geprüft
        # Alle Züge in der Form N1xd4+ oder N1xd4#
        # string [1] durch __check_of_rank_notation geprüft
        # string [2] durch __check_if_schlagen_notation geprüft
        # string [3] durch __check_if_file_notation geprüft
        # string [4] durch __check_if_rank_notation geprüft
        # Alle Züge in der Form N1xd4+
        # string [5] durch __check_if_check_notation geprüft
        # Alle Züge in der Form N1xd4#
        # string [5] durch __check_if_check_mate_notation geprüft
        if self.__check_if_file_notation(string[1]): 
            if self.__check_if_schlagen_notation(string[2]) and self.__check_if_file_notation(string[3]) and self.__check_if_rank_notation(string[4]):
                if self.__check_if_check_notation(string[5]):
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
                if self.__check_if_check_mate_notation(string[5]):
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
            if self.__check_if_rank_notation(string[2]):
                if self.__check_if_file_notation(string[3]) and self.__check_if_rank_notation(string[4]):
                    if self.__check_if_check_notation(string[5]):
                        match notation:
                            case e_notation.knight:
                                return 1, e_move_type.knight_file_rank_file_rank_check
                            case e_notation.bishop:
                                return 1, e_move_type.bishop_file_rank_file_rank_check
                            case e_notation.rook:
                                return 1, e_move_type.rook_file_rank_file_rank_check
                            case e_notation.queen:
                                return 1, e_move_type.queen_file_rank_file_rank_check
                            case _:
                                return 0, e_move_type.notdef
                        return 0, e_move_type.notdef
                    if self.__check_if_check_mate_notation(string[5]):
                        match notation:
                            case e_notation.knight:
                                return 1, e_move_type.knight_file_rank_file_rank_check_mate
                            case e_notation.bishop:
                                return 1, e_move_type.bishop_file_rank_file_rank_check_mate
                            case e_notation.rook:
                                return 1, e_move_type.rook_file_rank_file_rank_check_mate
                            case e_notation.queen:
                                return 1, e_move_type.queen_file_rank_file_rank_check_mate
                            case _:
                                return 0, e_move_type.notdef
                        return 0, e_move_type.notdef
                    return 0, e_move_type.notdef
                if self.__check_if_schlagen_notation(string[3]) and self.__check_if_file_notation(string[4]) and self.__check_if_rank_notation(string[5]):
                    match notation:
                        case e_notation.knight:
                            return 1, e_move_type.knight_file_rank_schlagen_file_rank
                        case e_notation.bishop:
                            return 1, e_move_type.bishop_file_rank_schlagen_file_rank
                        case e_notation.rook:
                            return 1, e_move_type.rook_file_rank_schlagen_file_rank
                        case e_notation.queen:
                            return 1, e_move_type.queen_file_rank_schlagen_file_rank
                        case _:
                            return 0, e_move_type.notdef
                    return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef
        if self.__check_if_rank_notation(string[1]) and self.__check_if_schlagen_notation(string[2]) and self.__check_if_file_notation(string[3]) and self.__check_if_rank_notation(string[4]):
            if self.__check_if_check_notation(string[5]):
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
            if self.__check_if_check_mate_notation(string[5]):
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

    def __check_if_case6_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge der Form exd8=Q
        # string [0] durch match case geprüft
        # string [1] durch __check_if_schlagen_notation
        # string [2] durch __check_if_file_notation
        # string [3] durch __check_if_rank_notation
        # string [4] durch __check_if_promote_notation
        # string [5] durch __check_if_piece_notation_notation
        if self.__check_if_schlagen_notation(string[1]) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]) and self.__check_if_promote_notation(string[4]) and self.__check_if_piece_notation(string[5]):
            return 1, e_move_type.pawn_schlagen_file_rank_promote
        return 0, e_move_type.notdef

    def __check_if_case6_roche(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form O-O-O+ oder O-O-O#
        # string [0] durch match case geprüft
        # string [1] durch __check_if_roche_strich_notation
        # string [2] durch __check_if_roche_o_notation
        # string [3] durch __check_if_roche_strich_notation
        # string [4] durch __check_if_roche_o_notation
        # Alle Züge der Form O-O-O+
        # string [5] durch __check_if_check_notation
        # Alle Züge der Form O-O-O#
        # string [5] durch __check_if_check_mate_notation

        if self.__check_if_roche_strich_notation(string[1]) and self.__check_if_roche_o_notation(string[2]) and self.__check_if_roche_strich_notation(string[3]) and self.__check_if_roche_o_notation(string[4]):
            if self.__check_if_check_notation(string[5]):
                return 1, e_move_type.roche_long_check
            if self.__check_if_check_mate_notation(string[5]):
                return 1, e_move_type.roche_long_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    # Schaut ob ein 7 Zeichen langer String die richtige Form für einen Zug hat
    def __check_if_case7_knight_bishop_rook_queen(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        # Alle Züge in der Form Nf1xd4+ oder Nf1xd4#
        # string [0] durch match case geprüft
        # string [1] durch __check_if_file_notation
        # string [2] durch __check_if_rank_notation
        # string [3] durch __check_if_schlagen_notation
        # string [4] durch __check_if_file_notation
        # string [5] durch __check_if_rank_notation
        # Alle Züge in der Form Nf1xd4+
        # string [6] durch __check_if_check_notation
        # Alle Züge in der Form Nf1xd4#
        # string [6] durch __check_if_check_mate_notation

        if self.__check_if_file_notation(string[1]) and self.__check_if_rank_notation(string[2]) and self.__check_if_schlagen_notation(string[3]) and self.__check_if_file_notation(string[4]) and self.__check_if_rank_notation(string[5]):
            if self.__check_if_check_notation(string[6]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_file_rank_schlagen_file_rank_check
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_file_rank_schlagen_file_rank_check
                    case e_notation.rook:
                        return 1, e_move_type.rook_file_rank_schlagen_file_rank_check
                    case e_notation.queen:
                        return 1, e_move_type.queen_file_rank_schlagen_file_rank_check
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            if self.__check_if_check_mate_notation(string[6]):
                match notation:
                    case e_notation.knight:
                        return 1, e_move_type.knight_file_rank_schlagen_file_rank_check_mate
                    case e_notation.bishop:
                        return 1, e_move_type.bishop_file_rank_schlagen_file_rank_check_mate
                    case e_notation.rook:
                        return 1, e_move_type.rook_file_rank_schlagen_file_rank_check_mate
                    case e_notation.queen:
                        return 1, e_move_type.queen_file_rank_schlagen_file_rank_check_mate
                    case _:
                        return 0, e_move_type.notdef
                return 0, e_move_type.notdef
            return 0, e_move_type.notdef  
        return 0, e_move_type.notdef

    def __check_if_case7_pawn(self, string: str) -> tuple[bool, e_move_type]:
        # Alle Züge der Form exd8=Q+ oder exd8=Q#
        # string [0] durch match case geprüft
        # string [1] durch __check_if_schlagen_notation
        # string [2] durch __check_if_file_notation
        # string [3] durch __check_if_rank_notation
        # string [4] durch __check_if_promote_notation
        # string [5] durch __check_if_piece_notation_notation
        # Alle Züge der Form exd8=Q+
        # string [6] durch __check_if_check_notation
        # Alle Züge der Form exd8=Q#
        # string [6] durch __check_if_check_mate_notation
        if self.__check_if_schlagen_notation(string[1]) and self.__check_if_file_notation(string[2]) and self.__check_if_rank_notation(string[3]) and self.__check_if_promote_notation(string[4]) and self.__check_if_piece_notation(string[5]):
            if self.__check_if_check_notation(string[6]):
                return 1, e_move_type.pawn_schlagen_file_rank_promote_check
            if self.__check_if_check_mate_notation(string[6]):
                return 1, e_move_type.pawn_schlagen_file_rank_promote_check_mate
            return 0, e_move_type.notdef
        return 0, e_move_type.notdef
    
    # Match case für move Typen nach Länge
    def __match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(self, string: str, notation: e_notation) -> tuple[bool, e_move_type]:
        match len(string):
            case 3:
                check, move_type = self.__check_if_case3_knight_bishop_rook_queen_king(string, notation)
                if check:
                    return check, move_type
                return 0, move_type
                    
            case 4:
                check, move_type = self.__check_if_case4_knight_bishop_rook_queen_king(string, notation)
                if check:
                    return check, move_type
                return 0, move_type
                    
            case 5:
                check, move_type = self.__check_if_case5_knight_bishop_rook_queen_king(string, notation)
                if check:
                    return check, move_type
                return 0, move_type

            case 6:
                if notation != e_notation.king: # es existiert kein case 6 für Königszüge
                    check, move_type = self.__check_if_case6_knight_bishop_rook_queen(string, notation)
                    if check:
                        return check, move_type
                    return check, move_type
                return 0, e_move_type.notdef
            
            case 7:
                if notation != e_notation.king: # es existiert kein case 7 für Königszüge
                    check, move_type = self.__check_if_case7_knight_bishop_rook_queen(string, notation)
                    if check:
                        return check, move_type
                    return check, move_type
                return 0, e_move_type.notdef

            case _:
                return 0, e_move_type.notdef

        return 0, e_move_type.notdef

    def __match_case_string_length_for_notation_and_move_type_pawn(self, string: str) -> tuple[bool, e_move_type]:
        match len(string):
            case 2:
                check, move_type = self.__check_if_case2_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 3:
                check, move_type = self.__check_if_case3_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 4:
                check, move_type = self.__check_if_case4_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 5:
                check, move_type = self.__check_if_case5_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 6:
                check, move_type = self.__check_if_case6_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 7:
                check, move_type = self.__check_if_case7_pawn(string)
                if check:
                    return check, move_type
                return 0, move_type

            case _:
                return 0, e_move_type.notdef

        return 0, e_move_type.notdef

    def __match_case_string_length_for_notation_and_move_type_roche(self, string: str) -> tuple[bool, e_move_type]:
        match len(string):
            case 3:
                check, move_type = self.__check_if_case3_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 4:
                check, move_type = self.__check_if_case4_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 5:
                check, move_type = self.__check_if_case5_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case 6:
                check, move_type = self.__check_if_case6_roche(string)
                if check:
                    return check, move_type
                return 0, move_type

            case _:
                return 0, e_move_type.notdef

        return 0, e_move_type.notdef
    
    # Schaut ob der Move die richtige Form hat
    # Wenn korrekt True
    def __check_if_correct_notation_and_return_move_type(self, string: str) -> tuple[bool, e_move_type]:
        
        match string[0]:
            # Alle Bauernzüge fangen mit einem File an
            case e_files.a.value | e_files.b.value | e_files.c.value | e_files.d.value | e_files.e.value | e_files.f.value | e_files.g.value:  
                check, move_type = self.__match_case_string_length_for_notation_and_move_type_pawn(string)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Springerzüge fangen mit "N" an
            case e_notation.knight.value:
                check, move_type = self.__match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.knight)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Läuferzüge fangen mit "B" an
            case e_notation.bishop.value:
                check, move_type = self.__match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.bishop)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Turmzüge fangen mit "R" an
            case e_notation.rook.value:
                check, move_type = self.__match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.rook)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Damenzüge fangen mit "Q" an
            case e_notation.queen.value:
                check, move_type = self.__match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.queen)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Königzüge fangen mit "K" an
            case e_notation.king.value:
                check, move_type = self.__match_case_string_length_for_notation_and_move_type_knight_bishop_rook_queen_king(string, e_notation.king)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Alle Rochezüge fangen mit "O" an
            case e_notation.roche_o.value:
                check, move_type = self.__match_case_string_length_for_notation_and_move_type_roche(string)
                if check:
                    return check, move_type
                return 0, e_move_type.notdef
            
            # Falsche Eingabe
            case _:
                return 0, e_move_type.notdef
            
        return 0, move_type

    # Set und get Funktionen
    def set_move_and_type_and_player_and_new_position_and_piece(self, string: str, board: c_board) -> bool:
        check, move_type = self.__check_if_correct_notation_and_return_move_type(string)
        if check:
            self._move = string
            self._move_type = move_type
            self._new_position = self.move_to_new_position()
            self._piece = self.new_position_to_piece(board)
            self._old_position = self._piece.get_position()
            return 1
        return 0

    def get_move(self) -> str:
        return self._move
            
    def get_move_type(self) -> str:
        return self._move_type
    
    def get_move_player(self) -> e_move_player:
        return self._move_player
    
    def get_old_position(self) -> c_position:
        return self._old_position
    
    def get_new_position(self) -> c_position:
        return self._old_position
    
    def move_to_new_position(self) -> c_position:
        move = self._move
        file = None
        rank = None
        len_move_minus_one = len(move)-1
        
        if move[len_move_minus_one] == e_notation.check or move[len_move_minus_one] == e_notation.check_mate:
            move = move[:-1]
        
        if move[len_move_minus_one] == e_notation.knight or move[len_move_minus_one] == e_notation.bishop or move[len_move_minus_one] == e_notation.rook or move[len_move_minus_one] == e_notation.queen:
            move = move[:-2]

        match move[len_move_minus_one]:
            case e_ranks.r_1.value:
                rank = e_zeile.r_1
            case e_ranks.r_2.value:
                rank = e_zeile.r_2
            case e_ranks.r_3.value:
                rank = e_zeile.r_3
            case e_ranks.r_4.value:
                rank = e_zeile.r_4
            case e_ranks.r_5.value:
                rank = e_zeile.r_5
            case e_ranks.r_6.value:
                rank = e_zeile.r_6
            case e_ranks.r_7.value:
                rank = e_zeile.r_7
            case e_ranks.r_8.value:
                rank = e_zeile.r_8

        match move[len_move_minus_one - 1]:
            case e_files.a.value:
                rank = e_spalte.l_a
            case e_files.b.value:
                rank = e_spalte.l_b
            case e_files.c.value:
                rank = e_spalte.l_c
            case e_files.d.value:
                rank = e_spalte.l_d
            case e_files.e.value:
                rank = e_spalte.l_e
            case e_files.f.value:
                rank = e_spalte.l_f
            case e_files.g.value:
                rank = e_spalte.l_g
            case e_files.h.value:
                rank = e_spalte.l_h

    def new_position_to_piece(self, board: c_board) -> c_chess_piece:
        # TODO
        match self._move_type:
            case 

        return 0
    