import time
from entity.Game import Game
from entity.utils.BoardUtil import BoardUtil
from entity.utils.enums import Direction
from heuristics.NumberOfPiecesOutPlace import numberOfPiecesOutPlace
from heuristics.selectBoardByHeuristic import selectBoardByHeuristic
from tests.data import requiredData


class GreedySearch:
    def __init__(self, initialBoard=[]):
        self.game = Game(initialBoard)
        self.extendedNeighbors = list()
        self.visiteds = list()

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = BoardUtil.tryMove(node, direction)
        if(nodeMoved == None):
            return False

        isFound = False

        if(nodeMoved not in self.visiteds):
            isFound = self.game.isCheckIfFinalState(nodeMoved)
            self.extendedNeighbors.append(nodeMoved)
            self.visiteds.append(nodeMoved)

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

        self.visiteds.append(currentNode)

        isFound = self.game.isCheckIfFinalState(currentNode)

        while(not isFound):
            currentNode = self._getLastInserted(self.visiteds)

            self.extendedNeighbors = []
            for direction in Direction:
                isFound = self.moveAndCheck(currentNode, direction)

                if(isFound):
                    lastInserted = self._getLastInserted(self.extendedNeighbors)
                    self.visiteds.append(lastInserted)
                    self.game.printNodeAndInformation(lastInserted)
                    break

            if(self.extendedNeighbors == []):
                break
            self.useHeuristic(currentNode)

        time1 = time.time()

        print("----Finalizado----")
        print(f"Foram realizados {self.game.getCountMove()} movimentos!")
        print("Tempo de execucao: ", time1 - time0)

    def useHeuristic(self, currentNode):
        (neighborsWithLowerHeuristics, heuristic) = selectBoardByHeuristic(self.extendedNeighbors, self.game.getFinalState(), numberOfPiecesOutPlace)

        heuristicCurrentNode = numberOfPiecesOutPlace(currentNode, self.game.getFinalState())
        if(heuristic > heuristicCurrentNode):
            self.extendedNeighbors = []
            return
        
        self.visiteds.append(neighborsWithLowerHeuristics)
        self.game.printNodeAndInformation(neighborsWithLowerHeuristics)
        self.extendedNeighbors = []

    def _getLastInserted(self, array):
        return array[len(array) -1]


if __name__ == '__main__':
    gs = GreedySearch(requiredData[0]["board"])
    gs.start()
