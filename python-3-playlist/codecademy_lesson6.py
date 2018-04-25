# lloyd = {
#   "name": "Lloyd",
#   "homework":[],
#   "quizzes":[],
#   "tests": []
# }

# alice = {
#   "name": "Alice",
#   "homework":[],
#   "quizzes":[],
#   "tests":[]
# }

# tyler = {
#   "name": "Tyler",
#   "homework":[],
#   "quizzes":[],
#   "tests":[]
# }

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

# print the student's name
# print the student's homework
# print the student's quizzes
# print the student's tests

# for student in students:
#   print(student["name"])
#   print(student["homework"])
#   print(student["quizzes"])
#   print(student["tests"])

# division = 5 / 2
# print (division)

numbers = [1,3,5,6,7,8]
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

print(average (numbers))

def get_average (student):
  homework = 0.1 * average(student["homework"])
  quizzes = 0.3 * average(student["quizzes"])
  tests = 0.6 * average(student["tests"])
  return homework + quizzes + tests

# stdres = get_average(alice)
# print(f'num is {stdres:.4}')

# print(f'{get_average(alice):.4}')

def get_letter_grade (score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  

print(get_letter_grade(get_average(lloyd)))

