from queue import Queue
from entity.Game import Game
from entity.Position import Position
from entity.utils.enums import Direction
from entity.utils.BoardUtil import BoardUtil
from tests.data import *
import time
import psutil


class WideSearch:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.checkQueue = Queue()
        self.listVisited = list()

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = BoardUtil.tryMove(node, direction)
        if(nodeMoved == None):
            return False

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if (nodeMoved not in self.listVisited):
            self.checkQueue.put(nodeMoved)
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

        self.checkQueue.put(currentNode)
        self.listVisited.append(currentNode)
        isFound = self.game.isCheckIfFinalState(currentNode)

        while(not isFound and not self.checkQueue.empty()):
            currentNode = self.checkQueue.get()  # removendo o primeiro elemento da fila

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


# ws = WideSearch(requiredData[0]["board"])
ws = WideSearch(data[0]["board"])
ws.start()

'''
Relatorio de busca:
    entrada (requiredData[0]): 
        [
            [1, 2, 3, 4],
            [5, 6, 8, 12],
            [13, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    > Tempo de execução: 30.70090365409851
    > Nos visitados: 17277
    > CPU em %: 69,2
    > Uso de memoria: {'total': 12250648576, 'available': 8503197696,
     'percent': 30.6, 'used': 3056144384, 'free': 6503276544,
     'active': 3907117056, 'inactive': 1279950848,
     'buffers': 241758208, 'cached': 2449469440, 'shared': 403890176,
     'slab': 219258880}

    --------------------------------------
    entrada requiredData[1]: 
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

    entrada : (data[0]):
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ]
    > Tempo de execução: 0.005639314651489258
    > Nós visitados: 9
     > CPU em %:0,0
    > Uso de memoria: {'total': 12250648576, 'available': 8411586560,
     'percent': 31.3, 'used': 3132882944,
      'free': 6411431936, 'active': 3983904768,
       'inactive': 1297326080, 'buffers': 242405376,
        'cached': 2463928320, 'shared': 418832384,
         'slab': 219439104}

    

'''
