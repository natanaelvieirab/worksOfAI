def selectBoardByHeuristic(boardsList: list, boardFinal, heuristicFunction):
    numberMin = heuristicFunction(boardsList[0], boardFinal)
    numberMinPos = 0

    for i in range(1, len(boardsList)):
        numberCurrent = heuristicFunction(boardsList[i], boardFinal)

        if(numberCurrent < numberMin):
            numberMin = numberCurrent
            numberMinPos = i
        
    return (boardsList[numberMinPos], numberMin)
