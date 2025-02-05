from figures import c_pawn, c_knight, c_bishop, c_rook, c_queen, c_king
from figures.position_start_const import position_start_const
from board.figures.enums.chess_color_enum import e_chess_color
from board.figures.enums.chess_captured_enum import e_chess_captured
from board.position_and_position_enum import c_position


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

    def set_piece_on_board(self, position, char):

        if (not(isinstance(position, c_position))):
            raise TypeError("Ungültige Position eingegeben")
        
        if (not(isinstance(char, str)) or (len(char)!=1)):
            raise TypeError("Ungültiger Character eingegeben")

        self._board[position.linie][position.rang] = char

    def set_all_pieces_on_board(self):

        self.w_pawn1.get_position()
        self.w_pawn1.get_char()


    def reset_board(self):
        for i in range(8):
            for i2 in range(8):
                self._board[i][i2] = " "

        self.reset_pieces()

        self.set_all_pieces_on_board()













