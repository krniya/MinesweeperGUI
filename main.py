import settings
from board import Board
from game import Game


def main():
    prob = settings.PROBABILITY
    size = settings.SIZE
    board = Board(size, prob)
    screenSize = settings.SCREEN_SIZE
    game = Game(board, screenSize)
    game.run()


if __name__ == '__main__':
    main()