#!/usr/bin/env python
"""
Console Pacman build with basic python
"""

from random import random

class Person(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Pacman(Person):
    def __init__(self, x, y):
        super(Pacman, self).__init__(x, y)
        self.score = 0
        self.die = 0


class Ghost(Person):
    def __init__(self, x, y):
        super(Ghost, self).__init__(x, y)


# Variables declaration

class Ghosts(object):
    """
    Class to store all the ghosts and some utility functions
    """
    def __init__(self, player):
        self.ghosts = []
        self.player = player

    def move_ghosts(self):
        """
        Move the ghosts in the direction of Pacman
        """
        temp_ghosts = []
        for ghost in self.ghosts:
            if (self.player.x - ghost.x > 0 and
               board.board[ghost.y][ghost.x+1 if ghost.x < 34 else ghost.x] == '.' or
               board.board[ghost.y][ghost.x+1 if ghost.x < 34 else ghost.x] == 'P'
               ):
                board.board[ghost.y][ghost.x] = '.'
                if board.board[ghost.y][ghost.x+1] == 'P':
                    print 'Lost the game'
                    self.player.die = 1
                    exit()
                board.board[ghost.y][ghost.x+1] = 'G'
                ghost.x += 1
            elif (self.player.x - ghost.x < 0 and
                 board.board[ghost.y][ghost.x-1 if ghost.x > 0 else ghost.x] == '.'
                 or board.board[ghost.y][ghost.x-1 if ghost.x > 0 else ghost.x] == 'P'
                 ):
                board.board[ghost.y][ghost.x] = '.'
                if board.board[ghost.y][ghost.x-1] == 'P':
                    print 'Lost the game'
                    self.player.die = 1
                    exit()
                board.board[ghost.y][ghost.x-1] = 'G'
                ghost.x -= 1
            elif (self.player.y - ghost.y > 0
                 and board.board[ghost.y+1 if ghost.y < 14 else ghost.y][ghost.x] == '.'
                 or board.board[ghost.y+1 if ghost.y < 14 else ghost.y][ghost.x] == 'P'
                 ):
                board.board[ghost.y][ghost.x] = '.'
                if board.board[ghost.y+1][ghost.x] == 'P':
                    print 'Lost the game'
                    self.player.die = 1
                    exit()
                board.board[ghost.y+1][ghost.x] = 'G'
                ghost.y += 1
            elif (board.board[ghost.y-1 if ghost.y > 0 else ghost.y][ghost.x] == '.'
                 or board.board[ghost.y-1 if ghost.y > 0 else ghost.y][ghost.x] == 'P'
                 ):
                board.board[ghost.y][ghost.x] = '.'
                if board.board[ghost.y-1][ghost.x] == 'P':
                    print 'Lost the game'
                    self.player.die = 1
                    exit()
                board.board[ghost.y-1][ghost.x] = 'G'
                ghost.y -= 1
            temp_ghosts.append(ghost)
        self.ghosts = temp_ghosts

    def move_ghost(self):
        self.player.die = 1

class Board(object):
    """
    A random 15 cross 35 board design having wall, Ghost, Coins and Pacman
    with no of coins = 25, ghosts = 5
    """
    def __init__(self, ghosts, player):
        self.board = [['.' for i in xrange(35)] for j in xrange(15)]
        self.ghosts = ghosts
        self.player = player
        self.coins = []
        self.initialize_board()

    def initialize_board(self):
        """
        Initialize the board
        """
        no_ghost = 0
        while no_ghost <= 5:
            tempx = (int(random()*100))%35
            tempy = (int(random()*100))%15
            if self.board[tempy][tempx] == '.':
                self.board[tempy][tempx] = 'G'
                self.ghosts.ghosts.append(Ghost(tempx, tempy))
                no_ghost += 1

        no_walls = 0
        while no_walls <= 30:
            tempx = (int(random()*100))%35
            tempy = (int(random()*100))%15
            if self.board[tempy][tempx] == '.':
                self.board[tempy][tempx] = 'X'
                no_walls += 1

        no_coins = 0
        while no_coins <= 25:
            tempx = (int(random()*100))%35
            tempy = (int(random()*100))%15
            if self.board[tempy][tempx] == '.':
                self.board[tempy][tempx] = 'C'
                self.coins.append([tempx, tempy])
                no_coins += 1

        no_pacman = 0
        while no_pacman == 0:
            tempx = (int(random()*100))%35
            tempy = (int(random()*100))%15
            if self.board[tempy][tempx] == '.':
                self.board[tempy][tempx] = 'P'
                self.player.x = tempx
                self.player.y = tempy
                no_pacman = 1

    def display_itself(self):
        """
        Display the board
        """
        for row in self.board:
            for col in row:
                print col,
            print '\n',
    
    def reset(self):
        """
        Restart the game
        """
        self.coins = []
        self.player.score = 0
        self.__init__(self.ghosts, self.player)



class TakeProcessInput(object):
    """
    Takes the input and change the game board by using other
    utility classes
    """
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def take_input(self):
        while True:
            self.board.display_itself()
            print 'Score: %s' % self.player.score
            dirn = raw_input('Enter Move: ')
            self.process_input(dirn)

    def process_input(self, dirn):
        pacman = MovePacman(self.player, self.board)
        if dirn == 'w':
            pacman.move_up()
        elif dirn == 'a':
            pacman.move_left()
        elif dirn == 's':
            pacman.move_down()
        elif dirn == 'd':
            pacman.move_right()
        else:
            print 'Invalid Key'
            pacman.dont_move_ghosts = 1
        if pacman.dont_move_ghosts == 0:
            ghosts.move_ghosts()


class MovePacman(object):
    """
    Utility class which has the functions to move the Pacman
    """
    def __init__(self, player, board):
        self.dont_move_ghosts = 0
        self.player = player
        self.board = board

    def coin_taken(self, x, y):
        """
        Increase the score when coin taken
        """
        if self.board.board[self.player.y+y][self.player.x+x] == 'C':
            self.player.score += 1

    def move_up(self):
        """
        Move the pacman up
        """
        kya = self.board.board[self.player.y-1][self.player.x]
        if self.player.y > 0 and kya != 'X' and kya != 'G':
            self.board.board[self.player.y][self.player.x] = '.'
            self.coin_taken(0, -1)
            self.board.board[self.player.y-1][self.player.x] = 'P'
            self.player.y -= 1
        else:
            print "Can't move up"
            self.dont_move_ghosts = 1

    def move_left(self):
        """
        Move the pacman left
        """
        kya = self.board.board[self.player.y][self.player.x-1]
        if self.player.x > 0 and kya != 'X' and kya != 'G':
            self.board.board[self.player.y][self.player.x] = '.'
            self.coin_taken(-1, 0)
            self.board.board[self.player.y][self.player.x-1] = 'P'
            self.player.x -= 1
        else:
            print "Can't move left"
            self.dont_move_ghosts = 1

    def move_down(self):
        """
        Move the pacman down
        """
        kya = self.board.board[self.player.y+1][self.player.x]
        if self.player.y < 14 and kya != 'X' and kya != 'G':
            self.board.board[self.player.y][self.player.x] = '.'
            self.coin_taken(0, 1)
            self.board.board[self.player.y+1][self.player.x] = 'P'
            self.player.y += 1
        else:
            print "Can't move down"
            self.dont_move_ghosts = 1

    def move_right(self):
        """
        Move right
        """
        kya = self.board.board[self.player.y][self.player.x+1]
        if self.player.x < 34 and kya != 'X' and kya != 'G':
            self.board.board[self.player.y][self.player.x] = '.'
            self.coin_taken(1, 0)
            self.board.board[self.player.y][self.player.x+1] = 'P'
            self.player.x += 1
        else:
            print "Can't move right"
            self.dont_move_ghosts = 1


if __name__ == '__main__':
    # Make Objects
    player = Pacman(-1, -1)
    ghosts = Ghosts(player)
    board = Board(ghosts, player)
    TakeProcessInput(board, player).take_input()
