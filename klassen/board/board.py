from figures.pawn import c_pawn
from figures.knight import c_knight
from figures.bishop import c_bishop
from figures.rook import c_rook
from figures.queen import c_queen
from figures.king import c_king
from figures.chess_piece import c_chess_piece
from klassen.board.figures.enums.position_start_const_enum import position_start_const
from board.figures.enums.chess_color_enum import e_chess_color
from board.figures.enums.chess_captured_enum import e_chess_captured
from board.figures.enums.chess_pieces_enum import e_chess_piece
from board.figures.enums.chess_char_enum import e_chess_char
from board.position_and_position_enum import c_position
from klassen.enums.move_enum import e_move


class board():

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

    #-------------------------------------------------------------------
    # Get und Set Funktionen
    #-------------------------------------------------------------------

    # get_char()        
    # get_captured()    # set_captured()
    # get_position()    # set_position()
    # get_farbe()
    # get_typ()
    #------------------------------------------------------------------------

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
    def set_piece_on_board(self, position: c_position, char: str):

        if ((len(char)!=1)):
            raise TypeError("Ungültiger Character eingegeben")

        self._board[position.linie][position.rang] = char

    # Liest alle Positionen der Figuren aus und fügt deren Char ins Board ein
    def set_all_pieces_on_board(self):

        # Set pawns on board
        self.set_piece_on_board(self.w_pawn1.get_position(), self.w_pawn1.get_char())
        self.set_piece_on_board(self.w_pawn2.get_position(), self.w_pawn2.get_char())
        self.set_piece_on_board(self.w_pawn3.get_position(), self.w_pawn3.get_char())
        self.set_piece_on_board(self.w_pawn4.get_position(), self.w_pawn4.get_char())
        self.set_piece_on_board(self.w_pawn5.get_position(), self.w_pawn5.get_char())
        self.set_piece_on_board(self.w_pawn6.get_position(), self.w_pawn6.get_char())
        self.set_piece_on_board(self.w_pawn7.get_position(), self.w_pawn7.get_char())
        self.set_piece_on_board(self.w_pawn8.get_position(), self.w_pawn8.get_char())

        self.set_piece_on_board(self.b_pawn1.get_position(), self.b_pawn1.get_char())
        self.set_piece_on_board(self.b_pawn2.get_position(), self.b_pawn2.get_char())
        self.set_piece_on_board(self.b_pawn3.get_position(), self.b_pawn3.get_char())
        self.set_piece_on_board(self.b_pawn4.get_position(), self.b_pawn4.get_char())
        self.set_piece_on_board(self.b_pawn5.get_position(), self.b_pawn5.get_char())
        self.set_piece_on_board(self.b_pawn6.get_position(), self.b_pawn6.get_char())
        self.set_piece_on_board(self.b_pawn7.get_position(), self.b_pawn7.get_char())
        self.set_piece_on_board(self.b_pawn8.get_position(), self.b_pawn8.get_char())

        # Set knights on board
        self.set_piece_on_board(self.w_knight1.get_position(), self.w_knight1.get_char())
        self.set_piece_on_board(self.w_knight2.get_position(), self.w_knight2.get_char())

        self.set_piece_on_board(self.b_knight1.get_position(), self.b_knight1.get_char())
        self.set_piece_on_board(self.b_knight2.get_position(), self.b_knight2.get_char())

        # Set bishops on board
        self.set_piece_on_board(self.w_bishop1.get_position(), self.w_bishop1.get_char())
        self.set_piece_on_board(self.w_bishop2.get_position(), self.w_bishop2.get_char())
        self.set_piece_on_board(self.b_bishop1.get_position(), self.b_bishop1.get_char())
        self.set_piece_on_board(self.b_bishop2.get_position(), self.b_bishop2.get_char())

        # Set rooks on board
        self.set_piece_on_board(self.w_rook1.get_position(), self.w_rook1.get_char())
        self.set_piece_on_board(self.w_rook2.get_position(), self.w_rook2.get_char())
        self.set_piece_on_board(self.b_rook1.get_position(), self.b_rook1.get_char())
        self.set_piece_on_board(self.b_rook2.get_position(), self.b_rook2.get_char())

        # Set queens on board
        self.set_piece_on_board(self.w_queen.get_position(), self.w_queen.get_char())
        self.set_piece_on_board(self.b_queen.get_position(), self.b_queen.get_char())

        #Set kings on board
        self.set_piece_on_board(self.w_king.get_position(), self.w_king.get_char())
        self.set_piece_on_board(self.b_king.get_position(), self.b_king.get_char())

    # Position der Figuren und auf dem Board werden zurückgesetzt
    def reset_board(self):
        for i in range(8):
            for i2 in range(8):
                self._board[i][i2] = " "

        self.reset_pieces()
        self.set_all_pieces_on_board()

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

    # Verschiebt Figur auf dem Schachfeld und ändert die Position der jeweiligen Figur
    # Wenn Figur geschlagen wird, wird _captured der Figur gesetzt
    # Wenn Figur geschlagen wird, wird der Wert der Figur - des Figurtypen - return(t)
    def change_piece_position(self, position: c_position, new_position: c_position, piece: e_chess_piece) -> int:
        char = None
        value = 0
        
        # Wenn eine Figur auf der neuen Position ist, wird captured gesetzt und value wird auf dessen Wert gesetzt
        if self._board[new_position.linie.value][new_position.rang.value] != " ":
            piece = self.find_piece_with_position()
            piece.set_captured(e_chess_captured.yes)
            value = piece.get_typ().value
        
        # Figurposition wird auf new_position gesetzt, char Wert wird auf das Zeichen der Figur
        match piece:

            # case white pawns
            case e_chess_piece.w_pawn1_e:
                self.w_pawn1.set_position(new_position)
                char = e_chess_char.white_pawn.value
            
            case e_chess_piece.w_pawn2_e:
                self.w_pawn2.set_position(new_position)
                char = e_chess_char.white_pawn.value

            case e_chess_piece.w_pawn3_e:
                self.w_pawn3.set_position(new_position)
                char = e_chess_char.white_pawn.value

            case e_chess_piece.w_pawn4_e:
                self.w_pawn4.set_position(new_position)
                char = e_chess_char.white_pawn.value

            case e_chess_piece.w_pawn5_e:
                self.w_pawn5.set_position(new_position)
                char = e_chess_char.white_pawn.value

            case e_chess_piece.w_pawn6_e:
                self.w_pawn6.set_position(new_position)
                char = e_chess_char.white_pawn.value

            case e_chess_piece.w_pawn7_e:
                self.w_pawn7.set_position(new_position)
                char = e_chess_char.white_pawn.value

            case e_chess_piece.w_pawn8_e:
                self.w_pawn8.set_position(new_position)
                char = e_chess_char.white_pawn.value

            # case black pawns
            case e_chess_piece.b_pawn1_e:
                self.b_pawn1.set_position(new_position)
                char = e_chess_char.black_pawn.value
            
            case e_chess_piece.b_pawn2_e:
                self.w_pawn2.set_position(new_position)
                char = e_chess_char.black_pawn.value

            case e_chess_piece.b_pawn3_e:
                self.b_pawn3.set_position(new_position)
                char = e_chess_char.black_pawn.value

            case e_chess_piece.b_pawn4_e:
                self.w_pawn4.set_position(new_position)
                char = e_chess_char.black_pawn.value

            case e_chess_piece.b_pawn5_e:
                self.b_pawn5.set_position(new_position)
                char = e_chess_char.black_pawn.value

            case e_chess_piece.b_pawn6_e:
                self.b_pawn6.set_position(new_position)
                char = e_chess_char.black_pawn.value

            case e_chess_piece.b_pawn7_e:
                self.b_pawn7.set_position(new_position)
                char = e_chess_char.black_pawn.value

            case e_chess_piece.b_pawn8_e:
                self.b_pawn8.set_position(new_position)
                char = e_chess_char.black_pawn.value

            # case knights
            case e_chess_piece.w_knight1_e:
                self.w_knight1.set_position(new_position)
                char = e_chess_char.white_knight.value
            
            case e_chess_piece.w_knight2_e:
                self.w_knight1.set_position(new_position)
                char = e_chess_char.white_knight.value

            case e_chess_piece.b_knight1_e:
                self.b_knight1.set_position(new_position)
                char = e_chess_char.black_knight.value

            case e_chess_piece.b_knight2_e:
                self.b_knight1.set_position(new_position)
                char = e_chess_char.black_knight.value

            # case bishops
            case e_chess_piece.w_bishop1_e:
                self.w_bishop1.set_position(new_position)
                char = e_chess_char.white_bishop.value

            case e_chess_piece.w_bishop2_e:
                self.w_bishop2.set_position(new_position)
                char = e_chess_char.white_bishop.value

            case e_chess_piece.b_bishop1_e:
                self.b_bishop1.set_position(new_position)
                char = e_chess_char.black_bishop.value

            case e_chess_piece.b_bishop2_e:
                self.b_bishop2.set_position(new_position)
                char = e_chess_char.black_bishop.value

            # case rooks
            case e_chess_piece.w_rook1_e:
                self.w_rook1.set_position(new_position)
                char = e_chess_char.white_rook.value

            case e_chess_piece.w_rook2_e:
                self.w_rook2.set_position(new_position)
                char = e_chess_char.white_rook.value

            case e_chess_piece.b_rook1_e:
                self.b_rook1.set_position(new_position)
                char = e_chess_char.black_rook.value

            case e_chess_piece.b_rook2_e:
                self.b_rook2.set_position(new_position)
                char = e_chess_char.black_rook.value
            
            # case queens
            case e_chess_piece.w_queen_e:
                self.w_queen.set_position(new_position)
                char = e_chess_char.white_queen.value

            case e_chess_piece.b_queen_e:
                self.b_queen.set_position(new_position)
                char = e_chess_char.black_queen.value

            # case kings
            case e_chess_piece.w_king_e:
                self.w_king.set_position(new_position)
                char = e_chess_char.white_king.value

            case e_chess_piece.b_king_e:
                self.b_king.set_position(new_position)
                char = e_chess_char.black_king.value

            case _:
                raise TypeError("Ungültige Figur eingegeben")


        self._board[position.linie.value][position.rang.value] = " "
        self._board[new_position.linie.value][new_position.rang.value] = char

        return value

    
    def make_a_move(self, move: e_move):
        return 0












