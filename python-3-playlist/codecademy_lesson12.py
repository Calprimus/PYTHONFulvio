# >>>> 1/9
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

# >>>> 2/9
my_file = open("output.txt", "r+")

# >>>> 3/9

