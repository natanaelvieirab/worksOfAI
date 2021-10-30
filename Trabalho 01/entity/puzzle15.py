from entity.Game import Game
from utils.functions import is_odd

def is_15_puzzle_solvable(puzzle: Game):
    inversions_count = puzzle.get_inversions_number2()

    if is_odd(puzzle.boardSize):
        return not is_odd(inversions_count)
    else:
        position_of_empty_value_from_bottom = puzzle.get_position_of_empty_value_from_bottom2()

        if is_odd(position_of_empty_value_from_bottom):
            return not is_odd(inversions_count)
        else:
            return is_odd(inversions_count)
    return False
