def is_odd(self, value: int):
    return value % 2 == 1

def convert_board_in_list(self, board: list) -> list:
    elements_list = []
    
    for i in range(len(board)):
        elements_list += self.initialState[i]

    return elements_list
