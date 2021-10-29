from __pycache__.Game import Game


class DeepSearch:
    def __init__(self):
        self.game = Game()

    def start(self):
        isFound = False
        initialState = [[7, 4, 3, 10], [11, 0, 12, 6], [
            14, 1, 13, 9], [8, 2, 5, 15]]  # self.game.getInitialState()
        finalState = self.game.getFinalState()

        self.game.printNodeAndInformation(initialState)
        currentNode = initialState
        i = 0
        while(not isFound and i <= 3):
            i += 1
            blankPosition = self.game.getBlankPosition(currentNode)
            isFound = self.game.isCheckIfFinalState(currentNode)

            # if(isFound):
            #     self.game.printNodeAndInformation(currentNode)
            #     break

            if(self.game.canMoveTop(**blankPosition)):
                self.game.moveTop(currentNode, **blankPosition)
                blankPosition = self.game.getBlankPosition(currentNode)
                isFound = self.game.isCheckIfFinalState(currentNode)

            if(self.game.canMoveRight(**blankPosition)):
                self.game.moveRight(currentNode, **blankPosition)
                blankPosition = self.game.getBlankPosition(currentNode)
                isFound = self.game.isCheckIfFinalState(currentNode)

            if(self.game.canMoveDown(**blankPosition)):
                self.game.moveDown(currentNode, **blankPosition)
                blankPosition = self.game.getBlankPosition(currentNode)
                isFound = self.game.isCheckIfFinalState(currentNode)

            if(self.game.canMoveLeft(**blankPosition)):
                self.game.moveLeft(currentNode, **blankPosition)
                blankPosition = self.game.getBlankPosition(currentNode)
                isFound = self.game.isCheckIfFinalState(currentNode)

             #isFound = self.game.isCheckIfFinalState(currentNode)

            self.game.printNodeAndInformation(currentNode)


ds = DeepSearch()
ds.start()
