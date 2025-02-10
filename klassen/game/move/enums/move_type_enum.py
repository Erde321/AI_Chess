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
    # Nf1d4
    knight_file_rank_file_rank = 25
    # Nfxd4+
    knight_file_schlagen_file_rank_check = 26
    # Nfxd4#
    knight_file_schlagen_file_rank_check_mate = 27
    # N1xd4+
    knight_rank_schlagen_file_rank_check = 28
    # N1xd4#
    knight_rank_schlagen_file_rank_check_mate = 29
    # Nf1d4+
    knight_file_rank_file_rank_check = 30
    # Nf1d4#
    knight_file_rank_file_rank_check_mate = 31
    # Nf1xd4
    knight_file_rank_schlagen_file_rank = 32
    # Nf1xd4+
    knight_file_rank_schlagen_file_rank_check = 33
    # Nf1xd4#
    knight_file_rank_schlagen_file_rank_check_mate = 34

    # Alle Läuferzüge
    bishop_file_rank = 35
    bishop_file_rank_check = 36
    bishop_file_rank_check_mate = 37
    bishop_file_file_rank = 38
    bishop_rank_file_rank = 39
    bishop_schlagen_file_rank = 40
    bishop_schlagen_file_rank_check = 41
    bishop_schlagen_file_rank_check_mate = 42
    bishop_file_file_rank_check = 43
    bishop_file_file_rank_check_mate = 44
    bishop_rank_file_rank_check = 45
    bishop_rank_file_rank_check_mate = 46
    bishop_file_rank_file_rank = 47
    bishop_file_schlagen_file_rank_check = 48
    bishop_file_schlagen_file_rank_check_mate = 49
    bishop_rank_schlagen_file_rank_check = 50
    bishop_rank_schlagen_file_rank_check_mate = 51
    bishop_file_rank_file_rank_check = 52
    bishop_file_rank_file_rank_check_mate = 53
    bishop_file_rank_schlagen_file_rank = 54
    bishop_file_rank_schlagen_file_rank_check = 55
    bishop_file_rank_schlagen_file_rank_check_mate = 56

    # Alle Turmzüge
    rook_file_rank = 57
    rook_file_rank_check = 58
    rook_file_rank_check_mate = 59
    rook_file_file_rank = 60
    rook_rank_file_rank = 61
    rook_schlagen_file_rank = 62
    rook_schlagen_file_rank_check = 63
    rook_schlagen_file_rank_check_mate = 64
    rook_file_file_rank_check = 65
    rook_file_file_rank_check_mate = 66
    rook_rank_file_rank_check = 67
    rook_rank_file_rank_check_mate = 68
    rook_file_rank_file_rank = 69
    rook_file_schlagen_file_rank_check = 70
    rook_file_schlagen_file_rank_check_mate = 71
    rook_rank_schlagen_file_rank_check = 72
    rook_rank_schlagen_file_rank_check_mate = 73
    rook_file_rank_file_rank_check = 74
    rook_file_rank_file_rank_check_mate = 75
    rook_file_rank_schlagen_file_rank = 76
    rook_file_rank_schlagen_file_rank_check = 77
    rook_file_rank_schlagen_file_rank_check_mate = 78

    # Alle Damenzüge
    queen_file_rank = 79
    queen_file_rank_check = 80
    queen_file_rank_check_mate = 81
    queen_file_file_rank = 82
    queen_rank_file_rank = 83
    queen_schlagen_file_rank = 84
    queen_schlagen_file_rank_check = 85
    queen_schlagen_file_rank_check_mate = 86
    queen_file_file_rank_check = 87
    queen_file_file_rank_check_mate = 88
    queen_rank_file_rank_check = 89
    queen_rank_file_rank_check_mate = 90
    queen_file_rank_file_rank = 91
    queen_file_schlagen_file_rank_check = 92
    queen_file_schlagen_file_rank_check_mate = 93
    queen_rank_schlagen_file_rank_check = 94
    queen_rank_schlagen_file_rank_check_mate = 95
    queen_file_rank_file_rank_check = 96
    queen_file_rank_file_rank_check_mate = 97
    queen_file_rank_schlagen_file_rank = 98
    queen_file_rank_schlagen_file_rank_check = 99
    queen_file_rank_schlagen_file_rank_check_mate = 100

    # Alle Königzüge
    # Ka2
    king_file_rank = 101
    king_file_rank_check = 102
    king_file_rank_check_mate = 103
    king_schlagen_file_rank = 104
    king_schlagen_file_rank_check = 105
    king_schlagen_file_rank_check_mate = 106

    # Alle Rochezüge
    roche = 107
    roche_check = 108
    roche_check_mate = 109
    roche_long = 110
    roche_long_check = 111
    roche_long_check_mate = 112