from enum import Enum

class e_move_info_type(Enum):
    notdef = 0
    enough = 1
    file_fehlt = 2
    rank_fehlt = 3
    file_rank_fehlt = 4
    promote_fehlt = 5
    schlagen_fehlt = 6
    too_many_pieces = 7