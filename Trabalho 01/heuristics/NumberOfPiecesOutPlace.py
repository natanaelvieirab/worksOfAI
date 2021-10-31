def numberOfPiecesOutPlace(board1: list, board2: list):
    piecesOutPlace = 0

    for i in range(len(board1)):
        for j in range(len(board1)):
            if board1[i][j] != board2[i][j]:
                piecesOutPlace += 1

    return piecesOutPlace
