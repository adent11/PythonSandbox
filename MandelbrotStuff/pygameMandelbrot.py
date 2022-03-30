from traceback import print_tb
import multiprocessing as mp
import time
import pygame
import math

WIDTH, HEIGHT = 900, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

mandlebrotSurface = pygame.Surface((WIDTH, HEIGHT))
mouseSurface = pygame.Surface((WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Mandlebrot Set Drawer")
WIN.fill((255, 255, 255))
empty = pygame.Color(0, 0, 0, 0)
rS, rE = -2, 1
iS, iE = -1, 1
maxIter = 100
power = 2

def hslToRGB(h, s, l):
    c = (1 - abs(2*l-1)) * s
    x = c * (1 - abs((h/60) % 2 -1))
    m = l - c/2
    if 0 <= h and h < 60:
        rp, gp, bp = (c, x, 0)
    elif 60 <= h and h < 120:
        rp, gp ,bp = (x, c, 0)
    elif 120 <= h and h < 180:
        rp, gp ,bp = (0, c, x)
    elif 180 <= h and h < 240:
        rp, gp ,bp = (0, x, c)
    elif 240 <= h and h < 300:
        rp, gp ,bp = (x, 0, c)
    elif 300 <= h and h < 360:
        rp, gp ,bp = (c, 0, x)
    (r, g, b) = ((rp + m) * 255, (gp + m) * 255, (bp + m) * 255)
    return (int(r), int(g), int(b))

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

def renderPixel(x, y):
    point = complex(rS + (x / WIDTH) * (rE - rS),
                    iS + ((HEIGHT - y) / HEIGHT) * (iE - iS))
    z = 0
    n = 0
    """q = (p.real - 1/4) ** 2 + p.imag ** 2"""
    """if q * (q + (p.real - 1/4)) <= p.imag ** 2 / 4:  # Checks if point is in the center cartioid
        return maxIter"""
    while abs(z) <= 2 and n < maxIter:
        z = z**power + point
        n += 1
    """n = int(n)
    color = (255 - n * 255 / maxIter, 255 - n * 255 / maxIter, 255 - n * 255 / maxIter)
    if color == (255, 255, 255):
        color = (0, 0, 0)"""
    color = hslToRGB((n/maxIter) * 359, 1, .5)
    mandlebrotSurface.set_at((x, y), color)
    checkExit()


def drawMandelbrot():
    startTime = time.time()
    for x in range(WIDTH):
        """pool = mp.Pool()
        pool.map(renderPixel, [x, range(HEIGHT)])"""
        for y in range(HEIGHT):
            point = complex(rS + (x / WIDTH) * (rE - rS),
                            iS + ((HEIGHT - y) / HEIGHT) * (iE - iS))
            # print(point)
            mP = int(mandelbrot(point))
            """color = (255 - mP * 255 / maxIter, 255 - mP *
                     255 / maxIter, 255 - mP *
                     255 / maxIter)
            if color == (255, 255, 255):
                color = (0, 0, 0)"""
            color = hslToRGB((mP/maxIter) * 240, 1, .5)
            mandlebrotSurface.set_at((x, y), color)
            mandlebrotSurface.set_at((x, y), color)
            checkExit()
        WIN.blit(mandlebrotSurface, (0, 0))
        pygame.display.update()
    print(f"Rendering took {time.time() - startTime} seconds")


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



"""for intpwer in range(2976, 3001, 1):
    power = intpwer/1000
    print(power)
    
    pygame.image.save(
        WIN, f"Ndelbrot/{power}.jpg")
# checkExit()
mX, mY = pygame.mouse.get_pos()
#print(f"Mouse X: {mX}  Mouse Y: {mY}")"""
drawMandelbrot()
nextFrameTime = pygame.time.get_ticks() + 10
while True:
    checkExit()
    mX, mY = pygame.mouse.get_pos()
    printStatus()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            rS, rE, iS, iE = zoomedBounds(mX, mY, .1)
            #maxIter = maxIter * 1.05
            drawMandelbrot()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                maxIter = int(input("Enter new max iterations: "))
                drawMandelbrot()
    """if pygame.time.get_ticks() > nextFrameTime:
        nextFrameTime = nextFrameTime + 10
        drawPointPath()"""


# Interesting point: -.0789908670791665+0.14658918139999
