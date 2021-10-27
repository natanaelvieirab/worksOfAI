from .eightNumberBoard import EightNumberBoard

class Game:
    def __init__(self):
        self.nodeNumber  = 0
        self.visitedList = []
        self.nodeList    = []

        self.board = EightNumberBoard()
        self.startNode = self.board.getBoard()
        self.finalNode = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    def getBlankIndexes(self, node):
        return [[i, n.index(0)] for i, n in enumerate(node) if 0 in n][0]

    def printNode(self, node):
        print(node[0][0],node[0][1],node[0][2])
        print(node[1][0],node[1][1],node[1][2])
        print(node[2][0],node[2][1],node[2][2])
        self.nodeNumber += 1
        print('Node:', self.nodeNumber)
        print('------')

    def checkFinal(self, node):
        if node == self.finalNode:
            self.printNode(node)
            return True
        if node not in self.visitedList:
            self.printNode(node)
            self.nodeList.append(node)
            self.visitedList.append(node)
        return False