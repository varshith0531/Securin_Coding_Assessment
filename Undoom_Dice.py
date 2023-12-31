"""Now comes the real challenge. You were happily spending a lazy afternoon playing your board game with your dice when suddenly the mischievous Norse God Loki ( You
love Thor too much & Loki didn’t like that much ) appeared.
Loki dooms your dice for his fun removing all the “Spots” off the dice. No problem! You have the tools to re-attach the “Spots” back on the Dice.
However, Loki has doomed your dice with the following conditions:
● Die A cannot have more than 4 Spots on a face.
● Die A may have multiple faces with the same number of spots.
● Die B can have as many spots on a face as necessary i.e. even more than 6.
But in order to play your game, the probability of obtaining the Sums must remain the
same!
So if you could only roll P(Sum = 2) = 1/X, the new dice must have the spots reattached
such that those probabilities are not changed.
Input:
● Die_A = [1, 2, 3, 4, 5, 6] & Die B = Die_A = [1, 2, 3, 4, 5, 6]
Output:
● A Transform Function undoom_dice that takes (Die_A, Die_B) as input &
outputs New_Die_A = [?, ?, ?, ?, ?, ?],New_Die_B = [?, ?,?, ?, ?, ?] where,
● No New_Die A[x] > 4."""

def calculate_combinations(total_sum):
    combinations = [0] * (total_sum + 1)
    combinations[0] = 1
    for i in range(1, total_sum + 1):
        combinations[i] = combinations[i - 1] + combinations[i]
    return combinations

def calculate_spots(combinations, die_faces):
    spots = [0] * len(die_faces)
    total_sum = sum(die_faces)
    for i in range(len(die_faces) - 1, -1, -1):
        while die_faces[i] + spots[i] > total_sum or combinations[total_sum - die_faces[i] - spots[i]] <= 0:
            spots[i] += 1
        combinations[total_sum] -= 1
        total_sum -= die_faces[i] + spots[i]
    return spots

def undoom_dice(Die_A, Die_B):
    total_sum = sum(Die_A) + sum(Die_B)
    combinations = calculate_combinations(total_sum)
    new_Die_A = calculate_spots(combinations, Die_A)
    new_Die_B = calculate_spots(combinations, Die_B)
    return new_Die_A, new_Die_B

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
