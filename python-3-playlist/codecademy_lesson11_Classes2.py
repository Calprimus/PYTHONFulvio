# >>>> 1/11
# class Car(object):
#     pass

# >>>> 2/11

# class Car(object):
#     pass

# my_car = Car()

# >>>> 3/11
# class Car(object):
#     condition = "new"

# my_car = Car()

# >>>> 4/11
# class Car(object):
#     condition = "new"

# my_car = Car()

# print(my_car.condition)

# >>>> 5/11
# class Car(object):
#     condition = "new"
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg

# my_car = Car("DeLorean", "silver", 88)

# print(my_car.model)

# >>>> 6/11
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("DeLorean", "silver", 88)

print(my_car.model)
print(my_car.color)
print(my_car.mpg)

# >>>> 7/11

