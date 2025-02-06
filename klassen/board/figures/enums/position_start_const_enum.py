from board.position_and_position_enum import c_position
from board.position_and_position_enum import e_spalte
from board.position_and_position_enum import e_zeile

class position_start_const():
    #-----------------------------------------------------
    #------------------------------------------------------
    w_pawn1_p = c_position(e_spalte.l_a, e_zeile.r_2)
    w_pawn2_p = c_position(e_spalte.l_b, e_zeile.r_2)
    w_pawn3_p = c_position(e_spalte.l_c, e_zeile.r_2)
    w_pawn4_p = c_position(e_spalte.l_d, e_zeile.r_2)
    w_pawn5_p = c_position(e_spalte.l_e, e_zeile.r_2)
    w_pawn6_p = c_position(e_spalte.l_f, e_zeile.r_2)
    w_pawn7_p = c_position(e_spalte.l_g, e_zeile.r_2)
    w_pawn8_p = c_position(e_spalte.l_h, e_zeile.r_2)

    b_pawn1_p = c_position(e_spalte.l_h, e_zeile.r_7)
    b_pawn2_p = c_position(e_spalte.l_g, e_zeile.r_7)
    b_pawn3_p = c_position(e_spalte.l_f, e_zeile.r_7)
    b_pawn4_p = c_position(e_spalte.l_e, e_zeile.r_7)
    b_pawn5_p = c_position(e_spalte.l_d, e_zeile.r_7)
    b_pawn6_p = c_position(e_spalte.l_c, e_zeile.r_7)
    b_pawn7_p = c_position(e_spalte.l_b, e_zeile.r_7)
    b_pawn8_p = c_position(e_spalte.l_a, e_zeile.r_7)
    #-----------------------------------------------------
    #-----------------------------------------------------

    #-----------------------------------------------------
    #-----------------------------------------------------
    w_knight1_p = c_position(e_spalte.l_b, e_zeile.r_1)
    w_knight2_p = c_position(e_spalte.l_g, e_zeile.r_1)

    b_knight1_p = c_position(e_spalte.l_g, e_zeile.r_8)
    b_knight2_p = c_position(e_spalte.l_b, e_zeile.r_8)
    #-----------------------------------------------------
    #-----------------------------------------------------

    #-----------------------------------------------------
    #-----------------------------------------------------
    w_bishop1_p = c_position(e_spalte.l_c, e_zeile.r_1)
    w_bishop2_p = c_position(e_spalte.l_f, e_zeile.r_1)

    b_bishop1_p = c_position(e_spalte.l_f, e_zeile.r_8)
    b_bishop2_p = c_position(e_spalte.l_c, e_zeile.r_8)
    #-----------------------------------------------------
    #-----------------------------------------------------

    #-----------------------------------------------------
    #-----------------------------------------------------
    w_rook1_p = c_position(e_spalte.l_a, e_zeile.r_1)
    w_rook2_p = c_position(e_spalte.l_h, e_zeile.r_1)

    b_rook1_p = c_position(e_spalte.l_h, e_zeile.r_8)
    b_rook2_p = c_position(e_spalte.l_a, e_zeile.r_8)
    #-----------------------------------------------------
    #-----------------------------------------------------

    #-----------------------------------------------------
    #-----------------------------------------------------
    w_queen_p = c_position(e_spalte.l_d, e_zeile.r_1)
    
    b_queen_p = c_position(e_spalte.l_d, e_zeile.r_8)
    #-----------------------------------------------------
    #-----------------------------------------------------

    #-----------------------------------------------------
    #-----------------------------------------------------
    w_king_p = c_position(e_spalte.l_e, e_zeile.r_1)

    b_king_p = c_position(e_spalte.l_e, e_zeile.r_8)
    #-----------------------------------------------------
    #-----------------------------------------------------

    