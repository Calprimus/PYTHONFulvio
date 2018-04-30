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

def anti_vowel(text):
    removed = text
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for char1 in text:
        for char2 in vowel:
            if char1 == char2:
                removed = removed.replace(char1, "")
    return removed

print(anti_vowel("Irma la dolce"))            