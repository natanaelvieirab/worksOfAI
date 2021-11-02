import time
from queue import Queue
from entity.Game import Game
from entity.Position import Position
from entity.utils.enums import Direction
from heuristics.NumberOfPiecesOutPlace import numberOfPiecesOutPlace
from heuristics.selectBoardByHeuristic import selectBoardByHeuristic
from tests.data import requiredData


class GreedySearch:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.nodesList = list()
        self.tempList = list()
        self.visiteds = list()

    def moveAndCheck(self, node, direction: Direction, positionBlankSymbol: Position) -> bool:
        nodeMoved = self.game.move(node, direction, positionBlankSymbol)

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if(nodeMoved not in self.visiteds):
            self.tempList.append(nodeMoved)

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

        self.nodesList.append(currentNode)

        isFound = self.game.isCheckIfFinalState(currentNode)

        while(not isFound):
            currentNode = self._getLastInserted(self.nodesList)
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
        
            if(isFound):
                self.nodesList.append(self._getLastInserted(self.tempList))
                currentNode = self._getLastInserted(self.nodesList)
                self.game.printNodeAndInformation(currentNode)
                break

            if(self.tempList == []):
                break
            self.useHeuristic()
        time1 = time.time()

        print("----Finalizado----")
        print(f"foram realizado {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1-time0)

    def useHeuristic(self):
        indexMin = selectBoardByHeuristic(self.tempList, self.game.getFinalState(), numberOfPiecesOutPlace)
        
        self.nodesList.append(self.tempList[indexMin])
        self.visiteds.append(self.tempList[indexMin])
        self.game.printNodeAndInformation(self.tempList[indexMin])
        self.tempList = []

    def _getLastInserted(self, array):
        return array[len(array) -1]

gs = GreedySearch()
# gs = GreedySearch(requiredData[0]["board"])
gs.start()


