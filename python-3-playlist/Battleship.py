from random import randint 

board = []

for n in range(5):
    board.append(["O"]*5)

for z in board:
    for y in z:
        def print_board(board_in):
            # those are the rows
            for z in board:
                print(" ".join(z))

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# print_board(board)


# print(random_row(board))
# print(random_col(board))

print (ship_row)
print (ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship")
else: 
    print ("You missed my battleship!") 
    board[ship_row][ship_col] = "X"
    print_board(board)




