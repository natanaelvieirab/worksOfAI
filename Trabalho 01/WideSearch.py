from queue import Queue
from entity.Game import Game
from entity.Position import Position
from entity.utils.enums import Direction
from entity.utils.BoardUtil import BoardUtil
from tests.data import *
import time


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
        print(f"foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)


# ws = WideSearch(requiredData[1]["board"])
ws = WideSearch(data[0]["board"])
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

    entrada : (data[0]):
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 0, 11],
            [13, 14, 15, 12]
        ]
    > Tempo de execução: 0.005639314651489258
    > Nós visitados: 9
    

'''
