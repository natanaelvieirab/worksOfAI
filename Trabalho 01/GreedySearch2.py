from entity.Game import Game
from entity.utils.enums import Direction
from entity.utils.BoardUtil import BoardUtil
from heapq import heappush, heappop
from tests.data import *
import itertools
import time
import psutil


class GreedySearch2:
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

        heappush(self.heap, (h, nodeMoved))
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

        print("Tabuleiro Inicial:")
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
        print(f"Foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)
        print(f"CPU em %: {psutil.cpu_percent()}")
        print(f"Uso de memoria: {psutil.virtual_memory()._asdict()}")


# m = GreedySearch2(requiredData[0]["board"])
# m = GreedySearch2(data[0]["board"])
m = GreedySearch2()
m.start()

'''
Relatorio de busca:
    entrada requiredData[0]: 
        [
            [1, 2, 3, 4],
            [5, 6, 8, 12],
            [13, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    > Tempo de execução: 0.0034284591674804688
    > Nos visitados: 13
    > CPU em %: 64.1
    > Uso de memoria: {'total': 12336910336, 'available': 7774638080, 'percent': 37.0, 
    'used': 3650940928, 'free': 6048718848, 'active': 4342054912, 'inactive': 1193250816, 
    'buffers': 228106240, 'cached': 2409144320, 'shared': 606400512, 'slab': 241328128}
    
    --------------------------------------

    entrada data[0]: 
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ],
    > Tempo de execução: 0.0007767677307128906
    > Nos visitados: 3
    > CPU em %: 0.0
    > Uso de memoria: {'total': 12336910336, 'available': 7752753152, 'percent': 37.2, 
    'used': 3669565440, 'free': 6026121216, 'active': 4365422592, 'inactive': 1193197568, 
    'buffers': 228573184, 'cached': 2412650496, 'shared': 609591296, 'slab': 241496064}
'''
