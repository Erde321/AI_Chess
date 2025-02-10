from klassen.game.board.board import c_board
from klassen.game.move.move import c_move
from klassen.game.move.enums.move_player_enum import e_move_player

class c_game():

    def __init__(self):
        self._board = c_board
        self._move_player1 = c_move(e_move_player.player1)
        self._move_player2 = c_move(e_move_player.player2)