from random import choice
from re import A


class Board:
    def __init__(self, size=4):
        self.size = size
        self.blankSimbol = 0
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

        for i in range(0, limitNumber, self.size):
            limit = self.size * count

            if(limit == limitNumber):
                temp = listNumbers[i:(limit-1)]
                temp.append(0)
                finalState.append(temp)
            else:
                finalState.append(listNumbers[i:limit])
            count += 1

        return finalState

    def getInitialState(self):
        return self.initialState

    def createInitialState(self):
        limitNumber = self.size**2
        listNumbers = list(range(0, limitNumber))

        boardRandom = list()
        count = 1

        for i in range(0, self.size):
            boardRandom.append([])

            for j in range(0, self.size):
                number = choice(listNumbers)
                listNumbers.remove(number)

                boardRandom[i].append(number)

        return boardRandom

    def getFinalState(self):
        return self.finalState

    def printFinalState(self):
        matrizView = self.print(self.finalState)

        return matrizView

    def printInitialState(self):
        matrizView = self.print(self.initialState)

        return matrizView

    def print(self, matriz):
        matrizView = ""
        board = matriz

        for i in range(0, self.size):
            linha = board[i]
            for j in range(0, self.size):
                matrizView += "{} ".format(linha[j])

            matrizView += "\n"

        return matrizView

    def __str__(self):
        return self.printFinalState()

    def getBlankSimbol(self):
        return self.blankSimbol


# para testar
#b = Board()
# print(b)
