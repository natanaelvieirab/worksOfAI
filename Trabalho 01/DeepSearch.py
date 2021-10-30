from entity.Game import Game
from utils.enums import Direction


class DeepSearch:
    def __init__(self):
        self.game = Game()

    def start(self):
        isFound = False
        initialState = self.game.getInitialState()
        finalState = self.game.getFinalState()

        self.game.printNodeAndInformation(initialState)
        currentNode = initialState
        i = 0
        while(not isFound and i <= 1):
            i += 1

            isFound = self.game.isCheckIfFinalState(currentNode)

            if(self.game.can_move(Direction.TOP)):
                self.game.move(currentNode, Direction.TOP)
                isFound = self.game.isCheckIfFinalState(currentNode)
                self.game.printNodeAndInformation(currentNode)

            if(self.game.can_move(Direction.RIGHT) and not isFound):
                self.game.move(currentNode, Direction.RIGHT)
                isFound = self.game.isCheckIfFinalState(currentNode)
                self.game.printNodeAndInformation(currentNode)

            if(self.game.can_move(Direction.DOWN) and not isFound):
                self.game.move(currentNode, Direction.DOWN)
                isFound = self.game.isCheckIfFinalState(currentNode)
                self.game.printNodeAndInformation(currentNode)

            if(self.game.can_move(Direction.LEFT) and not isFound):
                self.game.move(currentNode, Direction.LEFT)
                isFound = self.game.isCheckIfFinalState(currentNode)
                self.game.printNodeAndInformation(currentNode)

             #isFound = self.game.isCheckIfFinalState(currentNode)

            # self.game.printNodeAndInformation(currentNode)


ds = DeepSearch()
ds.start()
