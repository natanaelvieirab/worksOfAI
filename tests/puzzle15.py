from consts import EMPTY_VALUE
from functions import is_odd

DIMENSIONS = 4 # dimensão 4 => 4*4 = 16 

def is_inversion(value1: int, value2: int):
    """Verifica se é uma inversão."""
    return value1 != EMPTY_VALUE and value2 != EMPTY_VALUE and value2 > value1

def get_inversions_number(arr: list):
    """A partir de um array, obtem-se o número de inversões."""
    inversions_count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if is_inversion(arr[j], arr[i]):
                inversions_count += 1
    return inversions_count

def is_15_puzzle_solvable(puzzle) :
    inversions_count = get_inversions_number([j for sub in puzzle for j in sub])

    if is_odd(DIMENSIONS):
        return not is_odd(inversions_count)
    else:
        position_of_empty_value_from_bottom = get_position_of_empty_value_from_bottom(puzzle)
        if is_odd(position_of_empty_value_from_bottom):
            return not is_odd(inversions_count)
        else:
            return is_odd(inversions_count)
    return False

def get_position_of_empty_value_from_bottom(puzzle: list) -> int:
    """Procura pelo Empty_Value, iniciando a busca pela posição final (canto direito-inferior)."""
    for i in range(DIMENSIONS - 1, -1, -1):
        for j in range(DIMENSIONS - 1, -1, -1):
            if puzzle[i, j] == EMPTY_VALUE:
                return DIMENSIONS - i # Tem que corrigir isso
    return 0

# Driver code
puzzle = [[1, 8, 2],[0, 4, 3],[7, 6, 5]]

if is_15_puzzle_solvable(puzzle):
    print("Solvable")
else:
    print("Not Solvable")
