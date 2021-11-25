from customDataTypes import MinHeap
import random, os, pygame

WIDTH, HEIGHT = 1200, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Heap Visualization")
clock = pygame.time.Clock()  # Starts a clock
pygame.font.init() # Initializes pygame font module
MYFONT = pygame.font.SysFont('Microsoftsansserif', 35) # Creates font object

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


GEN_GAP = 10
def drawHeap(heap):
    WIN.fill((255, 255, 255))
    for genIdx, genNodes in enumerate(heap):
        genLen = 2**genIdx
        for nodeIdx, node in enumerate(genNodes):
            nodeTxt = MYFONT.render(str(node[1]), 1, (0, 0, 0))
            nodeX = (2*nodeIdx+1)*WIDTH/(genLen*2)-nodeTxt.get_width()/2
            nodeY = genIdx*(nodeTxt.get_height() + GEN_GAP)+GEN_GAP
            WIN.blit(nodeTxt, (nodeX, nodeY))
    pygame.display.update()

tHQ = MinHeap()

while True:
    keys_pressed = pygame.key.get_pressed()  # Gets the keys pressed
    if keys_pressed[pygame.K_ESCAPE]:  # Quits if the escape key is pressed
        pygame.quit()
        exit()
    for event in pygame.event.get():  # Quits if window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                tHQ.insert('', random.randrange(100))
                drawHeap(tHQ.heap)
            if event.key == pygame.K_p:
                tHQ.dequeue()
                drawHeap(tHQ.heap)