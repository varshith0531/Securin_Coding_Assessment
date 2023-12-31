"""1. How many total combinations are possible? Show the math along with the code!"""
sides_per_die = 6
total_combinations = 0
for i in range(1, sides_per_die + 1):
  for j in range(1, sides_per_die + 1):
    total_combinations += 1
print("Total possible combinations:",total_combinations)
