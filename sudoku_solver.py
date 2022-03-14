board = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

isGiven = [[board[y][x] != 0 for x in range(9)] for y in range(9)]

curRow, curCol = 0, 0

def isSafe(row, col, num): # Checks if a number can be put in a place
    for i in range(9):
        if num == board[row, i]: # Checks if number in row
            return False

    for i in range(9): # Checks if number in column
        if num == board[i, col]:
            return False

    startRow = row - row % 3 # Finds first row of box number is in
    starCol = col - col % 3 # Finds first column of box number is in
    for i in range(3):
        for j in range(3):
            if board[startRow + i, starCol + j] == num: # Checks if number in box
                return False
    return True # Returns true if number can be put in that position

def previous(row, col):
    prevRow = row
    prevCol = col
    foundPrevious = False
    while not foundPrevious:
        prevCol = prevCol - 1
        if prevCol < 0:
            prevCol = 8
            prevRow = prevRow - 1
        foundPrevious = not isGiven[prevRow][prevCol]
    return prevRow, prevCol

def next(row, col):
    nextRow = row
    nextCol = col
    foundNext = False
    while not foundNext:
        nextCol = nextCol + 1
        if nextCol > 8:
            nextCol = 0
            nextRow = nextRow + 1
        foundNext = not isGiven[nextRow][nextCol]
    return nextRow, nextCol

while curRow < 9:
    if not isGiven[curRow][curCol]:
