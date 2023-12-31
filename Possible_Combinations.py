"""2. Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!
Hint: A 6 x 6 Matrix."""

num = 2
sides_per_die = 6
combinations = []
for i in range(1, sides_per_die + 1):
  combinations.append((i,))
for _ in range(1, num):
  new_combo = []
  for existing_combo in combinations:
    for roll in range(1, sides_per_die + 1):
      new_combo.append(existing_combo + (roll,))
  combinations = new_combo
print(combinations)
