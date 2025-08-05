# 1. Format function with number and string
# Using format() to mix numbers and strings in a message
number = 145
letter = 'o'

formatted_string = "The number is {} and the letter is '{}'".format(number, letter)
print(formatted_string)

print()  # Just for spacing


# 2. Calculate area of a circular pond and water it holds

radius = 84  # meters
pi = 3.14

area = pi * radius * radius
print("Area of the pond is:", int(area), "square meters")

# Bonus: If each square meter holds 1.4 liters of water
water_per_sqm = 1.4
total_water = area * water_per_sqm

# Print total water with no decimal
print("Total water in the pond :", int(total_water))

print()  # Just for spacing


# 3. Speed calculation
# Given: Distance = 490 meters, Time = 7 minutes
# First convert time to seconds: 7 min = 7 * 60 = 420 sec
distance = 490  # meters
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds  # meters per second

print("Speed in m/s :", int(speed))
