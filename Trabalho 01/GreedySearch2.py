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
        self.nodeStackBackup = list()
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

        return isFound

    def getBestWay(self):
        """Removendo o menor valor da pilha"""
        currentNode = heappop(self.heap)[1] if len(
            self.heap) != 0 else self.nodeStackBackup.pop()

        """Esvazia a heap e armazenar em uma pilha para resolver futuros conflitos"""
        while len(self.heap) != 0:
            self.nodeStackBackup.append(self.heap.pop()[1])

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

        heappush(self.heap, (2, currentNode))

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


m = GreedySearch2(requiredData[0]["board"])
# m = GreedySearch2(data[0]["board"])
# m = GreedySearch2()
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
    > Tempo de execução: 0.003081083297729492
    > Nos visitados: 13
    > CPU em %: 0
    > Uso de memoria: {'total': 12250648576, 'available': 9178820608, 'percent': 25.1,
     'used': 2318704640, 'free': 3690803200, 'active': 4203175936, 'inactive': 3492175872,
      'buffers': 642338816,
     'cached': 5598801920, 'shared': 428216320, 'slab': 519581696}
    
    --------------------------------------

    entrada data[0]: 
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ],
    > Tempo de execução: 0.0007140636444091797
    > Nos visitados: 3
    > CPU em %: 0.0
    > Uso de memoria: {'total': 12336910336, 'available': 7752753152, 'percent': 37.2, 
    'used': 3669565440, 'free': 6026121216, 'active': 4365422592, 'inactive': 1193197568, 
    'buffers': 228573184, 'cached': 2412650496, 'shared': 609591296, 'slab': 241496064}
    --------------------------------------

    entrada data[1]: 
        [
            [12, 1, 10, 2],
            [7, 11, 4, 14],
            [5, 0, 9, 15],
            [8, 13, 6, 3],
        ],
    > Tempo de execução: 3.9941036701202393
    > Nos visitados: 3294
    > CPU em %: 67,0
    > Uso de memoria: {'total': 12250648576, 'available': 9224286208,
     'percent': 24.7, 'used': 2286161920, 'free': 3736993792, 'active': 4169121792,
      'inactive': 3487752192, 'buffers': 641716224,
     'cached': 5585776640, 'shared': 415293440, 'slab': 519520256}
'''
