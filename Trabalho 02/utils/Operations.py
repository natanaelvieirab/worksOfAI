from utils.Individual import Individual
from random import choice
from heapq import heappop, heappush


class Operations:
    def __init__(self, restrictionsPopulation, generationLimit, sizePopulation):
        self.sizePopulation = sizePopulation
        self.generationLimit = generationLimit
        self.percentageCrossover = 60  # 60%
        self.population = self.__initialPopulation(restrictionsPopulation)

    def __initialPopulation(self, restrictionsPopulation: list) -> list:
        """Criando uma nova população aleatoria"""
        numbers = list(
            range(restrictionsPopulation[0], restrictionsPopulation[1]))

        population = []

        for i in range(0, self.sizePopulation):
            number = choice(numbers)
            numbers.remove(number)
            binary = self.__toBinary(number)
            population.append(Individual(binary, number))

        return population

    def __toBinary(self, number) -> str:
        return "{0:b}".format(number)

    def __toDecimal(self, number) -> int:
        return int(number, 2) if number != '' else 0

    def fitnessFunction(self, value: int) -> int:
        # f(x) = x^{2} - 3x + 4
        return value**2 - 3*value + 4

    # gerando filhos a partir dos melhores candidatos
    def bestBoys(self, heap) -> list:
        """Escolhendo os melhores individuos"""

        firstMostSignificant = heappop(heap)[1]
        children = []

        for i in range(0, self.sizePopulation//2):
            relevantIndividual = heappop(heap)[1]

            aux = self.__crossover([firstMostSignificant, relevantIndividual])

            children.append(aux[0])
            children.append(aux[1])

        return children

    def __crossover(self, identifications) -> list:
        piece = []
        children = []

        interation = 1
        isNegative = False

        for identification in identifications:
            if '-' in identification:
                isNegative = True
                identification = identification.split('-')[1]

            pos = self.__getPositionCrossover(identification)
            length = len(identification)

            if length == 1:
                genes1 = genes2 = identification
            else:
                genes1 = identification[pos: length] if interation == 1 else identification[0: pos]
                genes2 = identification[0: pos] if interation == 1 else identification[pos: length]

            piece.append(genes1)
            piece.append(genes2)
            interation += 1

        """Embaralhando genes"""
        children.append(self.__join(piece[0], piece[3]))
        children.append(self.__join(piece[2], piece[1]))

        return children

    def __getPositionCrossover(self, identification):
        return (self.percentageCrossover * len(identification)) // 100

    def __join(self, genes1, genes2):
        individualGenerate = genes1 + genes2

        return Individual(individualGenerate,
                          self.__toDecimal(individualGenerate))

    # realizando mutação nos filhos

    def mutation(self, children: list) -> list:
        mutants = []

        for child in children:
            identification = list(child.identification)

            positions = list(range(0, len(identification)))
            pos = choice(positions)  # gerando uma posicao aleatoria

            identification[pos] = '0' if identification[pos] == '1' else '1'

            child.identification = ''.join(identification)
            child.value = self.__toDecimal(child.identification)

            mutants.append(child)

        return mutants

    def printPopulation(self):

        for individual in self.population:
            print(individual)

        print("--------------------------------")

    def __str__(self) -> str:
        pass
