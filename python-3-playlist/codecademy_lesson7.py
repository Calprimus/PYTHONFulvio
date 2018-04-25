# n = [3, 5, 7]

# # for i in range(0, len(n)):
# #   print n[i]
  
# def print_list(x):
#   for i in range (0, len(x)):
#     print (x[i])
    
# print_list(n)

# n = [3, 5, 7]


# # Don't forget to return your new list!
# def double_list(x):
#   for i in range(0, len(x)):
#     x[i] = x[i] * 2
#   return x

# print(double_list(n))

# n = [3, 5, 7]

# def total(numbers):
#   result = 0
#   for x in numbers:
#     result =result + x
#   return result

# # print(total(n))

# def total(numbers):
#   result = 0
#   for i in range(0, len(numbers)):
#     result = result + numbers[i]
#   return result

# print (total(n))

# n = ["Michael", "Lieberman"]

# # Add your function here
# def join_strings(words):
#   result = ""
#   for i in range(0, len(words)):
#     result = result + words[i]
#   return result  

# print (join_strings(n))


"""
1.
Create a function called flatten that takes a single list and concatenates all the sublists that are part of it into a single list.

- On line 3, define a function called flatten with one argument called lists.
- Make a new, empty list called results.
- Iterate through lists. Call the looping variable numbers.
- Iterate through numbers.
- For each number, .append() it to results.
- Finally, return results from your function.
"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results



print (flatten(n))