import pygame
from GOLClass import lifeGrid

WIDTH, HEIGHT = 900, 400
squareSize = 10
firstSquarePos = (-1, -1)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()  # Starts a clock
grid = lifeGrid()
frameLength = 200
playing = False

def waitFor(t):
    while pygame.time.get_ticks() < t:
        keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
        if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
            pygame.quit()
            exit()
        for event in pygame.event.get():  # Quits if window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def drawGrid(updateScreen = False):
    curX, curY = (firstSquarePos[0]%squareSize, firstSquarePos[1]%squareSize)
    while curX < WIDTH:
        pygame.draw.line(WIN, (100, 100, 100), (curX, 0), (curX, HEIGHT), width = 1)
        curX = curX + squareSize
    while curY < HEIGHT:
        pygame.draw.line(WIN, (100, 100, 100), (0, curY), (WIDTH, curY), width = 1)
        curY = curY + squareSize
    pygame.draw.rect(WIN,(255, 0, 0),(firstSquarePos[0]+1,firstSquarePos[1]+1,squareSize-1, squareSize-1))

CELL_COLOR = (0, 0, 0)
def drawLiveCells():
    xOffset = firstSquarePos[0] % squareSize
    yOffset = firstSquarePos[1] % squareSize
    firstCellX = firstSquarePos[0] // squareSize * -1
    firstCellY = firstSquarePos[1] // squareSize * -1
    curCellY = firstCellY
    row = 0
    while row*squareSize < HEIGHT:
        col = 0
        curCellX = firstCellX
        while col*squareSize < WIDTH:
            if grid.isAlive(curCellX, curCellY):
                pygame.draw.rect(WIN,CELL_COLOR,(col*squareSize + xOffset, row*squareSize + yOffset,squareSize, squareSize))
            col = col + 1
            curCellX = curCellX + 1
        row = row + 1
        curCellY = curCellY + 1


def resizeSquare(newSize):
    global squareSize, firstSquarePos
    mouseX, mouseY = pygame.mouse.get_pos()
    sizeRatio = newSize/squareSize
    toMouseX, toMouseY = mouseX - firstSquarePos[0], mouseY - firstSquarePos[1]
    firstSquarePos = (mouseX - toMouseX*sizeRatio, mouseY - toMouseY*sizeRatio)
    squareSize = newSize


nextFrameTime = pygame.time.get_ticks() + frameLength
while True:
    WIN.fill((255,255,255))
    drawLiveCells()
    drawGrid()
    pygame.display.update()
    if playing and pygame.time.get_ticks() > nextFrameTime:
        grid.generate()
        nextFrameTime = nextFrameTime + frameLength
    for event in pygame.event.get():  # Quits if window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            lastMousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                if squareSize < 300000:
                    resizeSquare(squareSize + 1)
            elif event.y == -1:
                if squareSize > 5:
                    resizeSquare(squareSize - 1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                playing = not playing
                nextFrameTime = pygame.time.get_ticks()
            if event.key == pygame.K_0:
                firstSquarePos = (-1, -1)
            if event.key == pygame.K_g:
                grid.generate()
    keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
    if pygame.mouse.get_pressed()[1]:
        mousePos = pygame.mouse.get_pos()
        mousePosDif = tuple((mousePos[i]-lastMousePos[i] for i in range(2)))
        firstSquarePos = tuple(((firstSquarePos[i] + mousePosDif[i]) for i in range(2)))
        lastMousePos = mousePos
    if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
        pygame.quit()
        exit()
    if pygame.mouse.get_pressed()[0]:
        mousePos = pygame.mouse.get_pos()
        cell = ((-1*firstSquarePos[0] + mousePos[0])//squareSize, (-1*firstSquarePos[1] + mousePos[1])//squareSize)
        if not grid.isAlive(cell[0], cell[1]):
            grid.addCell(cell[0], cell[1])
    if keys_pressed[pygame.K_c]:
        grid.clear()
    if pygame.mouse.get_pressed()[2]:
        mousePos = pygame.mouse.get_pos()
        cell = ((-1*firstSquarePos[0] + mousePos[0])//squareSize, (-1*firstSquarePos[1] + mousePos[1])//squareSize)
        if grid.isAlive(cell[0], cell[1]):
            grid.kill(cell[0], cell[1])