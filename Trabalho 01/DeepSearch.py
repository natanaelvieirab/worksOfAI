from queue import Queue
from entity.Game import Game
from entity.Position import Position
from entity.utils.enums import Direction
from tests.data import *
import time


class DeepSearch:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.checkStack = []
        self.listVisited = list()
        self.index = 0

    def moveAndCheck(self, node, direction: Direction, positionBlankSymbol: Position) -> bool:
        nodeMoved = self.game.move(node, direction, positionBlankSymbol)

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if (nodeMoved not in self.listVisited):
            self.checkStack.insert(self.index, nodeMoved)
            self.index += 1

            self.listVisited.append(nodeMoved)
            self.game.printNodeAndInformation(nodeMoved)

        return isFound

    def start(self):

        currentNode = self.game.getInitialState()

        print("tabuleiro Inicial:")
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
            positionBlankSymbol = self.game.getBlankPosition(currentNode)

            self.index = 0

            if(self.game.can_move(Direction.TOP, positionBlankSymbol)):
                isFound = self.moveAndCheck(
                    currentNode, Direction.TOP, positionBlankSymbol)

            if(self.game.can_move(Direction.RIGHT, positionBlankSymbol) and not isFound):
                isFound = self.moveAndCheck(
                    currentNode, Direction.RIGHT, positionBlankSymbol)

            if(self.game.can_move(Direction.DOWN, positionBlankSymbol) and not isFound):
                isFound = self.moveAndCheck(
                    currentNode, Direction.DOWN, positionBlankSymbol)

            if(self.game.can_move(Direction.LEFT, positionBlankSymbol) and not isFound):
                isFound = self.moveAndCheck(
                    currentNode, Direction.LEFT, positionBlankSymbol)

        time1 = time.time()

        print("----Finalizado----")
        print(f"foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)


ds = DeepSearch(requiredData[0]["board"])
ds.start()
