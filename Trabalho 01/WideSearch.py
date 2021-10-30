from entity.Game import Game
from entity.Position import Position
from entity.utils.enums import Direction
from queue import Queue
import time


class DeepSearch:
    def __init__(self):
        self.game = Game()
        self.queue = Queue()

    def moveAndCheck(self, node, direction: Direction, positionBlankSymbol: Position) -> bool:
        nodeMoved = self.game.move(node, direction, positionBlankSymbol)
        self.queue.put(nodeMoved)

        isFound = self.game.isCheckIfFinalState(nodeMoved)
        self.game.printNodeAndInformation(nodeMoved)

        return isFound

    def start(self):

        initialState = self.game.getInitialState()

        print("tabuleiro Inicial:")
        self.game.print(initialState)
        print(" --------------- ")

        time0 = time.time()

        if(not self.game.isSolvable()):
            print("Este tabuleiro não possui solução!")
            return

        self.queue.put(initialState)
        isFound = self.game.isCheckIfFinalState(initialState)

        # i = 0
        while(not isFound and not self.queue.empty()):
            currentNode = self.queue.get()
            positionBlankSymbol = self.game.getBlankPosition()

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
        # if(isFound):
        print("----Finalizado----")
        self.game.print(currentNode)
        print(f"foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)
        # else:
        #     print("Não foi possivel encontrar uma solução para o problema")


ds = DeepSearch()
ds.start()
