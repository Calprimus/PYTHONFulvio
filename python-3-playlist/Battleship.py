board = []

for n in range(5):
    board.append(["O"]*5)
for z in board:
    for y in z:
        def print_board(board_in):
            # those are the rows
            for z in board:
                print(" ".join(z))

print_board(board)
