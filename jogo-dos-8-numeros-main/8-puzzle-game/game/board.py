class Board:
    def __init__(self, size):
        self.size = size
        self.matrix = [[None for j in range(size)] for i in range(size)]
        # cria a matriz onde:
        #[[None for j in range(TamColuna)] for i in range(TamLinha)]
        # TamColuna: quantidade de coluna que deve ter a matriz;
        # TamLinha: quantidade de linha que deve ter a matriz;
        # None é o valor que será adicionado nas "celulas"

    def update(self, i, j, value):
        self.matrix[i][j] = value

    # definindo um método para exibir quando é usado o print
    def __str__(self):
        result = ""

        for i in range(self.size):
            for j in range(self.size):
                result += "{} ".format(self.matrix[i][j])
            result += "\n" if i+1 < self.size else ""

        return result
