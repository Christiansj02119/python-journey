import math

# Calculating area of a circle
radius = int(input('radius: '))
aoc = math.pi * radius ** 2
print('area of circle: ', aoc)

# Calculating area of a rectangle
length = float(input('length: '))
width = float(input('width: '))
area_of_rectangle = length * width
print('area_of_rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 60
gravity = 5
weight = mass * gravity
print(weight, 'N')

# Calculate the density of a liquid
mass = 10
volume = 0.075
density = mass * volume
print(density, 'Kg/m^3')








