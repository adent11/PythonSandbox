import pygame
import math

WIDTH, HEIGHT = 1080, 720

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

mandlebrotSurface = pygame.Surface((WIDTH, HEIGHT))
mouseSurface = pygame.Surface((WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Mandlebrot Set Drawer")
WIN.fill((255, 255, 255))
empty = pygame.Color(0, 0, 0, 0)
RS, RE = -2, 1
IS, IE = -1, 1
maxIter = 100


def checkExit():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def mandlebrot(p):
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
    x = WIDTH * (p.real - RS) / (RE - RS)
    y = HEIGHT * (p.imag - IS) / (IE - IS)
    return (x, y)


for x in range(WIDTH):
    for y in range(HEIGHT):
        point = complex(RS + (x / WIDTH) * (RE - RS),
                        IS + (y / HEIGHT) * (IE - IS))
        # print(point)
        color = 255 - int(mandlebrot(point) * 255 / maxIter)
        mandlebrotSurface.set_at((x, y), (color, color, color))
        checkExit()
    WIN.blit(mandlebrotSurface, (0, 0))
    pygame.display.update()

nextFrameTime = pygame.time.get_ticks() + 10
while True:
    checkExit()
    mX, mY = pygame.mouse.get_pos()
    print(f"Mouse X: {mX}  Mouse Y: {mY}")
    '''
    if pygame.time.get_ticks() > nextFrameTime:
        nextFrameTime = nextFrameTime + 10
        WIN.blit(mandlebrotSurface, (0, 0))
        if mX < WIDTH and mY < HEIGHT:
            point = complex(RS + (mX / WIDTH) * (RE - RS),
                            IS + (mY / HEIGHT) * (IE - IS))
            n = 1
            while n < 16:
                pygame.draw.line(WIN, (112, 169, 255), cplxToPos(
                    nIters(point, n)), cplxToPos(nIters(point, n + 1)), width=2)
                n = n + 1
        pygame.display.update()'''
