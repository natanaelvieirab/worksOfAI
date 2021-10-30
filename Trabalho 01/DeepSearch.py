from entity.Game import Game
from entity.utils.enums import Direction
import time


class DeepSearch:
    def __init__(self):
        self.game = Game()

    def moveAndCheck(self, currentNode, direction: Direction) -> bool:
        self.game.move(currentNode, direction)
        isFound = self.game.isCheckIfFinalState(currentNode)
        self.game.printNodeAndInformation(currentNode)

        return isFound

    def start(self):

        initialState = self.game.getInitialState()

        print("tabuleiro Inicial:")
        self.game.print(initialState)
        print(" --------------- ")

        time0 = time.time()

        if(not self.game.isSolvable()):
            print("Este tabuleiro não possui solução!")
            return

        currentNode = initialState
        isFound = self.game.isCheckIfFinalState(currentNode)

        i = 0
        while(not isFound and i <= 1):
            i += 1

            if(self.game.can_move(Direction.TOP)):
                isFound = self.moveAndCheck(currentNode, Direction.TOP)

            if(self.game.can_move(Direction.RIGHT) and not isFound):
                isFound = self.moveAndCheck(currentNode, Direction.RIGHT)

            if(self.game.can_move(Direction.DOWN) and not isFound):
                isFound = self.moveAndCheck(currentNode, Direction.DOWN)

            if(self.game.can_move(Direction.LEFT) and not isFound):
                isFound = self.moveAndCheck(currentNode, Direction.LEFT)

        time1 = time.time()
        if(isFound):
            print("----Finalizado----")
            self.game.print(currentNode)
            print(f"foram realizado {self.game.getCountMove()} movimentos!")
            print("Tempo de execucao: ", time1-time0)
        else:
            print("Não foi possivel encontrar uma solução para o problema")


ds = DeepSearch()
ds.start()
