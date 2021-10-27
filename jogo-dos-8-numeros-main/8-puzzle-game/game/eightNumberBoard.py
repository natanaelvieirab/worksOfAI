import copy
from .board import Board
from random import choice

class EightNumberBoard:
    def __init__(self):
        self.size = 3
        self.board = Board(self.size)

        numbers = list(range(0,9))
        
        randomMatrix = []
        for i in range(self.size):
            randomMatrix.append([])
            for j in range(self.size):
                number = choice(numbers)
                numbers.remove(number)
                
                randomMatrix[i].append(number)

        self.board.matrix = randomMatrix

    def getBoard(self):
        return self.board.matrix

    def canMoveLeft(self, pos):
        return pos != [0,3] and pos != [1,0] and pos != [2,0]

    def canMoveRight(self, pos):
        return pos != [0,2] and pos != [1,2] and pos != [2,2]

    def canMoveBottom(self, pos):
        return pos !=[2,0] and pos !=[2,1] and pos != [2,2]

    def canMoveTop(self, pos):
        return pos != [0, 0] and pos != [0,1] and pos != [0,2]

    def top(self, node, i, j):
        upNode = copy.deepcopy(node)
        upNode[i][j] = upNode[i-1][j]
        upNode[i-1][j] = 0
        
        return upNode

    def right(self, node, i, j):
        rightNode = copy.deepcopy(node)
        rightNode[i][j] = rightNode[i][j+1]
        rightNode[i][j+1] = 0

        return rightNode

    def left(self, node, i, j):
        leftNode = copy.deepcopy(node)
        leftNode[i][j] = leftNode[i][j-1]
        leftNode[i][j-1] = 0

        return leftNode
    
    def bottom(self, node, i, j):
        downNode = copy.deepcopy(node)
        downNode[i][j] = downNode[i+1][j]
        downNode[i+1][j] = 0

        return downNode
    
    def __str__(self):
        return self.board.__str__()