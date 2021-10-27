from game.game import Game
from queue import Queue 
import time

class Bfs(Game):
    def __init__(self):
        super().__init__()
        self.queue = Queue()

    def checkFinal(self, node):
        if node == self.finalNode:
            self.printNode(node)
            return True
        if node not in self.visitedList:
            self.printNode(node)
            self.queue.put(node)
            self.visitedList.append(node)
        return False

    def run(self):
        found = False

        self.queue.put(self.board.getBoard())
        self.visitedList.append(self.board.getBoard())
        self.printNode(self.board.getBoard())
        t0 = time.time()

        while (not found and not self.queue.empty()):
            currentNode = self.queue.get()
            
            blankIndex = self.getBlankIndexes(currentNode)
            
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
    algorithm = Bfs()
    algorithm.run()