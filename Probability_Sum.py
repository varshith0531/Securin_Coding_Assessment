"""3. Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).
    Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain Sum = 2. Die A = Die B = 1"""

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
def probability_sum(lis,n):
    count=0
    for i in range(len(lis)):
        s=0
        for j in range(len(lis[i])):
            s+=lis[i][j]
        if s==n:
            count+=1
    return count
sum=2
for i in range(2,(sum*6)+1):
    total=1/probability_sum(combinations,i)
    print("The probability of sum for %d is %.2f"%(i,total))
