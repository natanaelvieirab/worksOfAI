from entity.Board import Board
from entity.Position import Position
from utils.consts import BLANK_SYMBOL
from utils.enums import Direction

class Game(Board):
    def __init__(self):
        super().__init__()
        self.boardSize = super().getBoardSize()
        self.blankSimbol = super().getBlankSimbol()
        self.blank_symbol_pos = self.getBlankPosition2()

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

    def getBlankPosition2(self):
        board = self.getInitialState()

        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if(board[i][j] == BLANK_SYMBOL):
                    return Position(i, j)

    def printNodeAndInformation(self, node, nodeNumber="nonenenenen"):
        super().print(node)
        print("Node nº: ", nodeNumber, "\n")
        print("-------------------")

    def can_move(self, direction: Direction) -> bool:
        """Verifica se a peça em branco pode ser movida na direção indicada."""
        if direction == Direction.TOP:
            return self.blank_symbol_pos.line > 0 
        elif direction == Direction.RIGHT:
            return self.blank_symbol_pos.column < (self.boardSize - 1)
        elif direction == Direction.DOWN:
            return self.blank_symbol_pos.line < (self.boardSize - 1)
        else:
            return self.blank_symbol_pos.column > 0

    # Verificando se pode realizar o movimento
    def canMoveTop(self, **posBlankSimbol):
        return (posBlankSimbol["line"] - 1) != -1

    def canMoveRight(self, **posBlankSimbol):
        return (posBlankSimbol["column"] + 1) != self.boardSize

    def canMoveDown(self, **posBlankSimbol):
        return (posBlankSimbol["line"] + 1) != self.boardSize

    def canMoveLeft(self, **posBlankSimbol):
        return (posBlankSimbol["column"] - 1) != -1

    def move(self, direction: Direction, node) -> bool:
        """Move peça em branco na direção indicada."""
        line = self.blank_symbol_pos.line
        column = self.blank_symbol_pos.column

        if direction == Direction.TOP:
            line -= 1
        elif direction == Direction.RIGHT:
            column += 1
        elif direction == Direction.DOWN:
            line += 1
        else:
            column -= 1
        
        self._swap2(node, line, column)

    def _swap2(self, node, line: int, column: int):
        node[self.blank_symbol_pos.line][self.blank_symbol_pos.column] = node[line][column]
        node[line][column] = BLANK_SYMBOL
        self.blank_symbol_pos.set_position(line, column)

    # Realizando o movimento para uma direção
    def moveTop(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"] - 1, posBlankSimbol["column"], **posBlankSimbol)

    def moveRight(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"], posBlankSimbol["column"] + 1, **posBlankSimbol)

    def moveDown(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"] + 1, posBlankSimbol["column"], **posBlankSimbol)

    def moveLeft(self, node, **posBlankSimbol):
        self._swap(node, posBlankSimbol["line"], posBlankSimbol["column"] - 1, **posBlankSimbol)

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
        return value1 != BLANK_SYMBOL and value2 != BLANK_SYMBOL and value2 > value1

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
                if puzzle[i][j] == BLANK_SYMBOL:
                    return self.boardSize - i # Verificar isso
        return 0
