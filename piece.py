class Piece:
    def __init__(self, hasBomb) -> None:
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False


    def getHasBomb(self):
        return self.hasBomb
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumArround()

    def setNumArround(self):
        self.numArround = 0
        for piece in self.neighbors:
            if (piece.getHasBomb()):
                self.numArround += 1
    
    def getNumArround(self):
        return self.numArround