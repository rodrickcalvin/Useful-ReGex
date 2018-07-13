# class Sample(self):
#     x = 5
#     pass


# Create an object or instance
# y = Sample()


# Classes contain attributes and methods.
# - Methods are operation that can be performed the object
# - Attributes are characteristics of an object

# Creating an attribute
class Dog():
    def __init__(self, breed, color, size):
        self.breed = breed
        self.color = color
        self.size = size


maxim = Dog('Rottweiler', 'Black', 'Big')
print(maxim.breed)


# CLASS ATTRIBUTES
class Chicken:
    # This is a class attribute
    species = 'birds'

    def __init__(self, breed, kind):
        self.breed = breed
        self.kind = kind


print(Chicken.species)


# METHODS
class Circle:
    pi = 3.142

    # instantiation
    def __init__(self, diameter, radius=1):
        self.diameter = diameter
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * Circle.pi


c = Circle(4)

# INHERITANCE
