from game.game import Game
from queue import Queue 
import time

class Dfs(Game):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.stack = []

    
    def checkFinal(self, node):
        if node == self.finalNode:
            self.printNode(node)
            return True

        if node not in self.visitedList:
            self.printNode(node)
            self.stack.insert(self.index, node)
            self.index += 1
            self.visitedList.append(node)
        return False

    def run(self):
        found = False

        self.stack.append(self.board.getBoard())
        self.visitedList.append(self.board.getBoard())
        self.printNode(self.board.getBoard())
        t0 = time.time()

        while (not found and len(self.stack) != 0):
            currentNode = self.stack.pop(0)
            
            blankIndex = self.getBlankIndexes(currentNode)

            self.index = 0

            if self.board.canMoveTop(blankIndex):
                found = self.checkFinal(
                    self.board.top(currentNode, blankIndex[0], blankIndex[1])
                )
            if self.board.canMoveLeft(blankIndex) and found == False:
                found = self.checkFinal(
                    self.board.left(currentNode, blankIndex[0], blankIndex[1])
                )
            if self.board.canMoveRight(blankIndex) and found == False:
                found = self.checkFinal(
                    self.board.right(currentNode, blankIndex[0], blankIndex[1])
                )
            if self.board.canMoveBottom(blankIndex) and found == False:
                found = self.checkFinal(
                    self.board.bottom(currentNode, blankIndex[0], blankIndex[1])
                )

        t1 = time.time()
        print('Time:', t1-t0)
        print('------')


if __name__ == '__main__':
    algorithm = Dfs()
    algorithm.run()