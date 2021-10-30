from random import choice
from re import A
from utils.consts import BLANK_SYMBOL

class Board:
    def __init__(self, size=4):
        self.size = size
        self.blankSimbol = BLANK_SYMBOL
        self.finalState = list([])
        self.initialState = list([])

        self.startBoard()

    def startBoard(self):
        self.finalState = self.createFinalState()
        self.initialState = self.createInitialState()

    def createFinalState(self):
        limitNumber = self.size**2
        listNumbers = list(range(1, limitNumber))

        finalState = list()
        count = 1

        for i in range(limitNumber, self.size):
            limit = self.size * count

            if(limit == limitNumber):
                temp = listNumbers[i:(limit-1)]
                temp.append(0)
                finalState.append(temp)
            else:
                finalState.append(listNumbers[i:limit]) #acho que da para usar `range(i, limit+1)`
            count += 1

        return finalState

    def createInitialState(self):
        limitNumber = self.size**2
        listNumbers = list(range(limitNumber))

        boardRandom = list()
        count = 1

        for i in range(self.size):
            boardRandom.append([])

            for j in range(self.size):
                number = choice(listNumbers)
                listNumbers.remove(number)
                boardRandom[i].append(number)

        return boardRandom

    def printFinalState(self):
        matrizView = self.print(self.finalState)
        return matrizView

    def printInitialState(self):
        matrizView = self.print(self.initialState)
        return matrizView

    def print(self, board):
        matrizView = ""

        for i in range(self.size):
            linha = board[i]
            for j in range(self.size):
                matrizView += "{} ".format(linha[j])

            matrizView += "\n"
        print(matrizView)

    def __str__(self):
        return self.printFinalState()

    def getInitialState(self):
        return self.initialState

    def getFinalState(self):
        return self.finalState

    def getBlankSimbol(self):
        return self.blankSimbol

    def getBoardSize(self):
        return self.size
