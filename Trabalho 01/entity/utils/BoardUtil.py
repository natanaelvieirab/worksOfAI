import copy
from ..Board import Board
from ..Position import Position
from .enums import Direction


class BoardUtil():
    def getBlankPosition(node: Board) -> Position:
        for i in range(0, node.size):
            line = node[i]

            if(node.blankSymbol in line):
                return Position(i, line.index(node.blankSymbol))

    def can_move(node: Board, direction: Direction) -> bool:
        """Verifica se a peça em branco pode ser movida na direção indicada."""
        
        if direction == Direction.TOP:
            return node.positionBlankSymbol.line > 0
        elif direction == Direction.RIGHT:
            return node.positionBlankSymbol.column < (node.size - 1)
        elif direction == Direction.DOWN:
            return node.positionBlankSymbol.line < (node.size - 1)
        else:
            return node.positionBlankSymbol.column > 0

    def move(self, node: Board, direction: Direction):
        """Move peça em branco na direção indicada."""

        line = node.positionBlankSymbol.line
        column = node.positionBlankSymbol.column
        nodeMoved = copy.deepcopy(node)

        if direction == Direction.TOP:
            line -= 1
        elif direction == Direction.RIGHT:
            column += 1
        elif direction == Direction.DOWN:
            line += 1
        else:
            column -= 1

        self._swap(nodeMoved, line, column)
        return nodeMoved

    def _swap(node: Board, lineValue: int, columnValue: int):
        """Troca uma peça de lugar com a peça em branco."""

        line = node.positionBlankSymbol.line
        column = node.positionBlankSymbol.column

        node[line][column] = node[lineValue][columnValue]
        node[lineValue][columnValue] = node.blankSymbol
        node.positionBlankSymbol.set_position(lineValue, columnValue)
