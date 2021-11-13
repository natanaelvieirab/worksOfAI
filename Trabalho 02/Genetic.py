# f(x) = x2 - 3x + 4 assume o valor mínimo.
# [x] Assumir que x [-10, +10]
# [x] Codificar X como vetor binário
# [x] Criar uma população inicial com 4 indivíduos
# [] Aplicar Mutação com taxa de 1%
# [] Aplicar Crossover com taxa de 60%
# [] Usar seleção por torneio.
# [x] Usar 5 gerações.
from utils.Individual import Individual
from utils.Operations import Operations
from heapq import heappush


class Genetic(Operations):
    def __init__(self, restrictionsPopulation=[], generationLimit=5, sizePopulation=4):
        super().__init__(restrictionsPopulation, generationLimit, sizePopulation)

    def start(self):

        print("população inicial:")
        self.printPopulation()

        for i in range(0, self.generationLimit):
            print(f"Geração {i+1}")
            heap = []

            for individual in self.population:
                result = super().fitnessFunction(individual.value)
                heappush(heap, (result, individual.identification))

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
