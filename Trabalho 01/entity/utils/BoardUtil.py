import copy
from entity.Board import Board
from entity.Position import Position
from entity.utils.enums import Direction


class BoardUtil():
    def getBlankPosition(node: Board) -> Position:
        for i in range(0, node.size):
            line = node[i]

            if(node.blankSimbol in line):
                return Position(i, line.index(node.blankSimbol))

    def printNodeAndInformation(self, node):
        """Exibir o nós únicos juntamente com sua representação numerica"""

        super().print(node)

        self.countMove += 1
        print(f"Node nº: {self.countMove} \n")
        print("-------------------")

    def can_move(node: Board, direction: Direction, positionBlankSymbol: Position) -> bool:
        """Verifica se a peça em branco pode ser movida na direção indicada."""
        
        if direction == Direction.TOP:
            return positionBlankSymbol.line > 0
        elif direction == Direction.RIGHT:
            return positionBlankSymbol.column < (node.size - 1)
        elif direction == Direction.DOWN:
            return positionBlankSymbol.line < (node.size - 1)
        else:
            return positionBlankSymbol.column > 0

    def move(self, node: Board, direction: Direction, positionBlankSymbol: Position):
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

    def _swap(node: Board, lineValue: int, columnValue: int, positionBlankSymbol: Position):

        node[positionBlankSymbol.line][positionBlankSymbol.column] = node[lineValue][columnValue]
        node[lineValue][columnValue] = node.blankSimbol


