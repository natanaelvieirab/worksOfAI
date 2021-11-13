# f(x) = x2 - 3x + 4 assume o valor mínimo.
# [x] Assumir que x [-10, +10]
# [x] Codificar X como vetor binário
# [x] Criar uma população inicial com 4 indivíduos
# [] Aplicar Mutação com taxa de 1%
# [] Aplicar Crossover com taxa de 60%
# [] Usar seleção por torneio.
# [x] Usar 5 gerações.
from random import choice
from utils.Population import Population
from heapq import heappush, heappop


class Generic:
    def __init__(self, restrictionsPopulation=[]):
        self.sizePopulation = 4
        self.generationLimit = 5
        self.percentageCrossover = 60  # 60%
        self.population = self.initialPopulation(restrictionsPopulation)

    def initialPopulation(self, restrictionsPopulation: list) -> list:
        """Criando uma nova população aleatoria"""
        numbers = list(
            range(restrictionsPopulation[0], restrictionsPopulation[1]))

        population = []

        for i in range(0, self.sizePopulation):
            number = choice(numbers)
            numbers.remove(number)
            binary = self.__toBinary(number)
            population.append(Population(binary, number))

        return population

    def __toBinary(self, number) -> str:
        return "{0:b}".format(number)

    def __toDecimal(self, number) -> int:
        """Obsoleto"""
        return int(number, 2)

    def __fitnessFunction(self, value: int) -> int:
        # f(x) = x^{2} - 3x + 4
        return value**2 - 3*value + 4

    def start(self):

        for i in range(4, self.generationLimit):
            print(f"Geração {i+1}")
            heap = []

            for individual in self.population:
                result = self.__fitnessFunction(individual.value)
                heappush(heap, (result, individual.identification))

            # escolher o melhor para o cross-over
            children = self.__bestBoys(heap)
            # fazer mutação com os filhos

            # repetir o processo
            self.population = children

    def __bestBoys(self, heap) -> list:
        """Escolhendo os melhores individuos"""

        firstMostSignificant = heappop(heap)[1]
        children = []

        for i in range(1, self.sizePopulation//2):
            relevantIndividual = heappop(heap)[1]
            print(
                f"value:{relevantIndividual}, em decimal: {self.__toDecimal(relevantIndividual)}")
            children.append(self.__crossover(
                firstMostSignificant, relevantIndividual))

        return children

    def __crossover(self, identification1, identification2) -> Population:
        # ao extrair tem que levar em consideração:
        # se tem sinal , pq conta como caractere;
        # tamanho da string

        # ao juntar, levar em consideração o sinal

        indice1 = self.__getPositionCrossover(identification1)
        indice2 = self.__getPositionCrossover(identification2)
        length1 = len(identification1)
        length2 = len(identification2)
        str1 = identification1[indice1: length1]
        str2 = identification2[0: indice2]

        print(f"indice1: {indice1}; sendo o tamanho: {length1}")
        print(f"1: {identification1}")
        print(f"foi extraido o seguinte: {str1}")

        print(f"indice2: {indice2}; sendo o tamanho: {length2}")
        print(f"2: {identification2}")
        print(f"foi extraido o seguinte: {str2}")

        print(f"resultado da junção de 2 e 1 : {str2+str1}")
        individualGenerate = str2+str1

        return Population(individualGenerate, self.__toDecimal(individualGenerate))

    def __getPositionCrossover(self, identification):
        return (self.percentageCrossover * len(identification)) // 100

    def printPopulation(self):

        for i in range(0, self.sizePopulation):
            print(self.population[i])

    def __str__(self) -> str:
        pass


restrictionsPopulation = [-10, +10]
ag = Generic(restrictionsPopulation)
ag.start()
