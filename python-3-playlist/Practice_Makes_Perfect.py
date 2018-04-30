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
def reverse(text):
    return reversed(text)
        
out = reverse("tesoro")
print(out)         
