class Board:
    def __init__(self, size):
        self.size = size
        self.matrix = [[None for j in range(size)] for i in range(size)]

    def update(self, i, j, value):
        self.matrix[i][j] = value
    
    def __str__(self):
        result = ""

        for i in range(self.size):
            for j in range(self.size):
                result += "{} ".format(self.matrix[i][j])
            result += "\n" if i+1 < self.size else ""

        return result