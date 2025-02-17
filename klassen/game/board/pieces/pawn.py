from enums.chess_typ_enum import e_chess_typ
from enums.chess_captured_enum import e_chess_captured
from enums.chess_color_enum import e_chess_color
from enums.chess_char_enum import e_chess_char
from chess_piece import c_chess_piece
from board.position_and_position_enum import c_position
from klassen.game.move.move import c_move
from klassen.game.board.pieces.enums.position_start_const_enum import position_start_const
from board.position_and_position_enum import e_zeile
from board.position_and_position_enum import e_spalte


class c_pawn(c_chess_piece):

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

    # Beinhaltet den Character zu dem die Figur promotet wird
    # _promote

    #-------------------------------------------------------------------
    # Klassenübergreifende Variable
    #-------------------------------------------------------------------
    _typ = e_chess_typ.pawn


    #-------------------------------------------------------------------
    # Konstruktor
    #-------------------------------------------------------------------
    def __init__(self, position: c_position, farbe: e_chess_color):

        self._captured = e_chess_captured.no
        self._promote = e_chess_typ.pawn

        super().__init__(position, farbe, self._typ, self._captured)

        if self._farbe == e_chess_color.white:
            self._char = e_chess_char.white_pawn
        elif self._farbe == e_chess_color.black:
            self._char = e_chess_char.black_pawn
        else:
            raise TypeError("Ungültige Farbe eingegeben")

    #-------------------------------------------------------------------
    # Set und Get Funktionen
    #-------------------------------------------------------------------
    def get_char(self) -> e_chess_char:
        return self._char  

    def get_promote(self) -> e_chess_typ:
        return self._promote
    
    def set_promote(self, promote: e_chess_typ) -> bool:
        if promote != e_chess_typ.king and promote != e_chess_typ.pawn:
            self._promote = promote
            return 1
        return 0

    #-------------------------------------------------------------------
    # Ist der Zug möglich Funktion
    #-------------------------------------------------------------------
    # Alle Laufmöglichkeiten wegen pawn promoten
    def laufen_possible(self, new_position: c_position, latest_opponent_new_position: c_position, latest_opponent_old_position: c_position, latest_opponent_piece_type: e_chess_typ) -> bool:
        
        match self._promote:
            case e_chess_typ.pawn:

                match self._farbe:
                    case e_chess_color.white:
                        if (self._position == position_start_const.w_pawn1_p or self._position == position_start_const.w_pawn2_p or self._position == position_start_const.w_pawn3_p or self._position == position_start_const.w_pawn4_p or self._position == position_start_const.w_pawn5_p or self._position == position_start_const.w_pawn6_p or self._position == position_start_const.w_pawn7_p or self._position == position_start_const.w_pawn8_p) and ((new_position._zeile == self._position._zeile + 2) or (new_position._zeile == self._position._zeile + 1)):
                            return 1
                        elif new_position._zeile == self._position._zeile + 1 and new_position._spalte == self._position._spalte:
                            return 1
                        elif new_position._zeile == self._position._zeile + 1 and new_position._spalte == self._position._spalte + 1 and latest_opponent_piece_type == e_chess_typ.pawn and latest_opponent_old_position._zeile == self._position._zeile + 2 and latest_opponent_new_position._zeile == self._position._zeile and self._position._spalte == latest_opponent_old_position._spalte - 1:
                            return 1
                        elif new_position._zeile == self._position._zeile + 1 and new_position._spalte == self._position._spalte - 1 and latest_opponent_piece_type == e_chess_typ.pawn and latest_opponent_old_position._zeile == self._position._zeile + 2 and latest_opponent_new_position._zeile == self._position._zeile and self._position._spalte == latest_opponent_old_position._spalte + 1:
                            return 1
                        else:
                            return 0

                    case e_chess_color.black:
                        if (self._position == position_start_const.b_pawn1_p or self._position == position_start_const.b_pawn2_p or self._position == position_start_const.b_pawn3_p or self._position == position_start_const.b_pawn4_p or self._position == position_start_const.b_pawn5_p or self._position == position_start_const.b_pawn6_p or self._position == position_start_const.b_pawn7_p or self._position == position_start_const.b_pawn8_p) and ((new_position._zeile == self._position._zeile - 2) or (new_position._zeile == self._position._zeile - 1)):
                            return 1
                        elif new_position._zeile == self._position._zeile - 1 and new_position._spalte == self._position._spalte:
                            return 1
                        elif new_position._zeile == self._position._zeile - 1 and new_position._spalte == self._position._spalte + 1 and latest_opponent_piece_type == e_chess_typ.pawn and latest_opponent_old_position._zeile == self._position._zeile - 2 and latest_opponent_new_position._zeile == self._position._zeile and self._position._spalte == latest_opponent_old_position._spalte + 1:
                            return 1
                        elif new_position._zeile == self._position._zeile - 1 and new_position._spalte == self._position._spalte - 1 and latest_opponent_piece_type == e_chess_typ.pawn and latest_opponent_old_position._zeile == self._position._zeile - 2 and latest_opponent_new_position._zeile == self._position._zeile and self._position._spalte == latest_opponent_old_position._spalte - 1:
                            return 1
                        else:
                            return 0

                    case _:
                        raise TypeError("Falsche Farbe")
                return 0
                    
            case e_chess_typ.knight:

                if new_position._zeile == self._position._zeile + 1:
                    if (self._position._zeile == e_zeile.r_8) or (self._position._spalte == e_spalte.l_a or self._position._spalte == e_spalte.l_b or self._position._spalte == e_spalte.l_g or self._position._spalte == e_spalte.l_h):
                        return 0
                    return 1
                
                elif self._position._zeile + 2:
                    if (self._position._zeile == e_zeile.r_8 or self._position._zeile == e_zeile.r_7) or (self._position._spalte == e_spalte.l_a or self._position._spalte == e_spalte.l_h):
                        return 0
                    return 1


                elif self._position._zeile - 1:
                    if (self._position._zeile == e_zeile.r_1) or (self._position._spalte == e_spalte.l_a or self._position._spalte == e_spalte.l_b or self._position._spalte == e_spalte.l_g or self._position._spalte == e_spalte.l_h):
                        return 0
                    return 1

                elif self._position._zeile - 2:
                    if (self._position._zeile == e_zeile.r_1 or self._position._zeile == e_zeile.r_2) or (self._position._spalte == e_spalte.l_a or self._position._spalte == e_spalte.l_h):
                        return 0
                    return 1
                
                else:
                    return 0

            case e_chess_typ.bishop:

                for i in range(1,8):
                    for i2 in range(1,8):
                
                        if new_position._zeile == self._position._zeile + i and new_position._spalte == self._position._spalte + i2:
                            if self._position._zeile == e_zeile.r_8 or self._position._spalte == e_spalte.l_h:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile + i and new_position._spalte == self._position._spalte - i2:
                            if self._position._zeile == e_zeile.r_8 or self._position._spalte == e_spalte.l_a:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte + i2:
                            if self._position._zeile == e_zeile.r_1 or self._position._spalte == e_spalte.l_h:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte - i2:
                            if self._position._zeile == e_zeile.r_1 or self._position._spalte == e_spalte.l_a:
                                return 0
                            return 1

                        else:
                            return 0
                
                return 0

            case e_chess_typ.rook:

                for i in range(1,8):
                
                    if new_position._zeile == self._position._zeile + i and new_position._spalte == self._position._spalte :
                        if self._position._zeile == e_zeile.r_8:
                            return 0
                        return 1

                    elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte:
                        if self._position._zeile == e_zeile.r_1:
                            return 0
                        return 1

                    elif new_position._zeile == self._position._zeile and new_position._spalte == self._position._spalte + i:
                        if self._position._spalte == e_spalte.l_h:
                            return 0
                        return 1

                    elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte - i:
                        if self._position._spalte == e_spalte.l_a:
                            return 0
                        return 1

                    else:
                        return 0
                
                return 0

            case e_chess_typ.queen:
                for i in range(1,8):
                    for i in range(1,8):
                
                        if new_position._zeile == self._position._zeile + i and new_position._spalte == self._position._spalte :
                            if self._position._zeile == e_zeile.r_8:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte:
                            if self._position._zeile == e_zeile.r_1:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile and new_position._spalte == self._position._spalte + i:
                            if self._position._spalte == e_spalte.l_h:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte - i:
                            if self._position._spalte == e_spalte.l_a:
                                return 0
                            return 1


                    for i2 in range(1,8):
                
                        if new_position._zeile == self._position._zeile + i and new_position._spalte == self._position._spalte + i2:
                            if self._position._zeile == e_zeile.r_8 or self._position._spalte == e_spalte.l_h:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile + i and new_position._spalte == self._position._spalte - i2:
                            if self._position._zeile == e_zeile.r_8 or self._position._spalte == e_spalte.l_a:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte + i2:
                            if self._position._zeile == e_zeile.r_1 or self._position._spalte == e_spalte.l_h:
                                return 0
                            return 1

                        elif new_position._zeile == self._position._zeile - i and new_position._spalte == self._position._spalte - i2:
                            if self._position._zeile == e_zeile.r_1 or self._position._spalte == e_spalte.l_a:
                                return 0
                            return 1

                        else:
                            return 0
                
                return 0

            case _:
                raise TypeError("Falscher Typ")

        return 0