class lifeGrid:
    def __init__(self):
        self.curGenCells = {}
        self.nextGenCells = {}
        self.cellNeighborCount = {}
        self.neighborDeltas = [(dX, dY) for dX in range(-1, 2) for dY in range(-1, 2) if dX != 0 or dY != 0]

    def addCell(self, cellX, cellY):
        self.curGenCells[(cellX, cellY)] = True
    
    def isAlive(self, x, y):
        return (x, y) in self.curGenCells
    
    def kill(self, x, y):
        del self.curGenCells[(x, y)]
    
    def clear(self):
        self.curGenCells = {}
    
    def generate(self):
        self.cellNeighborCount = {}
        self.nextGenCells = {}
        for cell in self.curGenCells:
            for neighborDelta in self.neighborDeltas:
                neighbor = (cell[0] + neighborDelta[0], cell[1] + neighborDelta[1])
                if neighbor in self.cellNeighborCount:
                    self.cellNeighborCount[neighbor] = self.cellNeighborCount[neighbor] + 1
                else:
                    self.cellNeighborCount[neighbor] = 1
        for cell in self.cellNeighborCount:
            if self.cellNeighborCount[cell] == 3:
                self.nextGenCells[cell] = True
            elif self.cellNeighborCount[cell] == 2 and cell in self.curGenCells:
                self.nextGenCells[cell] = True
        self.curGenCells = self.nextGenCells