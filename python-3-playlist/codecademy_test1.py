# fish_in_clarks_pond = 50

# print ("Catching fish")
# print (fish_in_clarks_pond)

# number_of_fish_caught = 10
# fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught
# print (fish_in_clarks_pond)

# january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
# annual_rainfall = january_to_june_rainfall

# july_rainfall = 1.05
# annual_rainfall += july_rainfall

# august_rainfall = 4.91
# annual_rainfall += august_rainfall

# september_rainfall = 5.16
# october_rainfall = 7.20
# november_rainfall = 5.06
# december_rainfall = 4.06

# september_to_december_rainfall = 5.16 + 7.20 + 5.06 + 4.06

# annual_rainfall += september_to_december_rainfall

# print (f'the annual rainfall is : {annual_rainfall:.3f}')

# cucumbers = 100
# num_people = 6

# whole_cucumbers_per_person = cucumbers / num_people
# print (whole_cucumbers_per_person)

# float_cucumbers_per_person = cucumbers/num_people
# print (float_cucumbers_per_person)

# address_string = """136 Whowho Rd
# Apt 7
# Whosville, WZ 44494"""
# print (address_string)

# """plan your trip"""

# def hotel_cost(nights):
#   return 140 * nights

# def plane_ride_cost(city):
#   if city == "Charlotte":
#     return 183
#   elif city == "Tampa":
#     return 220
#   elif city == "Pittsburgh":
#     return 222
#   elif city == "Los Angeles":
#     return 475

# def rental_car_cost(days):
#   cost = days * 40
#   if days >= 7:
#     cost -= 50
#   elif days >= 3:
#     cost -= 20
#   return cost

# def trip_cost(city, days, spending_money):
#   return rental_car_cost(days)+hotel_cost(days -1)+plane_ride_cost(city)+spending_money

# print (trip_cost("Los Angeles", 5, 600))

# for letter in "Codecademy":
#       print (letter)
    
# # Empty lines to make the output pretty
# print()
# print()

# word = "Programming is fun!"

# for letter in word:
#   # Only print out the letter i
#   if letter == "i":
#     print (letter)

# once  = {'a': 1, 'b': 2}
# twice = {'a': 2, 'b': 4}
# for key in once:
#       print(key)
#       print ("Once: %s" % once[key])
#       print ("Twice: %s" % twice[key])

# prices = {
#   "banana" : 4,
#   "apple"  : 2,
#   "orange" : 1.5,
#   "pear"   : 3,
# }
# stock = {
#   "banana" : 6,
#   "apple"  : 0,
#   "orange" : 32,
#   "pear"   : 15,
# }

# for key in prices:
#   print (key)
#   print ("price: %s" % prices[key])
#   print ("stock: %s" % stock[key])
  
# total = 0

# for key in prices:
#   print (prices[key]*stock[key])
#   total = total + prices[key]*stock[key]

# print (total)

# shopping_list = ["banana", "orange", "apple"]

# stock = {
#   "banana": 6,
#   "apple": 0,
#   "orange": 32,
#   "pear": 15
# }
    
# prices = {
#   "banana": 4,
#   "apple": 2,
#   "orange": 1.5,
#   "pear": 3
# }

# # Write your code below!
# def compute_bill(food):
#   total = 0
#   for item in food:
#     total = total + food[item]
#     return total

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for key in food:
      if stock[key] > 0:
        total += prices[key]
        stock[key] -= 1
    return total