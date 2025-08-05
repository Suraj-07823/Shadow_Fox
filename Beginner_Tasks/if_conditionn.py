# Part 1: BMI Category Checker

# Ask the user to enter height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

# Check BMI category
if bmi >= 30:
    print("Category: Obesity")
elif bmi >= 25:
    print("Category: Overweight")
elif bmi >= 18.5:
    print("Category: Normal")
else:
    print("Category: Underweight")



# Part 2: City to Country Checker

# Predefined cities
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask user for city name
city = input("\nEnter a city name: ")

if city in australia:
    print(city, "is in Australia.")
elif city in uae:
    print(city, "is in UAE.")
elif city in india:
    print(city, "is in India.")
else:
    print("Sorry, I don't know which country", city, "belongs to.")



# Part 3: Check if two cities are in the same country

city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")

# Check if both cities are from the same list
if city1 in australia and city2 in australia:
    print("Both cities are in Australia.")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE.")
elif city1 in india and city2 in india:
    print("Both cities are in India.")
else:
    print("They don't belong to the same country.")
