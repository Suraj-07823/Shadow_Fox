# 1. Store the value of pi
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

# 2. Using a keyword as a variable name (Uncomment to see the error)
# for = 4
# print(for)
# Python will throw a SyntaxError: 'for' is a reserved keyword

# 3. Simple Interest Calculation
P = 10000  # Principal Amount in Rs.
R = 5      # Rate of Interest in %
T = 3      # Time in years

SI = (P * R * T) / 100
print(f"Simple Interest for {T} years = ₹{SI}")
