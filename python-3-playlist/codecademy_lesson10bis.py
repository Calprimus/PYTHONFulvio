# >>>> 1/14
# print (5 >> 4)  # Right Shift
# print (5 << 1)  # Left Shift
# print (8 & 5)   # Bitwise AND
# print (9 | 4)   # Bitwise OR
# print (12 ^ 42) # Bitwise XOR
# print (~88)     # Bitwise NOT

# >>>> 2/14
# print(0b1, end = " ")
# print (0b10, end = " ")
# print (0b11, end = " ")
# print (0b100, end = " ")
# print (0b101, end = " ")
# print (0b110, end = " ")
# print (0b111)
# print ("******")
# print (0b1 + 0b11)
# print (0b11 * 0b11)

# 8's bit  4's bit  2's bit  1's bit
#     1       0       1      0 
#     8   +   0    +  2   +  0  = 10 

# >>>> 3/14
# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32
# 2 ** 6 = 64
# 2 ** 7 = 128
# 2 ** 8 = 256
# 2 ** 9 = 512
# 2 ** 10 = 1024

# 8's bit  4's bit  2's bit  1's bit
#     1       0       1      0 
#     8   +   0    +  2   +  0  = 10 

# one = 0b1
# two = 0b10
# three = 0b11
# four = 0b100
# five = 0b101
# six = 0b110
# seven = 0b111
# eight = 0b1000
# nine = 0b1001
# ten = 0b1010
# eleven = 0b1011
# twelve = 0b1100

# >>>> 4/14
# print (bin(1))
# print (bin(2))
# print (bin(3))
# print (bin(4))
# print (bin(5))

# >>>> 5/14
# print (int("1",2))
# print (int("10",2))
# print (int("111",2))
# print (int("0b100",2))
# print (int(bin(5),2))
# # Print out the decimal equivalent of the binary 11001001.
# print (int("11001001", 2))

# >>>> 6/14
# shift_right = 0b1100
# shift_left = 0b1

# # Your code here!
# shift_right = 0b1100 >> 2
# shift_left = 0b1 << 2

# print (bin(shift_right))
# print (bin(shift_left))

# >>>> 7/14
# bino = bin(0b1110 & 0b101)
# print(int(bino, 2))

# >>>> 8/14
bino = bin(0b1110 | 0b101)
print(int(bino, 2))

