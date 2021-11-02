import copy
from entity.Position import Position
from entity.utils.enums import Direction
from entity.utils.const import BLANK_SYMBOL


class BoardUtil():
    @staticmethod
    def getBlankPosition(node: list) -> Position:
        for i in range(0, len(node)):
            for j in range(0, len(node[i])):
                if(node[i][j] == BLANK_SYMBOL):
                    return Position(i, j)
        return Position(0,0)

    @staticmethod
    def can_move(node: list, direction: Direction, positionBlankSymbol: Position) -> bool:
        """Verifica se a peça em branco pode ser movida na direção indicada."""
        
        if direction == Direction.TOP:
            return positionBlankSymbol.line > 0
        elif direction == Direction.RIGHT:
            return positionBlankSymbol.column < (len(node) - 1)
        elif direction == Direction.DOWN:
            return positionBlankSymbol.line < (len(node) - 1)
        else:
            return positionBlankSymbol.column > 0

    @staticmethod
    def move(node: list, direction: Direction, positionBlankSymbol: Position):
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

        BoardUtil.swap(nodeMoved, line, column, positionBlankSymbol)
        return nodeMoved

    @staticmethod
    def swap(node: list, lineValue: int, columnValue: int, positionBlankSymbol: Position):
        """Troca uma peça de lugar com a peça em branco."""

        node[positionBlankSymbol.line][positionBlankSymbol.column] = node[lineValue][columnValue]
        node[lineValue][columnValue] = BLANK_SYMBOL

    @staticmethod
    def tryMove(node: list, direction: Direction):
        positionBlankSymbol = BoardUtil.getBlankPosition(node)

        if(BoardUtil.can_move(node, direction, positionBlankSymbol)):
            return BoardUtil.move(node, direction, positionBlankSymbol)
        return None
