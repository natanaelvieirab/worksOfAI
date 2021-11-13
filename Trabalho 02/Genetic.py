from utils.Operations import Operations
from heapq import heappop, heappush


class Genetic(Operations):
    def __init__(self, restrictionsPopulation=[], generationLimit=5, sizePopulation=4):
        super().__init__(restrictionsPopulation, generationLimit, sizePopulation)

    def calculatingProbability(self, heapFitnessFunction):
        sum = 0
        heapProbability = []

        for individual in self.population:
            result = super().fitnessFunction(individual.value)
            sum += result
            heappush(heapFitnessFunction, (result, individual.identification))

        for h in heapFitnessFunction:
            probability = (h[0]/sum) * 100
            heappush(heapProbability, (probability, h[1]))

        return heapProbability

    def start(self):

        print("população inicial:")
        self.printPopulation()

        for i in range(0, self.generationLimit):
            print(f"Geração {i+1}")
            heap = []

            heap = self.calculatingProbability(heap)

            # escolher os melhores para o cross-over
            children = self.bestBoys(heap)

            # fazer mutação com os filhos
            self.population = self.mutation(children)

            # Mostrar a nova população e repetir o processo
            self.printPopulation()

    def __str__(self) -> str:
        pass


if __name__ == '__main__':
    restrictionsPopulation = [-10, +10]
    ag = Genetic(restrictionsPopulation)
    ag.start()
