from entity.Game import Game
from entity.utils.enums import Direction
from entity.utils.BoardUtil import BoardUtil
from heapq import heappush, heappop
from tests.data import *
import itertools
import time
import psutil


class AStar:
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
        g = len(nodeMoved)  # custo do caminho do nó inicial até o nó n
        f = g+h  # custo total

        heappush(self.heap, (f, nodeMoved))

        return isFound

    def getBestWay(self):
        """Removendo o menor valor da pilha"""
        currentNode = heappop(self.heap)[1] if len(
            self.heap) != 0 else self.nodeStackBackup.pop()

        """Esvazia a heap e armazenar em uma pilha para resolver futuros conflitos"""
        length = len(self.heap) - 1
        while length >= 0:
            self.nodeStackBackup.append(self.heap.pop(length)[1])
            length -= 1

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

        heappush(self.heap, (16, currentNode))

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


# star = AStar(requiredData[0]["board"])
# star = AStar(data[0]["board"])
star = AStar()
star.start()

'''
Relatorio de busca:
    entrada requiredData[0]: 
        [
            [1, 2, 3, 4],
            [5, 6, 8, 12],
            [13, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    > Tempo de execução: 0.003197193145751953
    > Nos visitados: 13
    > CPU em %: 0,0
    > Uso de memoria:{'total': 12250648576, 'available': 8434409472,
     'percent': 31.2, 'used': 3116130304,
      'free': 6433632256, 'active': 3968139264,
       'inactive': 1281953792, 'buffers': 243056640,
        'cached': 2457829376, 'shared': 412561408, 'slab': 219697152}

    --------------------------------------
    entrada (data[0])
      [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ],
    > Tempo de execução: 0.0009090900421142578
    > Nos visitados: 3
    > CPU em %: 0,0
    > Uso de memoria:{'total': 12250648576, 'available': 8454516736,
     'percent': 31.0, 'used': 3112218624,
      'free': 6454185984, 'active': 3963432960,
       'inactive': 1275674624, 'buffers': 242647040,
        'cached': 2441596928, 'shared': 396390400, 'slab': 219541504}

    --------------------------------------
   entrada data[1]: 
        [
            [12, 1, 10, 2],
            [7, 11, 4, 14],
            [5, 0, 9, 15],
            [8, 13, 6, 3],
        ],
    > Tempo de execução: 4.639868974685669
    > Nos visitados: 3294
    > CPU em %: 72,3
    > Uso de memoria: {'total': 12250648576, 'available': 9224286208,
     'percent': 24.7, 'used': 2286161920, 'free': 3736993792, 'active': 4169121792,
      'inactive': 3487752192, 'buffers': 641716224,
     'cached': 5585776640, 'shared': 415293440, 'slab': 519520256}

'''
