import copy
from entity.Board import Board
from entity.Position import Position
from entity.utils.enums import Direction
from entity.utils.functions import convert_board_in_list


class Game(Board):
    def __init__(self, initialBoard=[]):
        super().__init__(initialBoard)
        self.boardSize = super().getBoardSize()
        self.blankSimbol = super().getBlankSimbol()
        self.blank_symbol_pos = self.getBlankPosition(self.initialState)
        self.countMove = 0

    def __str__(self):
        return super().__str__()

    def getBlankPosition(self, node) -> Position:

        for i in range(0, self.boardSize):
            line = node[i]

            if(self.blankSimbol in line):
                return Position(i, line.index(self.blankSimbol))

    def printNodeAndInformation(self, node):
        """Exibir o nós únicos juntamente com sua representação numerica"""

        super().print(node)

        self.countMove += 1
        print(f"Node nº: {self.countMove} \n")
        print("-------------------")

    # referente ao movimento no simbolo branco
    def can_move(self, direction: Direction, positionBlankSymbol: Position) -> bool:
        """Verifica se a peça em branco pode ser movida na direção indicada."""

        if direction == Direction.TOP:
            return positionBlankSymbol.line > 0
        elif direction == Direction.RIGHT:
            return positionBlankSymbol.column < (self.boardSize - 1)
        elif direction == Direction.DOWN:
            return positionBlankSymbol.line < (self.boardSize - 1)
        else:
            return positionBlankSymbol.column > 0

    def move(self, node, direction: Direction, positionBlankSymbol: Position):
        """Move peça em branco na direção indicada."""

        line = positionBlankSymbol.line
        column = positionBlankSymbol.column
        nodeMoved = copy.deepcopy(node)

        if direction == Direction.TOP:
            line -= 1
        elif direction == Direction.RIGHT:
            column += 1
        elif direction == Direction.DOWN:
            line += 1
        else:
            column -= 1

        self._swap(nodeMoved, line, column, positionBlankSymbol)

        return nodeMoved

    def _swap(self, node, lineValue: int, columnValue: int, positionBlankSymbol: Position):

        node[positionBlankSymbol.line][positionBlankSymbol.column] = node[lineValue][columnValue]
        node[lineValue][columnValue] = self.blankSimbol

    def getCountMove(self):
        return self.countMove

    # verificando se chegou a estado final
    def isCheckIfFinalState(self, node) -> bool:
        return node == self.finalState

    # verificando se o tabuleiro gerado possui solucao
    def isSolvable(self) -> bool:
        numberInversions = self.get_inversions_number()
        position = self.get_position_of_empty_value_from_bottom()

        #print(f"numeros de inversões: {numberInversions}")
        #print(f"position: {position}")

        if self.boardSize % 2:
            return not numberInversions % 2
        else:
            if position % 2:
                return not numberInversions % 2
            else:
                return numberInversions % 2

    def _is_inversion(self, value1: int, value2: int) -> bool:
        """Verifica se é uma inversão."""
        return value1 != self.blankSimbol and value2 != self.blankSimbol and value1 < value2

    def get_inversions_number(self) -> int:
        """Obtem-se o número de inversões de elementos no board."""

        inversions_count = 0
        elements_list = convert_board_in_list(self.initialState)
        length = len(elements_list)

        for i in range(length):
            for j in range(i + 1, length):
                if self._is_inversion(elements_list[j], elements_list[i]):
                    inversions_count += 1

        return inversions_count

    def get_position_of_empty_value_from_bottom(self) -> int:
        """Procura pelo Empty_Value, iniciando a busca pela posição final (canto direito-inferior)."""
        # forma resumida
        return self.boardSize - self.blank_symbol_pos.line


# só será verdade quando esse arquivo for executado
# LEMBRETE: Ao rodar localmente, remover o "entity" nas importações,
# e apos rodar, coloque-o de volta

if __name__ == "__main__":
    game = Game()
    board = [[7, 4, 3, 10], [11, 0, 12, 6], [
        14, 1, 13, 9], [8, 2, 5, 15]]

    # print(game.get_position_of_empty_value_from_bottom())
    print(game.isSolvable())
