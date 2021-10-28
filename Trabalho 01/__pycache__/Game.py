
from Board import Board


class Game(Board):
    def __init__(self):
        super().__init__()
        self.blankSimbol = super().getBlankSimbol()

    def __str__(self):
        return super().__str__()

    def getBlankPosition(self, node):
        length = len(node)

        for i in range(0, self.size):
            line = node[i]

            if(self.blankSimbol in line):
                return {
                    "line": i,
                    "column": line.index(self.blankSimbol)
                }

    def printNodeAndInformation(self, node, nodeNumber):
        node = super().getInitialState()
        view = super().print(node)
        print("-------------------")
        print("Node nº: ", nodeNumber, "\n")

        return view


g = Game()
# testando herança
print(g.printInitialState())
# print(g.getBlankPosition([]))
print(g.printNodeAndInformation([], 212131))
