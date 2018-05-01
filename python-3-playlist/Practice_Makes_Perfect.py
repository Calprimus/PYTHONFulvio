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

# def scrabble_score(word):
#     total = 0
#     for x in word:
#         for s in score:
#             if x.lower() == s:
#                 total +=score[s]
#     return total

# # print(scrabble_score("bebe"))

# # How to get just the key from a list or dictionary

# key = list(score.keys())[0]
# print(key)

# >>>> 10/15
# def censor(text, word):
#     if word in text:
#         newtext = text.replace(word, '*' * (len(word)))
#     return newtext

# print (censor("una colta nella vita cera una bella vita", "vita"))

# >>>> 11/15
# def count(sequence, item):
#     total = 0
#     for x in sequence:
#         if x == item:
#             total += 1
#     return total

# print (count([1,2,5,3,2,1,2,1,1], 1))

# >>>> 12/15
# def purify(numbers):
#     new_list = []
#     for n in numbers:
#         if n % 2 == 0:
#             new_list.append(n)
#     return new_list

# print(purify([4,5,6,7,8,9]))    

# >>>> 13/15
# def product(numbers):
#     total = 1
#     for n in numbers:
#         total =n * total
#     return total

# print(product([4,5,5]))  #   

# >>>> 14/15
# def remove_duplicates(original_list):
#     new_list = []
#     for n in original_list:
#         if n not in new_list:
#             new_list.append(n)
#     return new_list

# print (remove_duplicates([1,1,2,2,3,3]))    

# >>>> 15/15
# this one works in the modern python 3.6
# def median(lista):
#     lista = sorted(lista)
#     howmany = len(lista)
#     if howmany % 2 == 1:
#         pos = int(howmany / 2)
#         return lista[pos]
#     else:
#         pos = int(howmany /2)
#         return lista[pos] + lista[pos -1] /2

# print(median([4,5,5,4]))
# >>>> this one worked in the cocademy terminal (python v 2.7)
# def median(lista):
#     lista= sorted(lista)
#     lenght= len(lista)
#     middle = lenght / 2
#     if lenght % 2 == 0:
#         return (lista[middle] + lista[middle+1])/2
#     else:
#         return lista[middle]

# print(median([4,5,5,4]))

def median(list_num):
    s = sorted(list_num)
    if len(s)%2 == 0:
        return (s[len(s)/2] + s[(len(s)/2) - 1]) / 2.0
    else: 
        return s[(len(s)-1)/2]

print(median([4,5,5,4]))