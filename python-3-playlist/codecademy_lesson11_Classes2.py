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
# class Car(object):
#     condition = "new"
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg

# my_car = Car("DeLorean", "silver", 88)

# print(my_car.model)
# print(my_car.color)
# print(my_car.mpg)

# >>>> 7/11
# class Car(object):
#     condition = "new"
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#     def display_car(self):
#         return "This is a " + self.color + " "+ self.model + " with " + str(self.mpg) + " MPG"
        
# my_car = Car("DeLorean", "silver", 88)

# print(my_car.display_car())

# >>>> 8/11

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a " + self.color + " "+ self.model + " with " + str(self.mpg) + " MPG"

    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = ElectricCar("molten salt", "ferrari", "red", 200)