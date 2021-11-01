from entity.Board import Board
from entity.Position import Position
from entity.utils.functions import isOdd, convert_board_in_list


class Game(Board):
    def __init__(self, initialBoard=[]):
        super().__init__(initialBoard)
        self.boardSize = super().getBoardSize()
        self.blankSimbol = super().getBlankSimbol()
        self.positionBlankSymbol = self.getBlankPosition(self.initialState)
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

    def getCountMove(self):
        return self.countMove

    # verificando se chegou a estado final
    def isCheckIfFinalState(self, node) -> bool:
        return node == self.finalState

    # verificando se o tabuleiro gerado possui solucao
    def isSolvable(self) -> bool:
        numberInversions = self.get_inversions_number()
        position = self.get_position_of_empty_value_from_bottom()

        if isOdd(self.boardSize):
            return not isOdd(numberInversions)
        else:
            if isOdd(position):
                return not isOdd(numberInversions)
            else:
                return isOdd(numberInversions)

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
        return self.boardSize - self.positionBlankSymbol.line


# só será verdade quando esse arquivo for executado
# LEMBRETE: Ao rodar localmente, remover o "entity" nas importações,
# e apos rodar, coloque-o de volta

if __name__ == "__main__":
    game = Game()
    board = [
        [7, 4, 3, 10], 
        [11, 0, 12, 6], 
        [14, 1, 13, 9], 
        [8, 2, 5, 15]
    ]

    # print(game.get_position_of_empty_value_from_bottom())
    print(game.isSolvable())
