from traceback import print_tb
import pygame
import math

WIDTH, HEIGHT = 1920, 1920

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

mandlebrotSurface = pygame.Surface((WIDTH, HEIGHT))
mouseSurface = pygame.Surface((WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Mandlebrot Set Drawer")
WIN.fill((255, 255, 255))
empty = pygame.Color(0, 0, 0, 0)
rS, rE = -1.5, 1.5
iS, iE = -1.5, 1.5
maxIter = 100
power = 1.5


def checkExit():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def printStatus():
    mX, mY = pygame.mouse.get_pos()
    mPosCplx = posToCplx(mX, mY)
    print(
        f"maxIters: {maxIter}  rS: {rS}  rE: {rE}  iS: {iS}  iE{iE}  mousePos: {mPosCplx}")


def mandelbrot(p):
    z = 0
    n = 0
    q = (p.real - 1/4) ** 2 + p.imag ** 2
    """if q * (q + (p.real - 1/4)) <= p.imag ** 2 / 4:  # Checks if point is in the center cartioid
        return maxIter"""
    while abs(z) <= 2 and n < maxIter:
        z = z**power + p
        n += 1
    return n


def nIters(p, n):
    z = 0
    for i in range(n):
        z = z**2 + p
    return z


def cplxToPos(p):
    x = WIDTH * (p.real - rS) / (rE - rS)
    y = HEIGHT * (p.imag - iS) / (iE - iS)
    return (x, y)


def posToCplx(x, y):
    real = rS + (x / WIDTH) * (rE - rS)
    imag = iS + ((HEIGHT - y) / HEIGHT) * (iE - iS)
    return complex(real, imag)


def zoomedBounds(cX, cY, zoom):
    cplxC = posToCplx(cX, cY)
    nRS = cplxC.real - (cplxC.real - rS) * zoom
    nRE = cplxC.real + (rE - cplxC.real) * zoom
    nIS = cplxC.imag - (cplxC.imag - iS) * zoom
    nIE = cplxC.imag + (iE - cplxC.imag) * zoom
    return nRS, nRE, nIS, nIE


def drawMandelbrot():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            point = complex(rS + (x / WIDTH) * (rE - rS),
                            iS + ((HEIGHT - y) / HEIGHT) * (iE - iS))
            # print(point)
            mP = int(mandelbrot(point))
            color = (255 - mP * 255 / maxIter, 255 - mP *
                     255 / maxIter, 255 - mP *
                     255 / maxIter)
            if color == (255, 255, 255):
                color = (0, 0, 0)
            mandlebrotSurface.set_at((x, y), color)
            checkExit()
    WIN.blit(mandlebrotSurface, (0, 0))
    pygame.display.update()


def drawPointPath():
    WIN.blit(mandlebrotSurface, (0, 0))
    if mX < WIDTH and mY < HEIGHT:
        point = complex(rS + (mX / WIDTH) * (rE - rS),
                        iS + (mY / HEIGHT) * (iE - iS))
        n = 1
        while n < 11:
            pygame.draw.line(WIN, (112, 169, 255), cplxToPos(
                nIters(point, n)), cplxToPos(nIters(point, n + 1)), width=1)
            n = n + 1
    pygame.display.update()


nextFrameTime = pygame.time.get_ticks() + 10
for intpwer in range(2544, 3001, 1):
    power = intpwer/1000
    print(power)
    drawMandelbrot()
    pygame.image.save(
        WIN, f"Ndelbrot/{power}.jpg")
# checkExit()
#mX, mY = pygame.mouse.get_pos()
#print(f"Mouse X: {mX}  Mouse Y: {mY}")
"""printStatus()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            rS, rE, iS, iE = zoomedBounds(mX, mY, .99)
            maxIter = maxIter * 1.05
            drawMandelbrot()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                maxIter = int(input("Enter new max iterations: "))
                drawMandelbrot()"""
'''if pygame.time.get_ticks() > nextFrameTime:
        nextFrameTime = nextFrameTime + 10
        drawPointPath()'''


# Interesting point: -.0789908670791665+0.14658918139999
