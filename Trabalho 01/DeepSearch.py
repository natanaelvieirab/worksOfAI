from queue import Queue
from entity.utils.BoardUtil import BoardUtil
from entity.Game import Game
from entity.utils.enums import Direction
from entity.Position import Position
import time


class DeepSearch:
    def __init__(self):
        self.game = Game()
        self.checkStack = []
        self.listVisited = list()
        self.index = 0

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = BoardUtil.tryMove(node, direction)
        if(nodeMoved == None):
            return False

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if (nodeMoved not in self.listVisited):
            self.checkStack.insert(self.index, nodeMoved)
            self.index += 1
            self.listVisited.append(nodeMoved)
            self.game.printNodeAndInformation(nodeMoved)

        return isFound

    def start(self):
        currentNode = self.game.getInitialState()

        print("Tabuleiro Inicial:")
        self.game.print(currentNode)
        print(" --------------- ")

        time0 = time.time()

        if(not self.game.isSolvable()):
            print("Este tabuleiro não possui solução!")
            return

        self.checkStack.append(currentNode)
        isFound = self.game.isCheckIfFinalState(currentNode)
        POSITION_INITIAL = 0

        while(not isFound and len(self.checkStack) != 0):
            currentNode = self.checkStack.pop(POSITION_INITIAL)

            self.index = 0

            for  direction in Direction:
                if(isFound):
                    break
                isFound = self.moveAndCheck(currentNode, direction)

        time1 = time.time()
        print("----Finalizado----")
        print(f"foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)


ds = DeepSearch(requiredData[0]["board"])
ds.start()
