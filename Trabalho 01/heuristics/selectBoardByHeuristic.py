def selectBoardByHeuristic(boardsList: list, boardFinal, heuristicFunction):
    numberMin = heuristicFunction(boardsList[0], boardFinal)
    numberMinPos = 0

    for i in range(1, len(boardsList)):
        numberCurrent = heuristicFunction(boardsList[i], boardFinal)

        if(numberCurrent < numberMin):
            numberMin = numberCurrent
            numberMinPos = i
        
    return numberMinPos

def orderBoardListByValueHeuristic(boardsList: list, boardFinal, heuristicFunction):
    weights = []
    weightsIndex = []

    for i in range(len(boardsList)):
        numberCurrent = heuristicFunction(boardsList[i], boardFinal)
        weights.append(numberCurrent)
        weightsIndex.append(i)
    
    sortByWeights(weights, weightsIndex)

    return weightsIndex

def sortByWeights(weights: list, weightsIndex: list):
    for i in range(len(weights)):
        minPos = i

        for j in range(i, len(weights)):
            if(weights[j] < weights[minPos]):
                minPos = j
        
        temp = weights[i]
        tempIndex = weightsIndex[i]
        weights[i] = weights[minPos]
        weightsIndex[i] = weightsIndex[minPos]
        weights[minPos] = temp
        weightsIndex[minPos] = temp
