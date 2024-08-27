import random

def roll_dice():
    return random.randint(1, 6)

def calculate_probabilities(num_rolls):
    outcomes = [roll_dice() for _ in range(num_rolls)]
    counts = {i: outcomes.count(i) for i in range(1, 7)}
    
    probabilities = {outcome: count / num_rolls for outcome, count in counts.items()}
    return probabilities

num_rolls = 6
probabilities = calculate_probabilities(num_rolls)

print(f"Outcomes after {num_rolls} rolls:")
for outcome, probability in probabilities.items():
    print(f"{outcome}: {probability:.4f}")
