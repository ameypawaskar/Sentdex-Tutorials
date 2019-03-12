game = [[0, 0, 1],
        [0, 1, 2],
        [1, 2, 1]]


def win(current_game):
    # horizontal
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")
    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically!")

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} has won Diagonally (/)")

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} has won Diagonally (\\)")


win(game)