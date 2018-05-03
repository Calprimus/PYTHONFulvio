# >>>> 1/18
# my_dict = {
#   "Name": "Jules",
#   "Age": 8,
#   "Eyes": "Brown",
#   "Good?": True
# }
# print (my_dict.items())

# >>>> Explanation Text 2/18
# Concept of Tuples
# keys() and values()
# While .items() returns an array of tuples with each tuple 
# consisting of a key/value pair from the dictionary:

# The .keys() method returns a list of the dictionary's keys, and
# The .values() method returns a list of the dictionary's values.
# Again, these methods will not return the keys or values from 
# the dictionary in any specific order.

# You can think of a tuple as an immutable (that is, unchangeable) list. 
# Tuples are surrounded by ()s and can contain any data type.

# >>>> 2/18
# my_dict = {
#   "Name": "Jules",
#   "Age": 8,
#   "Eyes": "Brown",
#   "Good?": True
# }
# print (my_dict.keys())
# print (my_dict.values())

# >>>> Explanation 3/18
# examples of "in" operator
# for number in range(5):
#   print (number, end = "")

# d = { 
#   "name": "Eric",
#   "age": 26
# }

# for key in d:
#   print (key, d[key], end = "")

# for letter in "Eric":
#   print (letter, end = "")  
#   # python2 print on the same line comma at the end
#   # python 3 print on the same line [[, end = ""]]

# >>>> 3/18
# my_dict = {
#   "Name": "Jules",
#   "Age": 8,
#   "Eyes": "Brown",
#   "Good?": True
# }

# for key in my_dict:
#     print(key, my_dict[key])

# >>>> 4/18 Text Explanation - List Comprehension 
# if we wanted to generate a list according to some logic
# —for example, a list of all the even numbers from 0 to 50?

# Python's answer to this is the list comprehension. 
# List comprehensions are a powerful way to generate lists 
# using the for/in and if keywords we've learned.

# evens_to_50 = [i for i in range(51) if i % 2 == 0]
# print (evens_to_50)

# >>>> 5/18
