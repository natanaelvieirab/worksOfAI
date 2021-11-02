from entity.Game import Game
from entity.Position import Position
from entity.utils.enums import Direction
from entity.utils.BoardUtil import BoardUtil
from heuristics.ManhanttanDistance import manhattanDistance
from heapq import heappush, heappop
from tests.data import *
import time


class Manhattan:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.nodeList = list()
        self.listVisited = list()
        self.finalState = self.game.getFinalState()

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = BoardUtil.tryMove(node, direction)

        if(nodeMoved == None):
            return False

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if (nodeMoved not in self.listVisited):
            self.nodeList.append(nodeMoved)
            self.listVisited.append(nodeMoved)
            self.game.printNodeAndInformation(nodeMoved)

        return isFound

    def getBestWay(self):
        stack = []

        for node in self.nodeList:
            h = manhattanDistance(node, self.finalState)
            g = len(node)
            f = g+h

            heappush(stack, (f, node))
        """Removendo o menor valor da pilha, em seguida removendo esse caminho da lista de nos"""
        index = self.nodeList.index(heappop(stack)[1])
        currentNode = self.nodeList.pop(index)

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

        self.nodeList.append(currentNode)
        self.listVisited.append(currentNode)
        isFound = self.game.isCheckIfFinalState(currentNode)

        while(not isFound and len(self.nodeList) != 0):
            currentNode = self.getBestWay()

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
    > Tempo de execução: 0.03873133659362793
    > Nos visitados: 31
    --------------------------------------
'''
