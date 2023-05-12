import sys

import pygame

import settings
from board import Board
from button import Button
from game import Game


class MainMenu:
    def __init__(self) -> None:
        pygame.init()

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("fonts/font.ttf", size)

    def loadMainMenu(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Minesweeper Menu")
        background = pygame.image.load("images/background.png")
        while True:
            self.screen.blit(background, (0,0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(35).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
            PLAY_BUTTON = Button(image=None, pos=(640, 200), text_input="PLAY", font=self.get_font(40), base_color="#d7fcd4", hovering_color="#d7fcd4")
            EASY_BUTTON = Button(image=None, pos=(213, 350), text_input="EASY", font=self.get_font(30), base_color="#d7fcd4", hovering_color="White")
            MEDIUM_BUTTON = Button(image=None, pos=(639, 350), text_input="MEDIUM", font=self.get_font(30), base_color="#d7fcd4", hovering_color="White")
            HARD_BUTTON = Button(image=None, pos=(1065, 350), text_input="HARD", font=self.get_font(30), base_color="#d7fcd4", hovering_color="White")
            HIGHSCORE_BUTTON = Button(image=None, pos=(640, 500), text_input="HIGHSCORE", font=self.get_font(30), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=None, pos=(640, 600), text_input="QUIT", font=self.get_font(30), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)
            for button in [PLAY_BUTTON,EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, HIGHSCORE_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        prob = settings.EASY_PROBABILITY
                        size = settings.EASY_SIZE
                        board = Board(size, prob)
                        screenSize = settings.EASY_SCREEN_SIZE
                        game = Game(board, screenSize)
                        game.run()
                    if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                        prob = settings.MEDIUM_PROBABILITY
                        size = settings.MEDIUM_SIZE
                        board = Board(size, prob)
                        screenSize = settings.MEDIUM_SCREEN_SIZE
                        game = Game(board, screenSize)
                        game.run()
                    if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                        prob = settings.HARD_PROBABILITY
                        size = settings.HARD_SIZE
                        board = Board(size, prob)
                        screenSize = settings.HARD_SCREEN_SIZE
                        game = Game(board, screenSize)
                        game.run()
                    if HIGHSCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pass
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()