from random import randint 

board = []

for n in range(5):
    board.append(["O"]*5)

# for z in board:
#     for y in z:
#         def print_board(board_in):
#             # those are the rows
#             for z in board:
#                 print(" ".join(z))

def print_board(board):
# those are the rows
    for row in board:
        print(" ".join(row))

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

for turn in range(4):

  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship")
  else: 
    if guess_row not in range(5) or guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      board[guess_row-1][guess_col-1] = "X"
      print ("You missed my battleship!") 
    print_board(board)
    print("Turn", turn +1)



