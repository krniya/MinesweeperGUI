from board import Board
from game import Game

size = (9,9)
board = Board(size)
screenSize = (800,800)

game = Game(board, screenSize)

game.run()