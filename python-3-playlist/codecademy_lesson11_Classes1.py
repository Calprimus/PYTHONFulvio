# >>>> 1/18
# class Fruit(object):
#       """A class that makes various tasty fruits."""
#   def __init__(self, name, color, flavor, poisonous):
#     self.name = name
#     self.color = color
#     self.flavor = flavor
#     self.poisonous = poisonous

#   def description(self):
#     print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

#   def is_edible(self):
#     if not self.poisonous:
#       print "Yep! I'm edible."
#     else:
#       print "Don't eat me! I am super poisonous."

# lemon = Fruit("lemon", "yellow", "sour", False)

# lemon.description()
# lemon.is_edible()

# class Fruit(object):
#     """A class that makes various tasty fruits."""
#     def __init__(self, name, color, flavor, poisonous):
#         self.name = name
#         self.color = color
#         self.flavor = flavor
#         self.poisonous = poisonous

#     def description(self):
#         print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

#     def is_edible(self):
#         if not self.poisonous:
#             print ("Yep! I'm edible.")
#         else:
#             print ("Don't eat me! I am super poisonous.")

# lemon = Fruit("lemon", "yellow", "sour", False)

# lemon.description()
# lemon.is_edible()

# >>>> 2/18
# class Animal(object):
#   pass

# >>>> 3/18
# class Animal(object):
#       def __init__(self):
#     pass

# >>>> 4/18
# class Animal(object):
#       def __init__(self, name):
#     self.name = name

# >>>> 5/18
class Animal(object):
      def __init__(self, name):
          self.name = name

zebra = Animal("Jeffrey")
print (zebra.name)

# >>>> 6/18
