"""1. How many total combinations are possible? Show the math along with the code!"""
die_faces = list(map(int,input().split()))
total_combinations = len(die_faces) * len(die_faces)
print("Total combinations:", total_combinations)
