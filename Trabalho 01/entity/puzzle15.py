from entity.Game import Game
from utils.functions import isOdd

def is_15_puzzle_solvable(puzzle: Game):
    inversions_count = puzzle.get_inversions_number2()

    if isOdd(puzzle.boardSize):
        return not isOdd(inversions_count)
    else:
        position_of_empty_value_from_bottom = puzzle.get_position_of_empty_value_from_bottom2()

        if isOdd(position_of_empty_value_from_bottom):
            return not isOdd(inversions_count)
        else:
            return isOdd(inversions_count)
    return False
