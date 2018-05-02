# >>>> 2/9
# grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# def print_grades(grades_input):
#     for x in grades_input:
#         print(x)

# print_grades(grades)

# >>>> 4/9
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for x in scores:
        total += x
    return total

print(grades_sum(grades))


