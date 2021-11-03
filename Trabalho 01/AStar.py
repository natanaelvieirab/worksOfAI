from entity.Game import Game
from entity.utils.enums import Direction
from entity.utils.BoardUtil import BoardUtil
from heapq import heappush, heappop
from tests.data import *
import itertools
import time


class Manhattan:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.nodeListBackup = list()
        self.listVisited = list()
        self.heap = []

    def manhattanDistance(self, nodeCurrent):
        length = len(nodeCurrent)
        node = list(itertools.chain(*nodeCurrent))

        total = sum(
            abs((val - 1) % length - i % length) +
            abs((val - 1)//length - i//length)
            for i, val in enumerate(node) if val
        )

        return total

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = BoardUtil.tryMove(node, direction)

        if(nodeMoved == None or (nodeMoved in self.listVisited)):
            return False

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if isFound:
            self.game.printNodeAndInformation(nodeMoved)
            return True

        # valor da heurística do nó n até um nó objetivo (distancia em linha reta no caso de distancias espaciais)
        h = self.manhattanDistance(nodeMoved)
        g = len(nodeMoved)  # custo do caminho do nó inicial até o nó n
        f = g+h  # custo total

        heappush(self.heap, (f, nodeMoved))
        self.nodeListBackup.append(nodeMoved)

        return isFound

    def getBestWay(self):
        """Removendo o menor valor da pilha"""
        currentNode = heappop(self.heap)[1] if len(
            self.heap) != 0 else self.nodeListBackup[0]

        self.nodeListBackup.pop(self.nodeListBackup.index(currentNode))

        self.listVisited.append(currentNode)
        self.game.printNodeAndInformation(currentNode)

        return currentNode

    def start(self):

        currentNode = self.game.getInitialState()

        print("tabuleiro Inicial:")
        self.game.print(currentNode)
        print(" --------------- ")

        time0 = time.time()

        if(not self.game.isSolvable()):
            print("Este tabuleiro não possui solução!")
            return

        self.nodeListBackup.append(currentNode)

        isFound = self.game.isCheckIfFinalState(currentNode)

        while(not isFound):
            currentNode = self.getBestWay()
            self.heap = []

            for direction in Direction:
                if(isFound):
                    break

                isFound = self.moveAndCheck(currentNode, direction)

        time1 = time.time()

        print("----Finalizado----")
        print(f"foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)


m = Manhattan(requiredData[0]["board"])
# m = Manhattan(data[0]["board"])
# m = Manhattan()
m.start()

'''
Relatorio de busca:
    entrada: 
        [
            [1, 2, 3, 4],
            [5, 6, 8, 12],
            [13, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    > Tempo de execução: 0.003942012786865234
    > Nos visitados: 13
    --------------------------------------
       [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ],
    > Tempo de execução: 0.0008709430694580078
    > Nos visitados: 3
    --------------------------------------
'''
