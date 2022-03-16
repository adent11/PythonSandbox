import pygame
import math

WIDTH, HEIGHT = 600, 400

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

mandlebrotSurface = pygame.Surface((WIDTH, HEIGHT))
mouseSurface = pygame.Surface((WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Mandlebrot Set Drawer")
WIN.fill((255, 255, 255))
empty = pygame.Color(0, 0, 0, 0)
rS, rE = -2, 1
iS, iE = -1, 1
maxIter = 500


def checkExit():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def mandelbrot(p):
    z = 0
    n = 0
    while abs(z) <= 2 and n < maxIter:
        z = z**2 + p
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
    imag = iS + (y / HEIGHT) * (iE - iS)
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
        print(x)
        for y in range(HEIGHT):
            point = complex(rS + (x / WIDTH) * (rE - rS),
                            iS + (y / HEIGHT) * (iE - iS))
            # print(point)
            mP = int(mandelbrot(point))
            color = (50 + mP * 205 / maxIter, 50 + mP *
                     205 / maxIter, 255)
            if color == (255, 255, 255):
                color = (0, 0, 0)
            mandlebrotSurface.set_at((x, y), color)
            checkExit()
    WIN.blit(mandlebrotSurface, (0, 0))
    pygame.display.update()


drawMandelbrot()
nextFrameTime = pygame.time.get_ticks() + 10
while True:
    checkExit()
    mX, mY = pygame.mouse.get_pos()
    print(f"Mouse X: {mX}  Mouse Y: {mY}")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            rS, rE, iS, iE = zoomedBounds(mX, mY, .1)
            drawMandelbrot()

    '''
    if pygame.time.get_ticks() > nextFrameTime:
        nextFrameTime = nextFrameTime + 10
        WIN.blit(mandlebrotSurface, (0, 0))
        if mX < WIDTH and mY < HEIGHT:
            point = complex(rS + (mX / WIDTH) * (rE - rS),
                            iS + (mY / HEIGHT) * (iE - iS))
            n = 1
            while n < 16:
                pygame.draw.line(WIN, (112, 169, 255), cplxToPos(
                    nIters(point, n)), cplxToPos(nIters(point, n + 1)), width=2)
                n = n + 1
        pygame.display.update()'''
