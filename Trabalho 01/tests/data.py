from  entity.Game import Game

data = [
    {
        isSolvable: True,
        board: Game([
            [12, 1, 10, 2],
            [7, 11, 4, 14],
            [5, 0, 9, 15],
            [8, 13, 6, 3],
        ]),
    },
    {
        isSolvable: True,
        board: Game([
            [13, 2, 10, 3],
            [1, 12, 8, 4],
            [5, 0, 9, 6],
            [15, 14, 11, 7],
        ]),
    },
    {
        isSolvable: True,
        board: Game([
            [6, 13, 7, 10],
            [8, 9, 11, 0],
            [15, 2, 12, 5],
            [14, 3, 1, 4],
        ]),
    },
    {
        isSolvable: False,
        board: Game([
            [3, 9, 1, 15],
            [14, 11, 4, 6],
            [13, 0, 10, 12],
            [2, 7, 8, 5],
        ]),
    },
]