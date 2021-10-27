from game.game import Game
from heapq import heappush, heappop
import time
import itertools
import time

class Manhanttan(Game):
    def heuristic(self, a):
        result = 0

        node = list(itertools.chain(*a))

        for current, target in enumerate(node):
            currentRow = int(current/3)
            currentColumn = current%3
            targetRow = int(target/3)
            targetColumn = target%3
            result += abs(currentRow-targetRow) + abs(currentColumn-targetColumn)

        return result

    def run(self):
        self.nodeList.append(self.startNode)
        self.visitedList.append(self.startNode)

        t0 = time.time()

        found = False

        while (not found and len(self.nodeList) != 0):
            fList = []
            for node in self.nodeList:
                h = self.heuristic(node)
                g = len(node)
                f = g+h
                heappush(fList, (f, node))

            currentNode = self.nodeList.pop(
                self.nodeList.index(
                    heappop(fList)[1]
                )
            )

            blankIndex = self.getBlankIndexes(currentNode)

            if self.board.canMoveTop(blankIndex):
                topNode = self.board.top(currentNode, blankIndex[0], blankIndex[1])
                found = self.checkFinal(topNode)

            if self.board.canMoveLeft(blankIndex) and found == False:
                leftNode = self.board.left(currentNode, blankIndex[0], blankIndex[1])
                found = self.checkFinal(leftNode)

            if self.board.canMoveRight(blankIndex) and found == False:
                rightNode = self.board.right(currentNode, blankIndex[0], blankIndex[1])
                found = self.checkFinal(rightNode)

            if self.board.canMoveBottom(blankIndex) and found == False:
                bottomNode = self.board.bottom(currentNode, blankIndex[0], blankIndex[1])
                found = self.checkFinal(bottomNode)

        t1 = time.time()
        print('Time:', t1-t0)
        print('------')    


if __name__ == '__main__':
    algorithm = Manhanttan()
    algorithm.run()
    