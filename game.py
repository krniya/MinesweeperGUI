import os
import sys
from time import sleep

import pygame

from button import Button


class Game():
    def __init__(self, board, screenSize) -> None:
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()


    def run(self):
        pygame.init()
        self.mainMenu()
        
    def runGame(self):
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if self.board.getWon():
                sound = pygame.mixer.Sound("./sounds/win.wav")
                sound.play()
                sleep(3)
                running = False
            if self.board.getLost():
                sound = pygame.mixer.Sound("./sounds/lost.wav")
                sound.play()
                sleep(3)
                running = False
        pygame.quit()

    def mainMenu(self):
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
                        self.runGame()
                    if HIGHSCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pass
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("fonts/font.ttf", size)

    def draw(self):
        topLeft = (0,0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if not fileName.endswith(".png"):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image


    def getImage(self, piece):
        string = None
        if(piece.getClicked()):
            string  = "bomb-at-clicked-block" if piece.getHasBomb() else str(piece.getNumArround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block"
        return self.images[string]
    
    def handleClick(self, position, rightClick):
        if self.board.getLost():
            return
        
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleCLick(piece, rightClick)
