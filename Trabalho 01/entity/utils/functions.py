def is_odd(value: int):
    return value % 2 == 1


def convert_board_in_list(board: list) -> list:
    # elements_list = []

    # for i in range(len(board)):
    #     elements_list += self.initialState[i]

    return [j for sub in board for j in sub]


if __name__ == "__main__":
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(board)
    print(convert_board_in_list(board))
