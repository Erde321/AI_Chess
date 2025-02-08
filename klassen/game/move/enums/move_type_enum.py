from enum import Enum

class e_move_type(Enum):
    notdef = 0
    # Bauernzüge
    # a4
    pawn_file_rank = 1
    # a4+
    pawn_file_rank_check = 2
    # a4#
    pawn_file_rank_check_mate = 3
    # a4=Q
    pawn_file_rank_promote = 4
    # axb5
    pawn_schlagen_file_rank = 5
    # a8=Q+
    pawn_file_rank_promote_check = 6
    # a8=Q#
    pawn_file_rank_promote_check_mate = 7
    # exd6+
    pawn_schlagen_file_rank_check = 8
    # exd6#
    pawn_schlagen_file_rank_check_mate = 9
    # exd8=Q
    pawn_schlagen_file_rank_promote = 10
    # exd8=Q+
    pawn_schlagen_file_rank_promote_check = 11
    # exd8=Q#
    pawn_schlagen_file_rank_promote_check_mate = 12

    # Springerzüge
    # Nf3
    knight_file_rank = 13
    # Nf3+
    knight_file_rank_check = 14
    # Nf3#
    knight_file_rank_check_mate = 15
    # Ncb5
    knight_file_file_rank = 16
    # N5d4
    knight_rank_file_rank = 17
    # Nxg6
    knight_schlagen_file_rank = 18
    # Nxe5+
    knight_schlagen_file_rank_check = 19
    # Nxe5#
    knight_schlagen_file_rank_check_mate = 20
    # Nbd2+
    knight_file_file_rank_check = 21
    # Nbd2#
    knight_file_file_rank_check_mate = 22
    # N1f3+
    knight_rank_file_rank_check = 23
    # N1f3#
    knight_rank_file_rank_check_mate = 24
    # Nfxd4+
    knight_file_schlagen_file_rank_check = 25
    # Nfxd4#
    knight_file_schlagen_file_rank_check_mate = 26
    # N1xd4+
    knight_rank_schlagen_file_rank_check = 27
    # N1xd4#
    knight_rank_schlagen_file_rank_check_mate = 28

    # Alle Läuferzüge
    bishop_file_rank = 29
    bishop_file_rank_check = 30
    bishop_file_rank_check_mate = 31
    bishop_file_file_rank = 32
    bishop_rank_file_rank = 33
    bishop_schlagen_file_rank = 34
    bishop_schlagen_file_rank_check = 35
    bishop_schlagen_file_rank_check_mate = 36
    bishop_file_file_rank_check = 37
    bishop_file_file_rank_check_mate = 38
    bishop_rank_file_rank_check = 39
    bishop_rank_file_rank_check_mate = 40
    bishop_file_schlagen_file_rank_check = 41
    bishop_file_schlagen_file_rank_check_mate = 42
    bishop_rank_schlagen_file_rank_check = 43
    bishop_rank_schlagen_file_rank_check_mate = 44

    # Alle Turmzüge
    rook_file_rank = 45
    rook_file_rank_check = 46
    rook_file_rank_check_mate = 47
    rook_file_file_rank = 48
    rook_rank_file_rank = 49
    rook_schlagen_file_rank = 50
    rook_schlagen_file_rank_check = 51
    rook_schlagen_file_rank_check_mate = 52
    rook_file_file_rank_check = 53
    rook_file_file_rank_check_mate = 54
    rook_rank_file_rank_check = 55
    rook_rank_file_rank_check_mate = 56
    rook_file_schlagen_file_rank_check = 57
    rook_file_schlagen_file_rank_check_mate = 58
    rook_rank_schlagen_file_rank_check = 59
    rook_rank_schlagen_file_rank_check_mate = 60

    # Alle Damenzüge
    queen_file_rank = 61
    queen_file_rank_check = 62
    queen_file_rank_check_mate = 63
    queen_file_file_rank = 64
    queen_rank_file_rank = 65
    queen_schlagen_file_rank = 66
    queen_schlagen_file_rank_check = 67
    queen_schlagen_file_rank_check_mate = 68
    queen_file_file_rank_check = 69
    queen_file_file_rank_check_mate = 70
    queen_rank_file_rank_check = 71
    queen_rank_file_rank_check_mate = 72
    queen_file_schlagen_file_rank_check = 73
    queen_file_schlagen_file_rank_check_mate = 74
    queen_rank_schlagen_file_rank_check = 75
    queen_rank_schlagen_file_rank_check_mate = 76

    # Alle Königzüge
    # Ka2
    king_file_rank = 78
    king_file_rank_check = 79
    king_file_rank_check_mate = 80
    king_schlagen_file_rank = 81
    king_schlagen_file_rank_check = 82
    king_schlagen_file_rank_check_mate = 83

    # Alle Rochezüge
    roche = 84
    roche_check = 85
    roche_check_mate = 86
    roche_long = 87
    roche_long_check = 88
    roche_long_check_mate = 89