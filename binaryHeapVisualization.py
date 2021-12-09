from customDataTypes import MinHeap
import random, pygame

WIDTH, HEIGHT = 1200, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Heap Visualization")
clock = pygame.time.Clock()  # Starts a clock
pygame.font.init() # Initializes pygame font module
MYFONT = pygame.font.SysFont('Microsoftsansserif', 30) # Creates font object
DRAW_DELAY = 400

class VisualizedMinHeap(MinHeap):
    def upheap(self, gen, idx):
        parGen = gen - 1
        parIdx = idx//2
        if gen != 0 and self.heap[gen][idx][1] < self.heap[parGen][parIdx][1]:
            self.swap(gen, idx, parGen, parIdx)
            self.draw()
            self.upheap(parGen, parIdx)

    def downheap(self, gen, idx):
        cGen = gen + 1
        c1Idx = idx * 2
        c2Idx = idx * 2 + 1
        hasChild = self.exists(cGen, c1Idx) or self.exists(cGen, c2Idx)
        if not self.exists(cGen, c2Idx):
            minCIdx = c1Idx
        elif self.heap[cGen][c1Idx][1] < self.heap[cGen][c2Idx][1]:
            minCIdx = c1Idx
        else:
            minCIdx = c2Idx
        
        if hasChild:
            if self.heap[cGen][minCIdx][1] < self.heap[gen][idx][1]:
                self.swap(gen, idx, cGen, minCIdx)
                self.draw()
                self.downheap(cGen, minCIdx)

    def insert(self, data, priority):
        if self.isEmpty(): # Inserts at root if heap is empty
            self.heap = [[(data, priority)]]
        elif len(self.heap) > 1 and len(self.heap[len(self.heap)-1]) < 2*len(self.heap[len(self.heap)-2]): # Inserts in the last generation if it is empty
            self.heap[len(self.heap)-1].append((data, priority))
        else: # Creates a new generation if the last is full
            self.heap.append([(data, priority)])
        self.draw()
        self.upheap(len(self.heap)-1, len(self.heap[len(self.heap)-1])-1) 

    def popMin(self):
        if self.isEmpty():
            return None
        if len(self.heap) == 1:
            return self.heap[0].pop()[0]
        poppedData = self.heap[0][0][0] # The first value (data) of the first node in the first generation (the root)
        replacement = self.heap[len(self.heap)-1].pop() # Removes last node in the last generation
        self.heap[0][0] = replacement # Replaces the root with the node removed from the end
        if len(self.heap[len(self.heap)-1]) == 0:
            self.heap.pop() # If the last generation is empty, it gets deleted
        self.draw()
        self.downheap(0, 0) # Ensures that the heap remains properly ordered by moving the new root to its correct place
        return poppedData
        
    def draw(self):
        pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(0, 0, WIDTH, HEIGHT-IN_BOX_H))
        GEN_GAP = 10
        for genIdx, genNodes in enumerate(self.heap):
            genLen = 2**genIdx
            for nodeIdx, node in enumerate(genNodes):
                nodeTxt = MYFONT.render(str(node[1]), 1, (0, 0, 0))
                nodeX = (2 * nodeIdx + 1) * WIDTH / (genLen*2)
                nodeY = genIdx * (nodeTxt.get_height() + GEN_GAP) + GEN_GAP
                WIN.blit(nodeTxt, (nodeX - nodeTxt.get_width() / 2, nodeY))
                if genIdx != 0:
                    parentX =(2 * (nodeIdx//2) + 1) * WIDTH / ((genLen/2) * 2)
                    parentY = (genIdx-1) * (nodeTxt.get_height() + GEN_GAP) + GEN_GAP + nodeTxt.get_height()
                    pygame.draw.line(WIN, (200, 200, 200), (nodeX, nodeY), (parentX, parentY), width = 2)
        pygame.display.update()
        waitFor(pygame.time.get_ticks() + DRAW_DELAY)

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

IN_BOX_W = 175
IN_BOX_H = 50
TEXT_X = 10
TEXT_Y = HEIGHT - IN_BOX_H + 10
def drawInputBox():
    pygame.draw.rect(WIN, (255, 255, 255), pygame.Rect(0, HEIGHT-IN_BOX_H, IN_BOX_W, IN_BOX_H))
    inpTxt = MYFONT.render(f"Input: {inputField}", 1, (0, 0, 0))
    WIN.blit(inpTxt, (TEXT_X, TEXT_Y))
    pygame.display.update()

tHQ = VisualizedMinHeap()
inputField = ''
MAX_IN_LEN = 2
WIN.fill((255, 255, 255))
pygame.display.update()
drawInputBox()
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
                tHQ.draw()
            if event.key == pygame.K_p:
                tHQ.popMin()
                tHQ.draw()
            if event.key == pygame.K_0 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '0'
                drawInputBox()
            if event.key == pygame.K_1 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '1'
                drawInputBox()
            if event.key == pygame.K_2 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '2'
                drawInputBox()
            if event.key == pygame.K_3 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '3'
                drawInputBox()
            if event.key == pygame.K_4 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '4'
                drawInputBox()
            if event.key == pygame.K_5 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '5'
                drawInputBox()
            if event.key == pygame.K_6 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '6'
                drawInputBox()
            if event.key == pygame.K_7 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '7'
                drawInputBox()
            if event.key == pygame.K_8 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '8'
                drawInputBox()
            if event.key == pygame.K_9 and len(inputField) < MAX_IN_LEN:
                inputField = inputField + '9'
                drawInputBox()
            if event.key ==  pygame.K_RETURN and len(tHQ.heap[-1]) < 32 and inputField != '':
                tHQ.insert('', int(inputField))
                inputField = ''
                drawInputBox()
            if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                if inputField != '':
                    inputField = inputField[:-1]
                    drawInputBox()
            if event.key == pygame.K_u:
                tHQ.draw()
                drawInputBox()
