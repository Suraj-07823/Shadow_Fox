# Initial list of superheroes
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original Justice League:", justice_league)

# 1. Count the number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning (she becomes the leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# 4. Separate Aquaman and Flash by inserting Superman or Green Lantern in between
justice_league.remove("Superman")  # Remove to reposition
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("After placing Superman between Aquaman and Flash:", justice_league)

# 5. Replace entire list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League team:", justice_league)

# 6. Sort the list alphabetically
justice_league.sort()
print("Alphabetically sorted team:", justice_league)
print("New leader (0th index):", justice_league[0])
