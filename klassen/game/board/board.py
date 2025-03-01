from pieces.pawn import c_pawn
from pieces.knight import c_knight
from pieces.bishop import c_bishop
from pieces.rook import c_rook
from pieces.queen import c_queen
from pieces.king import c_king
from pieces.chess_piece import c_chess_piece
from klassen.game.board.pieces.enums.position_start_const_enum import position_start_const
from board.pieces.enums.chess_color_enum import e_chess_color
from board.pieces.enums.chess_typ_enum import e_chess_typ
from board.pieces.enums.chess_captured_enum import e_chess_captured
from board.pieces.enums.chess_pieces_enum import e_chess_piece
from board.pieces.enums.chess_char_enum import e_chess_char
from board.position_and_position_enum import c_position
from klassen.game.move.move import c_move
from klassen.game.move.enums.move_type_enum import e_move_type


class c_board():
    #-------------------------------------------------------------------
    # Beschreibung
    #-------------------------------------------------------------------
    # Instanziiert eine Liste aus Leerzeichen als Board und jede Figur in jeder Farbe, setzt aber keine Figuren auf das Board.
    # Verschiebt eine Figur auf dem Board und die Position der Figur mit **change_piece_position()**, wenn eine Figur geschlagen wird, wird _captured gesetzt
    # Setzt das komplette Board zurück mit **reset_board()**, setzt aber keine Figuren auf das Board
    # Setzt die Position aller Figuren zurück mit **reset_pieces()**, ändert aber Board nicht
    # Setzt alle Figuren mit ihrer aktuellen Position auf das Board mit **set_all_pieces_on_board()**
    # Findet eine Figur mit einer Position und return(t) das Vaterklasseobjekt der Figur mit **find_piece_with_position()**

    #-------------------------------------------------------------------
    # Variablen
    #-------------------------------------------------------------------

    #-------------------------------------------------------------------
    # Bauernfiguren                                                             # Springerfiguren
    # w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8    # w_knight1, w_knight2
    # b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8    # b_knight1, b_knight2

    # Läuferfiguren                                                             # Turmfiguren
    # w_bishop1, w_bishop2                                                      # w_rook1, w_rook2
    # b_bishop1, b_bishop2                                                      # b_rook1, b_rook2

    # Damenfiguren                                                              # Königfiguren
    # w_queen                                                                   # w_king
    # b_queen                                                                   # b_king

    # Board
    # _board

    #-------------------------------------------------------------------
    # Funktionen
    #-------------------------------------------------------------------
    # Public
    #-------------------------------------------------------------------
    # reset_pieces()
    # set_all_pieces_on_board()
    # reset_board()
    # find_piece_with_position()
    # change_piece_position()
    #-------------------------------------------------------------------

    #-------------------------------------------------------------------
    # Get und Set Funktionen
    #-------------------------------------------------------------------

    #-------------------------------------------------------------------
    # Board

    # get_board()

    #-------------------------------------------------------------------
    # Figuren

    # get_char()        
    # get_captured()    # set_captured()
    # get_position()    # set_position()
    # get_farbe()
    # get_typ()
    # Nur Bauern: get_promote() # set_promote()
    #-------------------------------------------------------------------
    # Private
    #-------------------------------------------------------------------
    # __set_piece_on_board()

    #Instanziiert alle Figuren und das Board
    def __init__(self):
        # Schachfiguren Instanzen
        self.w_pawn1 = c_pawn(position_start_const.w_pawn1_p, e_chess_color.white)
        self.w_pawn2 = c_pawn(position_start_const.w_pawn2_p, e_chess_color.white)
        self.w_pawn3 = c_pawn(position_start_const.w_pawn3_p, e_chess_color.white)
        self.w_pawn4 = c_pawn(position_start_const.w_pawn4_p, e_chess_color.white)
        self.w_pawn5 = c_pawn(position_start_const.w_pawn5_p, e_chess_color.white)
        self.w_pawn6 = c_pawn(position_start_const.w_pawn6_p, e_chess_color.white)
        self.w_pawn7 = c_pawn(position_start_const.w_pawn7_p, e_chess_color.white)
        self.w_pawn8 = c_pawn(position_start_const.w_pawn8_p, e_chess_color.white)

        self.b_pawn1 = c_pawn(position_start_const.b_pawn1_p, e_chess_color.black)
        self.b_pawn2 = c_pawn(position_start_const.b_pawn2_p, e_chess_color.black)
        self.b_pawn3 = c_pawn(position_start_const.b_pawn3_p, e_chess_color.black)
        self.b_pawn4 = c_pawn(position_start_const.b_pawn4_p, e_chess_color.black)
        self.b_pawn5 = c_pawn(position_start_const.b_pawn5_p, e_chess_color.black)
        self.b_pawn6 = c_pawn(position_start_const.b_pawn6_p, e_chess_color.black)
        self.b_pawn7 = c_pawn(position_start_const.b_pawn7_p, e_chess_color.black)
        self.b_pawn8 = c_pawn(position_start_const.b_pawn8_p, e_chess_color.black)

        self.w_knight1 = c_knight(position_start_const.w_knight1_p, e_chess_color.white)
        self.w_knight2 = c_knight(position_start_const.w_knight2_p, e_chess_color.white)

        self.b_knight1 = c_knight(position_start_const.b_knight1_p, e_chess_color.black)
        self.b_knight2 = c_knight(position_start_const.b_knight2_p, e_chess_color.black)

        self.w_bishop1 = c_bishop(position_start_const.w_bishop1_p, e_chess_color.white)
        self.w_bishop2 = c_bishop(position_start_const.w_bishop2_p, e_chess_color.white)

        self.b_bishop1 = c_bishop(position_start_const.b_bishop1_p, e_chess_color.black)
        self.b_bishop2 = c_bishop(position_start_const.b_bishop2_p, e_chess_color.black)

        self.w_rook1 = c_rook(position_start_const.w_rook1_p, e_chess_color.white)
        self.w_rook2 = c_rook(position_start_const.w_rook2_p, e_chess_color.white)

        self.b_rook1 = c_rook(position_start_const.b_rook1_p, e_chess_color.black)
        self.b_rook2 = c_rook(position_start_const.b_rook2_p, e_chess_color.black)

        self.w_queen = c_queen(position_start_const.w_queen_p, e_chess_color.white)
        self.b_queen = c_queen(position_start_const.b_queen_p, e_chess_color.black)

        self.w_king = c_king(position_start_const.w_king_p, e_chess_color.white)
        self.b_king = c_king(position_start_const.b_king_p, e_chess_color.black)
    
        self._board = [
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
        ]

    #Setzt alle Figurpositionen auf ihren Standardwert
    def reset_pieces(self):
        # Reset white pawns
        self.w_pawn1.set_position(position_start_const.w_pawn1_p)
        self.w_pawn1.set_captured(e_chess_captured.no)
        self.w_pawn2.set_position(position_start_const.w_pawn2_p)
        self.w_pawn2.set_captured(e_chess_captured.no)
        self.w_pawn3.set_position(position_start_const.w_pawn3_p)
        self.w_pawn3.set_captured(e_chess_captured.no)
        self.w_pawn4.set_position(position_start_const.w_pawn4_p)
        self.w_pawn4.set_captured(e_chess_captured.no)
        self.w_pawn5.set_position(position_start_const.w_pawn5_p)
        self.w_pawn5.set_captured(e_chess_captured.no)
        self.w_pawn6.set_position(position_start_const.w_pawn6_p)
        self.w_pawn6.set_captured(e_chess_captured.no)
        self.w_pawn7.set_position(position_start_const.w_pawn7_p)
        self.w_pawn7.set_captured(e_chess_captured.no)
        self.w_pawn8.set_position(position_start_const.w_pawn8_p)
        self.w_pawn8.set_captured(e_chess_captured.no)

        # Reset black pawns
        self.b_pawn1.set_position(position_start_const.b_pawn1_p)
        self.b_pawn1.set_captured(e_chess_captured.no)
        self.b_pawn2.set_position(position_start_const.b_pawn2_p)
        self.b_pawn2.set_captured(e_chess_captured.no)
        self.b_pawn3.set_position(position_start_const.b_pawn3_p)
        self.b_pawn3.set_captured(e_chess_captured.no)
        self.b_pawn4.set_position(position_start_const.b_pawn4_p)
        self.b_pawn4.set_captured(e_chess_captured.no)
        self.b_pawn5.set_position(position_start_const.b_pawn5_p)
        self.b_pawn5.set_captured(e_chess_captured.no)
        self.b_pawn6.set_position(position_start_const.b_pawn6_p)
        self.b_pawn6.set_captured(e_chess_captured.no)
        self.b_pawn7.set_position(position_start_const.b_pawn7_p)
        self.b_pawn7.set_captured(e_chess_captured.no)
        self.b_pawn8.set_position(position_start_const.b_pawn8_p)
        self.b_pawn8.set_captured(e_chess_captured.no)

        # Reset knights
        self.w_knight1.set_position(position_start_const.w_knight1_p)
        self.w_knight1.set_captured(e_chess_captured.no)
        self.w_knight2.set_position(position_start_const.w_knight2_p)
        self.w_knight2.set_captured(e_chess_captured.no)
        self.b_knight1.set_position(position_start_const.b_knight1_p)
        self.b_knight1.set_captured(e_chess_captured.no)
        self.b_knight2.set_position(position_start_const.b_knight2_p)
        self.b_knight2.set_captured(e_chess_captured.no)

        # Reset bishops
        self.w_bishop1.set_position(position_start_const.w_bishop1_p)
        self.w_bishop1.set_captured(e_chess_captured.no)
        self.w_bishop2.set_position(position_start_const.w_bishop2_p)
        self.w_bishop2.set_captured(e_chess_captured.no)
        self.b_bishop1.set_position(position_start_const.b_bishop1_p)
        self.b_bishop1.set_captured(e_chess_captured.no)
        self.b_bishop2.set_position(position_start_const.b_bishop2_p)
        self.b_bishop2.set_captured(e_chess_captured.no)

        # Reset rooks
        self.w_rook1.set_position(position_start_const.w_rook1_p)
        self.w_rook1.set_captured(e_chess_captured.no)
        self.w_rook2.set_position(position_start_const.w_rook2_p)
        self.w_rook2.set_captured(e_chess_captured.no)
        self.b_rook1.set_position(position_start_const.b_rook1_p)
        self.b_rook1.set_captured(e_chess_captured.no)
        self.b_rook2.set_position(position_start_const.b_rook2_p)
        self.b_rook2.set_captured(e_chess_captured.no)

        # Reset queens
        self.w_queen.set_position(position_start_const.w_queen_p)
        self.w_queen.set_captured(e_chess_captured.no)
        self.b_queen.set_position(position_start_const.b_queen_p)
        self.b_queen.set_captured(e_chess_captured.no)

        # Reset kings
        self.w_king.set_position(position_start_const.w_king_p)
        self.w_king.set_captured(e_chess_captured.no)
        self.b_king.set_position(position_start_const.b_king_p)
        self.b_king.set_captured(e_chess_captured.no)

    # Setzt eine Figur auf das Board
    def __set_piece_on_board(self, position: c_position, char: str):

        if ((len(char)!=1)):
            raise TypeError("Ungültiger Character eingegeben")

        self._board[position.linie][position.rang] = char

    # Liest alle Positionen der Figuren aus und fügt deren Char ins Board ein
    def set_all_pieces_on_board(self):

        # Set pawns on board
        self.__set_piece_on_board(self.w_pawn1.get_position(), self.w_pawn1.get_char())
        self.__set_piece_on_board(self.w_pawn2.get_position(), self.w_pawn2.get_char())
        self.__set_piece_on_board(self.w_pawn3.get_position(), self.w_pawn3.get_char())
        self.__set_piece_on_board(self.w_pawn4.get_position(), self.w_pawn4.get_char())
        self.__set_piece_on_board(self.w_pawn5.get_position(), self.w_pawn5.get_char())
        self.__set_piece_on_board(self.w_pawn6.get_position(), self.w_pawn6.get_char())
        self.__set_piece_on_board(self.w_pawn7.get_position(), self.w_pawn7.get_char())
        self.__set_piece_on_board(self.w_pawn8.get_position(), self.w_pawn8.get_char())

        self.__set_piece_on_board(self.b_pawn1.get_position(), self.b_pawn1.get_char())
        self.__set_piece_on_board(self.b_pawn2.get_position(), self.b_pawn2.get_char())
        self.__set_piece_on_board(self.b_pawn3.get_position(), self.b_pawn3.get_char())
        self.__set_piece_on_board(self.b_pawn4.get_position(), self.b_pawn4.get_char())
        self.__set_piece_on_board(self.b_pawn5.get_position(), self.b_pawn5.get_char())
        self.__set_piece_on_board(self.b_pawn6.get_position(), self.b_pawn6.get_char())
        self.__set_piece_on_board(self.b_pawn7.get_position(), self.b_pawn7.get_char())
        self.__set_piece_on_board(self.b_pawn8.get_position(), self.b_pawn8.get_char())

        # Set knights on board
        self.__set_piece_on_board(self.w_knight1.get_position(), self.w_knight1.get_char())
        self.__set_piece_on_board(self.w_knight2.get_position(), self.w_knight2.get_char())

        self.__set_piece_on_board(self.b_knight1.get_position(), self.b_knight1.get_char())
        self.__set_piece_on_board(self.b_knight2.get_position(), self.b_knight2.get_char())

        # Set bishops on board
        self.__set_piece_on_board(self.w_bishop1.get_position(), self.w_bishop1.get_char())
        self.__set_piece_on_board(self.w_bishop2.get_position(), self.w_bishop2.get_char())
        self.__set_piece_on_board(self.b_bishop1.get_position(), self.b_bishop1.get_char())
        self.__set_piece_on_board(self.b_bishop2.get_position(), self.b_bishop2.get_char())

        # Set rooks on board
        self.__set_piece_on_board(self.w_rook1.get_position(), self.w_rook1.get_char())
        self.__set_piece_on_board(self.w_rook2.get_position(), self.w_rook2.get_char())
        self.__set_piece_on_board(self.b_rook1.get_position(), self.b_rook1.get_char())
        self.__set_piece_on_board(self.b_rook2.get_position(), self.b_rook2.get_char())

        # Set queens on board
        self.__set_piece_on_board(self.w_queen.get_position(), self.w_queen.get_char())
        self.__set_piece_on_board(self.b_queen.get_position(), self.b_queen.get_char())

        #Set kings on board
        self.__set_piece_on_board(self.w_king.get_position(), self.w_king.get_char())
        self.__set_piece_on_board(self.b_king.get_position(), self.b_king.get_char())

    # Position der Figuren und auf dem Board werden zurückgesetzt
    def reset_board(self):
        for i in range(8):
            for i2 in range(8):
                self._board[i][i2] = " "

    # Return(t) die Schachfigur, die auf einer Position steht
    def find_piece_with_position(self, position: c_position) -> c_chess_piece:
        char = self._board[position.linie.value][position.rang.value]

        # Schaut nach dem Character der Figuren und sieht dann nach der Positionen der Figuren
        # mit diesem Character und return(t) die gefundene Figur
        match char:

            case e_chess_char.white_pawn:
                match position:

                    case self.w_pawn1.position:
                        return self.w_pawn1
                    
                    case self.w_pawn2.position:
                        return self.w_pawn2
                    
                    case self.w_pawn3.position:
                        return self.w_pawn3
                    
                    case self.w_pawn4.position:
                        return self.w_pawn4
                    
                    case self.w_pawn5.position:
                        return self.w_pawn5
                    
                    case self.w_pawn6.position:
                        return self.w_pawn6
                    
                    case self.w_pawn7.position:
                        return self.w_pawn7
                    
                    case self.w_pawn8.position:
                        return self.w_pawn8

            case e_chess_char.black_pawn:
                match position:

                    case self.b_pawn1.position:
                        return self.b_pawn1
                    
                    case self.b_pawn2.position:
                        return self.b_pawn2
                    
                    case self.b_pawn3.position:
                        return self.b_pawn3
                    
                    case self.b_pawn4.position:
                        return self.b_pawn4
                    
                    case self.b_pawn5.position:
                        return self.b_pawn5
                    
                    case self.b_pawn6.position:
                        return self.b_pawn6
                    
                    case self.b_pawn7.position:
                        return self.b_pawn7
                    
                    case self.b_pawn8.position:
                        return self.b_pawn8

            case e_chess_char.white_knight:
                match position:

                    case self.w_knight1.position:
                        return self.w_knight1
                    
                    case self.w_knight2.position:
                        return self.w_knight2

            case e_chess_char.black_knight:
                match position:

                    case self.b_knight1.position:
                        return self.b_knight1
                    
                    case self.b_knight2.position:
                        return self.b_knight2

            case e_chess_char.white_bishop:
                match position:

                    case self.w_bishop1.position:
                        return self.w_bishop1
                    
                    case self.w_bishop2.position:
                        return self.w_bishop2

            case e_chess_char.black_bishop:
                match position:

                    case self.b_bishop1.position:
                        return self.b_bishop1
                    
                    case self.b_bishop2.position:
                        return self.b_bishop2

            case e_chess_char.white_rook:
                match position:

                    case self.w_rook1.position:
                        return self.w_rook1
                    
                    case self.w_rook2.position:
                        return self.w_rook2

            case e_chess_char.black_rook:
                match position:

                    case self.b_rook1.position:
                        return self.b_rook1
                    
                    case self.b_rook2.position:
                        return self.b_rook2

            case e_chess_char.white_queen:
                return self.w_queen

            case e_chess_char.black_queen:
                return self.b_queen

            case e_chess_char.white_king:
                return self.w_king

            case e_chess_char.black_king:
                return self.b_king
            
            
            case _:
                    raise TypeError("Ungültigen Character eingegeben")

    def is_piece_on_position(self, position: c_position) -> bool:
        if self._board[position._spalte.value][position._zeile.value] != e_chess_char.space.value:
            return 1
        return 0
    
    # TODO name, public/private usw anpassen wie nötig
    # Verschiebt Figur auf dem Schachfeld und ändert die Position der jeweiligen Figur
    # Wenn Figur geschlagen wird, wird _captured der Figur gesetzt
    # Wenn Figur geschlagen wird, wird der Wert der Figur - des Figurtypen - return(t)
    def change_piece_position(self, new_position: c_position, piece: e_chess_piece) -> int:
        char = None
        value = 0
        old_position = None 
        
        # Wenn eine Figur auf der neuen Position ist, wird captured gesetzt und value wird auf dessen Wert gesetzt
        if self._board[new_position._spalte.value][new_position._zeile.value] != " ":
            geschlagen_piece = self.find_piece_with_position(new_position)
            geschlagen_piece.set_captured(e_chess_captured.yes)
            value = geschlagen_piece.get_typ().value
        
        # Figurposition wird auf new_position gesetzt, char Wert wird auf das Zeichen der Figur
        match piece:

            # case white pawns
            case e_chess_piece.w_pawn1_e:
                self.w_pawn1.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn1.get_position()
            
            case e_chess_piece.w_pawn2_e:
                self.w_pawn2.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn2.get_position()

            case e_chess_piece.w_pawn3_e:
                self.w_pawn3.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn3.get_position()

            case e_chess_piece.w_pawn4_e:
                self.w_pawn4.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn4.get_position()

            case e_chess_piece.w_pawn5_e:
                self.w_pawn5.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn5.get_position()

            case e_chess_piece.w_pawn6_e:
                self.w_pawn6.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn6.get_position()

            case e_chess_piece.w_pawn7_e:
                self.w_pawn7.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn7.get_position()

            case e_chess_piece.w_pawn8_e:
                self.w_pawn8.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn8.get_position()

            # case black pawns
            case e_chess_piece.b_pawn1_e:
                self.b_pawn1.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn1.get_position()
            
            case e_chess_piece.b_pawn2_e:
                self.w_pawn2.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn2.get_position()

            case e_chess_piece.b_pawn3_e:
                self.b_pawn3.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn3.get_position()

            case e_chess_piece.b_pawn4_e:
                self.w_pawn4.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn4.get_position()

            case e_chess_piece.b_pawn5_e:
                self.b_pawn5.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn5.get_position()

            case e_chess_piece.b_pawn6_e:
                self.b_pawn6.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn6.get_position()

            case e_chess_piece.b_pawn7_e:
                self.b_pawn7.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn7.get_position()

            case e_chess_piece.b_pawn8_e:
                self.b_pawn8.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn8.get_position()

            # case knights
            case e_chess_piece.w_knight1_e:
                self.w_knight1.set_position(new_position)
                char = e_chess_char.white_knight.value
                old_position = self.w_knight1.get_position()
            
            case e_chess_piece.w_knight2_e:
                self.w_knight1.set_position(new_position)
                char = e_chess_char.white_knight.value
                old_position = self.w_knight2.get_position()

            case e_chess_piece.b_knight1_e:
                self.b_knight1.set_position(new_position)
                char = e_chess_char.black_knight.value
                old_position = self.b_knight1.get_position()

            case e_chess_piece.b_knight2_e:
                self.b_knight1.set_position(new_position)
                char = e_chess_char.black_knight.value
                old_position = self.b_knight2.get_position()

            # case bishops
            case e_chess_piece.w_bishop1_e:
                self.w_bishop1.set_position(new_position)
                char = e_chess_char.white_bishop.value
                old_position = self.w_bishop1.get_position()

            case e_chess_piece.w_bishop2_e:
                self.w_bishop2.set_position(new_position)
                char = e_chess_char.white_bishop.value
                old_position = self.w_bishop2.get_position()

            case e_chess_piece.b_bishop1_e:
                self.b_bishop1.set_position(new_position)
                char = e_chess_char.black_bishop.value
                old_position = self.b_bishop1.get_position()

            case e_chess_piece.b_bishop2_e:
                self.b_bishop2.set_position(new_position)
                char = e_chess_char.black_bishop.value
                old_position = self.b_bishop2.get_position()

            # case rooks
            case e_chess_piece.w_rook1_e:
                self.w_rook1.set_position(new_position)
                char = e_chess_char.white_rook.value
                old_position = self.w_rook1.get_position()

            case e_chess_piece.w_rook2_e:
                self.w_rook2.set_position(new_position)
                char = e_chess_char.white_rook.value
                old_position = self.w_rook2.get_position()

            case e_chess_piece.b_rook1_e:
                self.b_rook1.set_position(new_position)
                char = e_chess_char.black_rook.value
                old_position = self.b_rook1.get_position()

            case e_chess_piece.b_rook2_e:
                self.b_rook2.set_position(new_position)
                char = e_chess_char.black_rook.value
                old_position = self.b_rook2.get_position()
            
            # case queens
            case e_chess_piece.w_queen_e:
                self.w_queen.set_position(new_position)
                char = e_chess_char.white_queen.value
                old_position = self.w_queen.get_position()

            case e_chess_piece.b_queen_e:
                self.b_queen.set_position(new_position)
                char = e_chess_char.black_queen.value
                old_position = self.b_queen.get_position()

            # case kings
            case e_chess_piece.w_king_e:
                self.w_king.set_position(new_position)
                char = e_chess_char.white_king.value
                old_position = self.w_king.get_position()

            case e_chess_piece.b_king_e:
                self.b_king.set_position(new_position)
                char = e_chess_char.black_king.value
                old_position = self.b_king.get_position()

            case _:
                raise TypeError("Ungültige Figur eingegeben")


        self._board[old_position._spalte.value][old_position._zeile.value] = " "
        self._board[new_position._spalte.value][new_position._zeile.value] = char

        return value

    def is_piece_move_possible(self, new_position: c_position, piece: e_chess_piece, latest_opponent_move: c_move) -> bool:
        check = None
        match piece:

            # case white pawns
            case e_chess_piece.w_pawn1_e:
                check = self.w_pawn1.laufen_possible()
                
            
            case e_chess_piece.w_pawn2_e:
                self.w_pawn2.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn2.get_position()

            case e_chess_piece.w_pawn3_e:
                self.w_pawn3.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn3.get_position()

            case e_chess_piece.w_pawn4_e:
                self.w_pawn4.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn4.get_position()

            case e_chess_piece.w_pawn5_e:
                self.w_pawn5.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn5.get_position()

            case e_chess_piece.w_pawn6_e:
                self.w_pawn6.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn6.get_position()

            case e_chess_piece.w_pawn7_e:
                self.w_pawn7.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn7.get_position()

            case e_chess_piece.w_pawn8_e:
                self.w_pawn8.set_position(new_position)
                char = e_chess_char.white_pawn.value
                old_position = self.w_pawn8.get_position()

            # case black pawns
            case e_chess_piece.b_pawn1_e:
                self.b_pawn1.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn1.get_position()
            
            case e_chess_piece.b_pawn2_e:
                self.w_pawn2.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn2.get_position()

            case e_chess_piece.b_pawn3_e:
                self.b_pawn3.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn3.get_position()

            case e_chess_piece.b_pawn4_e:
                self.w_pawn4.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn4.get_position()

            case e_chess_piece.b_pawn5_e:
                self.b_pawn5.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn5.get_position()

            case e_chess_piece.b_pawn6_e:
                self.b_pawn6.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn6.get_position()

            case e_chess_piece.b_pawn7_e:
                self.b_pawn7.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn7.get_position()

            case e_chess_piece.b_pawn8_e:
                self.b_pawn8.set_position(new_position)
                char = e_chess_char.black_pawn.value
                old_position = self.b_pawn8.get_position()

            # case knights
            case e_chess_piece.w_knight1_e:
                self.w_knight1.set_position(new_position)
                char = e_chess_char.white_knight.value
                old_position = self.w_knight1.get_position()
            
            case e_chess_piece.w_knight2_e:
                self.w_knight1.set_position(new_position)
                char = e_chess_char.white_knight.value
                old_position = self.w_knight2.get_position()

            case e_chess_piece.b_knight1_e:
                self.b_knight1.set_position(new_position)
                char = e_chess_char.black_knight.value
                old_position = self.b_knight1.get_position()

            case e_chess_piece.b_knight2_e:
                self.b_knight1.set_position(new_position)
                char = e_chess_char.black_knight.value
                old_position = self.b_knight2.get_position()

            # case bishops
            case e_chess_piece.w_bishop1_e:
                self.w_bishop1.set_position(new_position)
                char = e_chess_char.white_bishop.value
                old_position = self.w_bishop1.get_position()

            case e_chess_piece.w_bishop2_e:
                self.w_bishop2.set_position(new_position)
                char = e_chess_char.white_bishop.value
                old_position = self.w_bishop2.get_position()

            case e_chess_piece.b_bishop1_e:
                self.b_bishop1.set_position(new_position)
                char = e_chess_char.black_bishop.value
                old_position = self.b_bishop1.get_position()

            case e_chess_piece.b_bishop2_e:
                self.b_bishop2.set_position(new_position)
                char = e_chess_char.black_bishop.value
                old_position = self.b_bishop2.get_position()

            # case rooks
            case e_chess_piece.w_rook1_e:
                self.w_rook1.set_position(new_position)
                char = e_chess_char.white_rook.value
                old_position = self.w_rook1.get_position()

            case e_chess_piece.w_rook2_e:
                self.w_rook2.set_position(new_position)
                char = e_chess_char.white_rook.value
                old_position = self.w_rook2.get_position()

            case e_chess_piece.b_rook1_e:
                self.b_rook1.set_position(new_position)
                char = e_chess_char.black_rook.value
                old_position = self.b_rook1.get_position()

            case e_chess_piece.b_rook2_e:
                self.b_rook2.set_position(new_position)
                char = e_chess_char.black_rook.value
                old_position = self.b_rook2.get_position()
            
            # case queens
            case e_chess_piece.w_queen_e:
                self.w_queen.set_position(new_position)
                char = e_chess_char.white_queen.value
                old_position = self.w_queen.get_position()

            case e_chess_piece.b_queen_e:
                self.b_queen.set_position(new_position)
                char = e_chess_char.black_queen.value
                old_position = self.b_queen.get_position()

            # case kings
            case e_chess_piece.w_king_e:
                self.w_king.set_position(new_position)
                char = e_chess_char.white_king.value
                old_position = self.w_king.get_position()

            case e_chess_piece.b_king_e:
                self.b_king.set_position(new_position)
                char = e_chess_char.black_king.value
                old_position = self.b_king.get_position()

            case _:
                raise TypeError("Ungültige Figur eingegeben")

    def is_piece_move_allowed(self, position: c_position, new_position: c_position, piece: e_chess_piece) -> bool:
        return 0

    def is_piece_move_possible_and_allowed(self, position: c_position, new_position: c_position, piece: e_chess_piece) -> bool:
        return 0
    
    def move_piece_on_board_and_piece_position(self, move: c_move) -> bool:
        # TODO
        return 0
                                               

    
    # Get Funktionen
    def get_board(self) -> list:
        return self._board
    
    def how_many_pieces_can_do_this_move(self, move_type: e_move_type, farbe: e_chess_color) -> int:
        count = None
        match move_type:
            #pawn
            case e_move_type.pawn_file_rank | e_move_type.pawn_file_rank_check | e_move_type.pawn_file_rank_check_mate | e_move_type.pawn_file_rank_promote | e_move_type.pawn_schlagen_file_rank | e_move_type.pawn_file_rank_promote_check | e_move_type.pawn_file_rank_promote_check_mate | e_move_type.pawn_schlagen_file_rank_check | e_move_type.pawn_schlagen_file_rank_check_mate | e_move_type.pawn_schlagen_file_rank_promote | e_move_type.pawn_schlagen_file_rank_promote_check | e_move_type.pawn_schlagen_file_rank_promote_check_mate:
                
                if farbe == e_chess_color.black:
                    if self.b_pawn1.laufen_possible():
                        count += 1
                    if self.b_pawn2.laufen_possible():
                        count += 1
                    if self.b_pawn3.laufen_possible():
                        count += 1
                    if self.b_pawn4.laufen_possible():
                        count += 1
                    if self.b_pawn5.laufen_possible():
                        count += 1
                    if self.b_pawn6.laufen_possible():
                        count += 1
                    if self.b_pawn7.laufen_possible():
                        count += 1
                    if self.b_pawn8.laufen_possible():
                        count += 1
                elif farbe == e_chess_color.white:
                    if self.w_pawn1.laufen_possible():
                        count += 1
                    if self.w_pawn2.laufen_possible():
                        count += 1
                    if self.w_pawn3.laufen_possible():
                        count += 1
                    if self.w_pawn4.laufen_possible():
                        count += 1
                    if self.w_pawn5.laufen_possible():
                        count += 1
                    if self.w_pawn6.laufen_possible():
                        count += 1
                    if self.w_pawn7.laufen_possible():
                        count += 1
                    if self.w_pawn8.laufen_possible():
                        count += 1
                else:
                    raise TypeError("Falsche Farbe")
            #knight
            case e_move_type.knight_file_rank | e_move_type.knight_file_rank_check | e_move_type.knight_file_rank_check_mate | e_move_type.knight_schlagen_file_rank | e_move_type.knight_schlagen_file_rank_check | e_move_type.knight_schlagen_file_rank_check_mate:
                if farbe == e_chess_color.black:
                    if self.b_knight1.laufen_possible():
                        count += 1
                    if self.b_knight2.laufen_possible():
                        count += 1
                elif farbe == e_chess_color.white:
                    if self.w_knight1.laufen_possible():
                        count += 1
                    if self.w_knight2.laufen_possible():
                        count += 1
                else:
                    raise TypeError("Falsche Farbe")
            #bishop
            case e_move_type.bishop_file_rank | e_move_type.bishop_file_rank_check | e_move_type.bishop_file_rank_check_mate | e_move_type.bishop_schlagen_file_rank | e_move_type.bishop_schlagen_file_rank_check | e_move_type.bishop_schlagen_file_rank_check_mate:
                if farbe == e_chess_color.black:
                    if self.b_bishop1.laufen_possible():
                        count += 1
                    if self.b_bishop2.laufen_possible():
                        count += 1
                elif farbe == e_chess_color.white:
                    if self.w_bishop1.laufen_possible():
                        count += 1
                    if self.w_bishop2.laufen_possible():
                        count += 1
                else:
                    raise TypeError("Falsche Farbe")
            #rook
            case e_move_type.rook_file_rank | e_move_type.rook_file_rank_check | e_move_type.rook_file_rank_check_mate | e_move_type.rook_schlagen_file_rank | e_move_type.rook_schlagen_file_rank_check | e_move_type.rook_schlagen_file_rank_check_mate:
                if farbe == e_chess_color.black:
                    if self.b_rook1.laufen_possible():
                        count += 1
                    if self.b_rook2.laufen_possible():
                        count += 1
                elif farbe == e_chess_color.white:
                    if self.w_rook1.laufen_possible():
                        count += 1
                    if self.w_rook2.laufen_possible():
                        count += 1
                else:
                    raise TypeError("Falsche Farbe")
            #queen
            case e_move_type.queen_file_rank | e_move_type.queen_file_rank_check | e_move_type.queen_file_rank_check_mate | e_move_type.queen_schlagen_file_rank | e_move_type.queen_schlagen_file_rank_check | e_move_type.queen_schlagen_file_rank_check_mate:
                return 1
            #king
            case e_move_type.king_file_rank | e_move_type.king_file_rank_check | e_move_type.king_file_rank_check_mate | e_move_type.king_schlagen_file_rank | e_move_type.king_schlagen_file_rank_check | e_move_type.king_schlagen_file_rank_check_mate:
                return 1

    def is_check(self, new_position: c_position, piece_type: e_chess_typ) -> bool:
        







