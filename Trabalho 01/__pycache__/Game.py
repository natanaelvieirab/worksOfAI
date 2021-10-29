

from __pycache__.Board import Board


class Game(Board):
    def __init__(self):
        super().__init__()
        self.blankSimbol = super().getBlankSimbol()
        self.boardSize = super().getBoardSize()

    def __str__(self):
        return super().__str__()

    def getBlankPosition(self, node):
        length = len(node)

        for i in range(0, self.size):
            line = node[i]

            if(self.blankSimbol in line):
                return {
                    "line": i,
                    "column": line.index(self.blankSimbol)
                }

    def printNodeAndInformation(self, node, nodeNumber="nonenenenen"):
        super().print(node)
        print("Node nº: ", nodeNumber, "\n")
        print("-------------------")

    # Verificando se pode realizar o movimento
    def canMoveTop(self, **posBlankSimbol):
        return (posBlankSimbol["line"] - 1) != -1

    def canMoveRight(self, **posBlankSimbol):
        return (posBlankSimbol["column"] + 1) != self.boardSize

    def canMoveDown(self, **posBlankSimbol):
        return (posBlankSimbol["line"] + 1) != self.boardSize

    def canMoveLeft(self, **posBlankSimbol):
        return (posBlankSimbol["column"] - 1) != -1

    # Realizando o movimento para uma direção
    def moveTop(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"] - 1,
                   posBlankSimbol["column"], **posBlankSimbol)

    def moveRight(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"],
                   posBlankSimbol["column"] + 1, **posBlankSimbol)

    def moveDown(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"] + 1,
                   posBlankSimbol["column"], **posBlankSimbol)

    def moveLeft(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"],
                   posBlankSimbol["column"] - 1, **posBlankSimbol)

    # Realizando a troca de posição
    def _swap(self, node, lineValue, columnValue,  **kwargs):
        line = kwargs["line"]
        column = kwargs["column"]

        value = node[lineValue][columnValue]
        node[lineValue][columnValue] = self.blankSimbol
        node[line][column] = value

    # verificando se chegou a estado final
    def isCheckIfFinalState(self, node):
        return node == self.finalState
