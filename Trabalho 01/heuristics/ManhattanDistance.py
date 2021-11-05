import itertools

def manhattanDistance(nodeCurrent):
    length = len(nodeCurrent)
    node = list(itertools.chain(*nodeCurrent))

    total = sum(
        abs((val - 1) % length - i % length) +
        abs((val - 1)//length - i//length)
        for i, val in enumerate(node) if val
    )

    return total
