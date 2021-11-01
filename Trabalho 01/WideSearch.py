from queue import Queue
from entity.Game import Game
from entity.Position import Position
from entity.utils.enums import Direction
import time


class WideSearch:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.checkQueue = Queue()
        self.listVisited = list()

    def moveAndCheck(self, node, direction: Direction, positionBlankSymbol: Position) -> bool:
        nodeMoved = self.game.move(node, direction, positionBlankSymbol)

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if (nodeMoved not in self.listVisited):
            self.checkQueue.put(nodeMoved)
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

        self.checkQueue.put(currentNode)
        self.listVisited.append(currentNode)
        isFound = self.game.isCheckIfFinalState(currentNode)

        while(not isFound and not self.checkQueue.empty()):
            currentNode = self.checkQueue.get()  # removendo o primeiro elemento da fila
            positionBlankSymbol = self.game.getBlankPosition(currentNode)

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


ws = WideSearch([
    [1, 2, 3, 4],
    [13, 6, 8, 12],
    [5, 9, 0, 7],
    [14, 11, 10, 15]
])
ws.start()

'''
Relatorio de busca:
    entrada: 
        [
            [1, 2, 3, 4],
            [5, 6, 8, 12],
            [13, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    > Tempo de execução: 30.70090365409851
    > Nos visitados: 17277
    --------------------------------------
    entrada: 
        [
            [1, 2, 3, 4],
            [13, 6, 8, 12],
            [5, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    > Tempo de execução:0
    > Nos visitados: 0
    Não possui solução
    --------------------------------------

'''
