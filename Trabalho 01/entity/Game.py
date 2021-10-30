from __pycache__.Board import Board
from utils.consts import EMPTY_VALUE

class Game(Board):
    def __init__(self):
        super().__init__()
        self.blankSimbol = super().getBlankSimbol()
        self.boardSize = super().getBoardSize()

    def __str__(self):
        return super().__str__()

    def getBlankPosition(self, node):
        length = len(node)

        for i in range(self.boardSize):
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
    def isCheckIfFinalState(self, node) -> bool:
        return node == self.finalState

    def _is_inversion(self, value1: int, value2: int) -> bool:
        """Verifica se é uma inversão."""
        return value1 != EMPTY_VALUE and value2 != EMPTY_VALUE and value2 > value1

    def get_inversions_number(self, arr: list) -> int:
        """A partir de um array, obtem-se o número de inversões."""

        # Transformar um arr(list) em um Board
        inversions_count = 0

        for i in range(self, len(arr)):
            for j in range(i + 1, len(arr)):
                if self.is_inversion(arr[j], arr[i]):
                    inversions_count += 1
        return inversions_count

    def get_position_of_empty_value_from_bottom(self, puzzle: list) -> int:
        """Procura pelo Empty_Value, iniciando a busca pela posição final (canto direito-inferior)."""

        # Transformar um puzzle(list) em um Board
        for i in range(self.boardSize - 1, -1, -1):
            for j in range(self.boardSize - 1, -1, -1):
                if puzzle[i, j] == EMPTY_VALUE:
                    return self.boardSize - i # Verificar isso
        return 0
