from queue import Queue
from entity.Game import Game
from entity.Position import Position
from utils.BoardUtil import BoardUtil
from utils.enums import Direction
import time


class DeepSearch:
    def __init__(self):
        self.game = Game()
        self.checkStack = []
        self.listVisited = list()
        self.index = 0

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = BoardUtil.move(node, direction)

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

        # if(not self.game.isSolvable()):
        #     print("Este tabuleiro não possui solução!")
        #     return

        self.checkStack.append(currentNode)
        isFound = self.game.isCheckIfFinalState(currentNode)
        POSITION_INITIAL = 0

        while(not isFound and len(self.checkStack) != 0):
            currentNode = self.checkStack.pop(POSITION_INITIAL)
            positionBlankSymbol = self.game.getBlankPosition(currentNode)

            self.index = 0

            if(BoardUtil.can_move(currentNode, Direction.TOP)):
                isFound = self.moveAndCheck(
                    currentNode, Direction.TOP)

            if(BoardUtil.can_move(currentNode, Direction.RIGHT) and not isFound):
                isFound = self.moveAndCheck(
                    currentNode, Direction.RIGHT)

            if(BoardUtil.can_move(currentNode, Direction.DOWN) and not isFound):
                isFound = self.moveAndCheck(
                    currentNode, Direction.DOWN)

            if(BoardUtil.can_move(currentNode, Direction.LEFT) and not isFound):
                isFound = self.moveAndCheck(
                    currentNode, Direction.LEFT)

        time1 = time.time()
        # if(isFound):
        print("----Finalizado----")
        print(f"foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)
        # else:
        #     print("Não foi possivel encontrar uma solução para o problema")


ds = DeepSearch()
ds.start()
