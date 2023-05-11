from board import Board
from game import Game

prob = 0.1
size = (9,9)
board = Board(size, prob)
screenSize = (800,800)

game = Game(board, screenSize)

game.run()