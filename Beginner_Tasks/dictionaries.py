# Part 1: List of friends and length of their names

# Step 1: Create a list of friends
friends = ["Aditya", "Meera", "Rohan", "Tina", "Sahil"]

# Step 2: Create a list of tuples with name and length
name_lengths = []

for name in friends:
    name_lengths.append((name, len(name)))

print("List of names and their lengths:")
print(name_lengths)



# Part 2: Track and compare travel expenses

# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Who spent more?
if your_total > partner_total:
    print("You spent more overall.")
elif partner_total > your_total:
    print("Your partner spent more overall.")
else:
    print("You both spent the same.")

# Find significant differences (> ₹100)
print("\n Categories with large spending differences:")

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > 100:
        print(f"{category}: Difference of ₹{difference}")
