import random
import os

class ListNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        return
    
    def hasParent(self):
        return self.parent != None

    def hasValue(self, value):
        if self.data == value:
            return True
        else:
            return False
    
    def findGrandparent(self):
        if self.hasParent():
            if self.parent.hasParent():
                self.grandparent = self.parent.parent
                return self.grandparent
    
    def findRoot(self):
        curNode = self
        while curNode.hasParent():
            curNode = curNode.parent
        return curNode
""""
n1 = ListNode(1)
n2 = ListNode(2, n1)
n3 = ListNode(3, n2)
print(type(n1))
print(n3.findRoot() == n1)
"""

class ListPriorityQueue():
    def __init__(self):
        self.items = []

    def insert(self, value, priority):
        self.items.append((value, priority))
    
    def popHighest(self):
        maxPriority = max([self.items[i][1] for i in range(len(self.items))])
        for i in range(len(self.items)):
            if self.items[i][1] == maxPriority:
                return self.items.pop(i)[0]
    
    def popLowest(self):
        minPriority = min([self.items[i][1] for i in range(len(self.items))])
        for i in range(len(self.items)):
            if self.items[i][1] == minPriority:
                return self.items.pop(i)[0]
    
    def print(self):
        for i in range(len(self.items)):
            print(self.items[i])

# https://www.cs.purdue.edu/homes/bharsha/downloads/cs50010lec9pt1.pdf

class MinHeap():
    def __init__(self):
        self.heap = [[]]

    def isEmpty(self):
        return self.heap == [[]]

    def exists(self, gen, idx):
        if len(self.heap)-1 < gen:
            return False
        elif len(self.heap[gen])-1 < idx:
            return False
        else:
            return True

    def swap(self, gen1, idx1, gen2, idx2):
        val1 = self.heap[gen1][idx1]
        val2 = self.heap[gen2][idx2]
        self.heap[gen1][idx1] = val2
        self.heap[gen2][idx2] = val1

    def upheap(self, gen, idx):
        parGen = gen - 1
        parIdx = idx//2
        #self.print()
        if gen != 0 and self.heap[gen][idx][1] < self.heap[parGen][parIdx][1]:
            self.swap(gen, idx, parGen, parIdx)
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
                #print(f"Parent: {self.heap[gen][idx][1]} swapped with Child: {self.heap[cGen][minCIdx][1]}")
                self.swap(gen, idx, cGen, minCIdx)
                self.downheap(cGen, minCIdx)
        #self.print()
        

    def insert(self, data, priority):
        if self.isEmpty(): # Inserts at root if heap is empty
            self.heap = [[(data, priority)]]
        elif len(self.heap) > 1 and len(self.heap[len(self.heap)-1]) < 2*len(self.heap[len(self.heap)-2]): # Inserts in the last generation if it is empty
            self.heap[len(self.heap)-1].append((data, priority))
        else: # Creates a new generation if the last is full
            self.heap.append([(data, priority)])
        self.upheap(len(self.heap)-1, len(self.heap[len(self.heap)-1])-1) 
    
    def dequeue(self):
        if self.isEmpty():
            return None
        if len(self.heap) == 1:
            return self.heap[0].pop()[0]
        poppedData = self.heap[0][0][0] # The first value (data) of the first node in the first generation (the root)
        replacement = self.heap[len(self.heap)-1].pop() # Removes last node in the last generation
        self.heap[0][0] = replacement # Replaces the root with the node removed from the end
        if len(self.heap[len(self.heap)-1]) == 0:
            self.heap.pop() # If the last generation is empty, it gets deleted
        self.downheap(0, 0) # Ensures that the heap remains properly ordered by moving the new root to its correct place
        return poppedData

    def print(self):
        for gen, pop in enumerate(self.heap):
            tempPop = pop[:]
            while len(tempPop) < 2**gen:
                tempPop.append(('     '))
            print(str(tempPop).center(os.get_terminal_size().columns))
        print()