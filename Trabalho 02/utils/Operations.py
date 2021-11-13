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
        # print(
        #     f"mais significativo:{firstMostSignificant}, em decimal:{self.__toDecimal(firstMostSignificant)}\n")

        for i in range(0, self.sizePopulation//2):
            relevantIndividual = heappop(heap)[1]
            # print(
            #     f"value:{relevantIndividual}, em decimal: {self.__toDecimal(relevantIndividual)}")

            aux = self.__crossover([firstMostSignificant, relevantIndividual])

            children.append(aux[0])
            children.append(aux[1])

        return children

    def __crossover(self, identifications) -> list:
        # ao extrair tem que levar em consideração:
        # [x] se tem sinal , pq conta como caractere;
        # [x] tamanho da string

        # ao juntar, levar em consideração o sinal ?
        piece = []
        children = []

        interation = 1
        for identification in identifications:
            if '-' in identification:
                # print(f"O numero {identification} é negativo")
                isNegative = True
                identification = identification.split('-')[1]

            pos = self.__getPositionCrossover(identification)
            length = len(identification)

            if pos == length:
                length += 1

            if pos == 0 and length == 1:
                pos += 1

            genes1 = identification[pos: length] if interation == 1 else identification[0: pos]
            genes2 = identification[0: pos] if interation == 1 else identification[pos: length]

            # print(
            #     f"identificador{interation}: {identification}\tindice:{pos}\tlen:{length}\textraido:{genes1} e {genes2}")
            piece.append(genes1)
            piece.append(genes2)
            interation += 1

        """Embaralhando genes"""
        individualGenerate = piece[0]+piece[3]
        individualGenerate2 = piece[2]+piece[1]

        print(f"resultado da junção de 0 e 3 : {individualGenerate}\n")
        print(f"resultado da junção de 2 e 1 : {individualGenerate2}\n")

        children.append(Individual(individualGenerate,
                                   self.__toDecimal(individualGenerate)))
        children.append(Individual(individualGenerate2,
                                   self.__toDecimal(individualGenerate2)))

        return children

    def __getPositionCrossover(self, identification):
        return (self.percentageCrossover * len(identification)) // 100

    # realizando mutação nos filhos

    def mutation(self, children: list) -> list:
        mutants = []
        # e o sinal ?
        for child in children:
            identification = list(child.identification)

            positions = list(range(0, len(identification)))
            pos = choice(positions)  # gerando uma posicao aleatoria

            identification[pos] = '0' if identification[pos] == '1' else '1'

            child.identification = ''.join(identification)

            mutants.append(child)

        return mutants

    def printPopulation(self):

        for individual in self.population:
            print(individual)

        print("--------------------------------")

    def __str__(self) -> str:
        pass
