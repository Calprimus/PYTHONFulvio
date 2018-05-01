# >>>> 2/15
# def is_even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# >>>> 3/15
# def is_int(x):
#     if x == int(x):
#         return True
#     else: 
#         return False


# x = input("Your input: ")
# print(x)

# >>>> 4/15
# def digit_sum(n):
#     total = 0
#     for digits in str(n):
#         total += int(digits)
#     return total

# print(digit_sum(23))

# >>>> 5/15
# def factorial(x):
#     if x ==0:
#         return 1
#     else:
#         return x*factorial(x-1)

# print(factorial(4))     

# >>>> 6/15    
# def is_prime(x):
#     if x<=1:
#         return False
#     for n in range (2, x-1):
#         if x%n == 0:
#             return False
#         else:
#             return True

# print((is_prime(1)))
          
# >>>> 7/15
# def reverse(text):
#     rev = ""
#     for x in text:
#         rev = x + rev
#     return rev

# printout= reverse("abcd")
# print(printout)
   
# >>>> 8/15
# def anti_vowel(text):
#     removed = text
#     vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     for char1 in text:
#         for char2 in vowel:
#             if char1 == char2:
#                 removed = removed.replace(char1, "")
#     return removed

# print(anti_vowel("Irma la dolce")) 

# >>>> 9/15
# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
#          "x": 8, "z": 10}          

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}   

# def scrabble_score(word):
#     total = 0
#     for x in word:
#         for s in score:
#             if x.lower() == s:
#                 total +=score[s]
#     return total

# print(scrabble_score("bebe"))

test = score["l"]
print(test)