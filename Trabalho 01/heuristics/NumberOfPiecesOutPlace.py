def numberOfPiecesOutPlace(boardCurrent: list, boardFinal: list):
    piecesOutPlace = 0

    for i in range(len(boardCurrent)):
        for j in range(len(boardCurrent)):
            if boardCurrent[i][j] != boardFinal[i][j]:
                piecesOutPlace += 1

    return piecesOutPlace
