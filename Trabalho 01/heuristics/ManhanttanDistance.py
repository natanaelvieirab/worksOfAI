from entity.Position import Position

def manhattanDistance(self, boardCurrent: list, boardFinal: list):
    # somatório das distâncias de cada peça ao seu lugar na configuração final)

    sum = 0

    for i in range(len(boardCurrent)):
        for j in range(len(boardCurrent[i])):
            positionDestiny = findCorrectPosition(boardCurrent[i][j], boardFinal)
            sum += calcDistance(Position(i, j), positionDestiny)

    return sum

def findCorrectPosition(piece: int, boardFinal: list):
    for i in range(len(boardFinal)):
        for j in range(len(boardFinal[i])):
            if(boardFinal[i][j] == piece):
                return Position(i, j)
    return (0, 0)

def calcDistance(positionCurrent: Position, positionDestiny: Position) -> int:
    return abs(positionCurrent.line - positionDestiny.line) + abs(positionCurrent.column - positionDestiny.column)
