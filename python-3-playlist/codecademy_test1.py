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

"""plan your trip"""

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days)+hotel_cost(days -1)+plane_ride_cost(city)+spending_money

print (trip_cost("Los Angeles", 5, 600))