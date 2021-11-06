from entity.utils.BoardUtil import BoardUtil
from entity.Game import Game
from entity.utils.enums import Direction
from tests.data import *
import psutil
import time


class DeepSearch:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.checkStack = []
        self.listVisited = list()
        self.index = 0
        self.qtdGeneratedNodes = 0
        self.qtdStoredNodes = 0

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = BoardUtil.tryMove(node, direction)
        if(nodeMoved == None):
            return False

        self.qtdGeneratedNodes += 1

        if (nodeMoved not in self.listVisited):
            self.checkStack.insert(self.index, nodeMoved)
            self.index += 1
            self.listVisited.append(nodeMoved)
            self.qtdStoredNodes += 1
            self.game.printNodeAndInformation(nodeMoved)

        isFound = self.game.isCheckIfFinalState(nodeMoved)
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

        self.checkStack.append(currentNode)
        isFound = self.game.isCheckIfFinalState(currentNode)
        self.qtdGeneratedNodes += 1
        self.qtdStoredNodes += 1

        POSITION_INITIAL = 0

        while(not isFound and len(self.checkStack) != 0):
            currentNode = self.checkStack.pop(POSITION_INITIAL)

            self.index = 0

            for direction in Direction:
                if(isFound):
                    break
                isFound = self.moveAndCheck(currentNode, direction)

        time1 = time.time()
        print("-------Finalizado------")
        print(f"Foram realizados {self.game.getCountMove()} movimentos!")

        print(f"Quantidade de nós Gerados: {self.qtdGeneratedNodes}")
        print(f"Quantidade de nós Armazenados: {self.qtdStoredNodes}")
        
        print("Tempo de execução: ", time1 - time0)
        print(f"CPU em %: {psutil.cpu_percent()}")
        print(f"Uso de memória: {psutil.virtual_memory()._asdict()}")


ds = DeepSearch(requiredData[0]["board"])
ds.start()
