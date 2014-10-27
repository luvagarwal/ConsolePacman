"""
Test File for COnsole Pacman
"""

import unittest
from nose.tools import assert_equals
import random
from Pacman import *

class TestPacman(unittest.TestCase):
    """
    Test class for Console Pacman
    """
    def setUp(self):
        self.player = Pacman(-1, -1)
        self.ghosts = Ghosts(self.player)
        self.board = Board(self.ghosts, self.player)

    def test_reset(self):
        """
        Test the reset function
        """
        assert len(self.board.coins) != 0
        self.player.score = 10
        self.board.reset()
        assert len(self.board.coins) != 0
        assert self.player.score == 0

    def test_score_change(self):
        assert self.player.score == 0
        self.player.x = self.board.coins[0][0] - 1
        self.player.y = self.board.coins[0][1]
        MovePacman(self.player, self.board).coin_taken(1, 0)
        assert self.player.score == 1

    def test_pacman_move_right(self):
        self.player.x = 3
        self.player.y = 4
        self.board.board[self.player.y][self.player.x+1] = 'X'
        MovePacman(self.player, self.board).move_right()
        assert self.player.x == 3
        assert self.player.y == 4
        self.board.board[self.player.y][self.player.x+1] = '.'
        MovePacman(self.player, self.board).move_right()
        assert self.player.x != 3
        assert self.player.y == 4

    def test_pacman_move_left(self):
        self.player.x = 3
        self.player.y = 4
        self.board.board[self.player.y][self.player.x-1] = 'X'
        MovePacman(self.player, self.board).move_left()
        assert self.player.x == 3
        assert self.player.y == 4
        self.board.board[self.player.y][self.player.x-1] = '.'
        MovePacman(self.player, self.board).move_left()
        assert self.player.x != 3
        assert self.player.y == 4


    def test_pacman_move_up(self):
        self.player.x = 3
        self.player.y = 4
        self.board.board[self.player.y-1][self.player.x] = 'X'
        MovePacman(self.player, self.board).move_up()
        assert self.player.x == 3
        assert self.player.y == 4
        self.board.board[self.player.y-1][self.player.x] = '.'
        MovePacman(self.player, self.board).move_up()
        assert self.player.x == 3
        assert self.player.y != 4

    def test_pacman_move_down(self):
        self.player.x = 3
        self.player.y = 4
        self.board.board[self.player.y+1][self.player.x] = 'X'
        MovePacman(self.player, self.board).move_down()
        assert self.player.x == 3
        assert self.player.y == 4
        self.board.board[self.player.y+1][self.player.x] = '.'
        MovePacman(self.player, self.board).move_down()
        assert self.player.x == 3
        assert self.player.y != 4


    def test_pacman_die(self):
        self.ghosts.ghosts[0].x = 2
        self.ghosts.ghosts[0].y = 3
        self.board.board[2][2] = '.'
        self.player.x = 4
        self.player.y = 3
        MovePacman(self.player, self.board).move_left()
        print self.player.x
        self.ghosts.move_ghost()
        assert self.player.die == 1
