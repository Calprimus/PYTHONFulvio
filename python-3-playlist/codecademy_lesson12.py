# >>>> 1/9
# my_list = [i ** 2 for i in range(1, 11)]
# # Generates a list of squares of the numbers 1 - 10

# f = open("output.txt", "w")

# for item in my_list:
#   f.write(str(item) + "\n")

# f.close()

# >>>> 2/9
# my_file = open("output.txt", "r+")

# >>>> 3/9
# my_list = [i ** 2 for i in range(1, 11)]

# my_file = open("output.txt", "r+")

# for item in my_list:
#   my_file.write(str(item) + "\n")


# my_file.close()

# >>>> 4/9
# my_file = open("output.txt", "r+")

# print(my_file.read())

# my_file.close()

# >>>> 5/9
# my_file = open("output.txt", "r")

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# my_file.close()

# # >>>> 6/9
# # Use a file handler to open a file for writing
# write_file = open("text.txt", "w")


# # Open the file for reading
# read_file = open("text.txt", "r")

# # Write to the file
# write_file.write("Not closing files is VERY BAD.")
# write_file.close()


# # Try to read from the file
# print (read_file.read())
# read_file.close()

# >>>> 7/9
# with open("text.txt", "w") as textfile:
#   textfile.write("Success!")

# >>>> 8/9
my_file = open("text.txt", "w")
with my_file as file:
  file.write("Yo dude wsup")


