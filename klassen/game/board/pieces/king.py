from enums.chess_typ_enum import e_chess_typ
from enums.chess_captured_enum import e_chess_captured
from enums.chess_color_enum import e_chess_color
from enums.chess_char_enum import e_chess_char
from chess_piece import c_chess_piece
from board.position_and_position_enum import c_position
from board.position_and_position_enum import e_zeile
from board.position_and_position_enum import e_spalte
from board.pieces.enums.mate_enum import e_mate



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
                if new_position._spalte == e_spalte.l_a and new_position._spalte == self._position._spalte - 1:
                    return 0
                return 1

            case (e_zeile.r_1, _):
                if new_position._zeile == self._position._zeile - 1:
                    return 0
                if new_position._spalte == e_spalte.l_h and  new_position._spalte == self._position._spalte + 1:
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

    def mate_check(self, board: list) -> e_mate:
        ausgabe = e_mate
        list_blocked_feld = list
        position = c_position
        for x in range(0,8):
            for y in range(0,8):
                match self._farbe:
                    case e_chess_color.white:
                        if board[x][y] != " " and board[x][y] != e_chess_char.white_king.value:
                            position.set_position(x,y)
                            list_blocked_feld.append(position)
                        match board[x][y]:
                            case e_chess_char.black_pawn.value:
                                if y+1 < 8 and board[x][y+1] != " ":
                                    position.set_position(x,y+1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-1 > -1 and board[x][y-1] != " ":
                                    position.set_position(x,y-1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                            
                            case e_chess_char.black_knight.value:
                                if y+1 < 8 and x+2 < 8 and board[x+2][y+1] != " ":
                                    position.set_position(x+2,y+1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y+1 < 8 and x-2 > -1 and board[x-2][y+1] != " ":
                                    position.set_position(x-2,y+1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-1 > -1 and x+2 < 8 and board[x+2][y-1] != " ":
                                    position.set_position(x+2,y-1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-1 > -1 and x-2 > -1 and board[x-2][y-1] != " ":
                                    position.set_position(x-2,y-1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y+2 < 8 and x+1 < 8 and board[x+1][y+2] != " ":
                                    position.set_position(x+1,y+2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y+2 < 8 and x-1 > -1 and board[x-1][y+2] != " ":
                                    position.set_position(x-1,y+2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-2 > -1 and x+1 < 8 and board[x+1][y-2] != " ":
                                    position.set_position(x+1,y-2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-2 > -1 and x-1 > -1 and board[x-1][y-2] != " ":
                                    position.set_position(x-1,y-2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)

                            case e_chess_char.black_bishop:
                                for i in range(1,7):
                                    if not(x+i > 7 or y+i > 7):
                                        if board[x+i][y+i] != " ":
                                            break
                                        position.set_position(x+i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0 or y+i > 7):
                                        if board[x-i][y+i] != " ": 
                                            break
                                        position.set_position(x-i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x+i > 7 or y-i < 0):
                                        if board[x+i][y-i] != " ":
                                            break
                                        position.set_position(x+i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 7 or y-i < 0):
                                        if board[x-i][y-i] != " ":
                                            break
                                        position.set_position(x-i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)

                            case e_chess_char.black_rook:
                                for i in range(1,7):
                                    if not(x+i > 7):
                                        if board[x+i][y] != " ":
                                            break
                                        position.set_position(x+i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0):
                                        if board[x-i][y] != " ":
                                            break
                                        position.set_position(x-i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y+i > 7):
                                        if board[x][y+i] == " ":
                                            break
                                        position.set_position(x,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y-i < 0):
                                        if board[x][y-i] != " ":
                                            break
                                        position.set_position(x,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)

                            case e_chess_char.black_queen:
                                for i in range(1,7):
                                    if not(x+i > 7 or y+i > 7):
                                        if board[x+i][y+i] != " ":
                                            break
                                        position.set_position(x+i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0 or y+i > 7):
                                        if board[x-i][y+i] != " ":
                                            break
                                        position.set_position(x-i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x+i > 7 or y-i < 0):
                                        if board[x+i][y-i] != " ":
                                            break
                                        position.set_position(x+i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 7 or y-i < 0):
                                        if board[x-i][y-i] != " ":
                                            break
                                        position.set_position(x-i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x+i > 7):
                                        if board[x+i][y] != " ":
                                            break
                                        position.set_position(x+i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0):
                                        if board[x-i][y] != " ":
                                            break
                                        position.set_position(x-i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y+i > 7):
                                        if board[x][y+i] != " ":
                                            break
                                        position.set_position(x,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y-i < 0):
                                        if board[x][y-i] != " ":
                                            break
                                        position.set_position(x,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                            
                            case e_chess_char.black_king:
                                if not(x+1 > 7):
                                    if board[x+1][y] == " ":
                                        position.set_position(x+1,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                        if not(y+1 > 7):
                                            position.set_position(x+1,y+1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                        if not(y-1 < 0):
                                            position.set_position(x+1,y-1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                if not(x-1 < 0):
                                    if board[x-1][y] == " ":
                                        position.set_position(x-1,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                        if not(y+1 > 7):
                                            position.set_position(x-1,y+1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                        if not(y-1 < 0):
                                            position.set_position(x-1,y-1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                if not(y+1 > 7):
                                    if board[x][y+1] == " ":
                                        position.set_position(x,y+1)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                if not(y-1 > 7):
                                    if board[x][y+1] == " ":
                                        position.set_position(x,y+1)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)         
                        
                            case _:
                                continue
                                
                    case e_chess_color.black:
                        if board[x][y] != " " and board[x][y] != e_chess_char.black_king.value:
                            position.set_position(x,y)
                            list_blocked_feld.append(position)
                        match board[x][y]:
                            case e_chess_char.white_pawn.value:
                                if y+1 < 8 and board[x][y+1] != " ":
                                    position.set_position(x,y+1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-1 > -1 and board[x][y-1] != " ":
                                    position.set_position(x,y-1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)

                            case e_chess_char.white_knight.value:
                                if y+1 < 8 and x+2 < 8 and board[x+2][y+1] != " ":
                                    position.set_position(x+2,y+1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y+1 < 8 and x-2 > -1 and board[x-2][y+1] != " ":
                                    position.set_position(x-2,y+1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-1 > -1 and x+2 < 8 and board[x+2][y-1] != " ":
                                    position.set_position(x+2,y-1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-1 > -1 and x-2 > -1 and board[x-2][y-1] != " ":
                                    position.set_position(x-2,y-1)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y+2 < 8 and x+1 < 8 and board[x+1][y+2] != " ":
                                    position.set_position(x+1,y+2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y+2 < 8 and x-1 > -1 and board[x-1][y+2] != " ":
                                    position.set_position(x-1,y+2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-2 > -1 and x+1 < 8 and board[x+1][y-2] != " ":
                                    position.set_position(x+1,y-2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)
                                if y-2 > -1 and x-1 > -1 and board[x-1][y-2] != " ":
                                    position.set_position(x-1,y-2)
                                    if not(position in list_blocked_feld):
                                        list_blocked_feld.append(position)

                            case e_chess_char.white_bishop:
                                for i in range(1,7):
                                    if not(x+i > 7 or y+i > 7):
                                        if board[x+i][y+i] != " ":
                                            break
                                        position.set_position(x+i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0 or y+i > 7):
                                        if board[x-i][y+i] != " ": 
                                            break
                                        position.set_position(x-i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x+i > 7 or y-i < 0):
                                        if board[x+i][y-i] != " ":
                                            break
                                        position.set_position(x+i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 7 or y-i < 0):
                                        if board[x-i][y-i] != " ":
                                            break
                                        position.set_position(x-i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)

                            case e_chess_char.white_rook:
                                for i in range(1,7):
                                    if not(x+i > 7):
                                        if board[x+i][y] != " ":
                                            break
                                        position.set_position(x+i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0):
                                        if board[x-i][y] != " ":
                                            break
                                        position.set_position(x-i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y+i > 7):
                                        if board[x][y+i] == " ":
                                            break
                                        position.set_position(x,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y-i < 0):
                                        if board[x][y-i] != " ":
                                            break
                                        position.set_position(x,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)

                            case e_chess_char.white_queen:
                                for i in range(1,7):
                                    if not(x+i > 7 or y+i > 7):
                                        if board[x+i][y+i] != " ":
                                            break
                                        position.set_position(x+i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0 or y+i > 7):
                                        if board[x-i][y+i] != " ":
                                            break
                                        position.set_position(x-i,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x+i > 7 or y-i < 0):
                                        if board[x+i][y-i] != " ":
                                            break
                                        position.set_position(x+i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 7 or y-i < 0):
                                        if board[x-i][y-i] != " ":
                                            break
                                        position.set_position(x-i,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x+i > 7):
                                        if board[x+i][y] != " ":
                                            break
                                        position.set_position(x+i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(x-i < 0):
                                        if board[x-i][y] != " ":
                                            break
                                        position.set_position(x-i,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y+i > 7):
                                        if board[x][y+i] != " ":
                                            break
                                        position.set_position(x,y+i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                for i in range(1,7):
                                    if not(y-i < 0):
                                        if board[x][y-i] != " ":
                                            break
                                        position.set_position(x,y-i)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                            
                            case e_chess_char.white_king:
                                if not(x+1 > 7):
                                    if board[x+1][y] == " ":
                                        position.set_position(x+1,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                        if not(y+1 > 7):
                                            position.set_position(x+1,y+1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                        if not(y-1 < 0):
                                            position.set_position(x+1,y-1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                if not(x-1 < 0):
                                    if board[x-1][y] == " ":
                                        position.set_position(x-1,y)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                        if not(y+1 > 7):
                                            position.set_position(x-1,y+1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                        if not(y-1 < 0):
                                            position.set_position(x-1,y-1)
                                            if not(position in list_blocked_feld):
                                                list_blocked_feld.append(position)
                                if not(y+1 > 7):
                                    if board[x][y+1] == " ":
                                        position.set_position(x,y+1)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)
                                if not(y-1 > 7):
                                    if board[x][y+1] == " ":
                                        position.set_position(x,y+1)
                                        if not(position in list_blocked_feld):
                                            list_blocked_feld.append(position)

                            case _:
                                continue
                    case _:
                        raise TypeError("Falsche Farbe")

        match self._farbe:
            case e_chess_color.white:
                for pos in list_blocked_feld:
                    if board[pos._spalte][pos._zeile] == e_chess_char.white_king.value:
                        
                        return e_mate.check_mate
                return e_mate.no_mate

            case e_chess_color.black:
                for pos in list_blocked_feld:
                    if board[pos._spalte][pos._zeile] == e_chess_char.black_king.value:
                        return e_mate.checkmate
                return e_mate.no_mate

            case _:
                raise TypeError("Falsche Farbe")

            
