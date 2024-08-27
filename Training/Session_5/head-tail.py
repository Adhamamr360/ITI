import random

def flip_coin(possible_outcomes):
    outcome = random.choice(possible_outcomes)
    return outcome

def calculate_probabilities(possible_outcomes):
    num_outcomes = len(possible_outcomes)
    probabilities = {outcome: 1 / num_outcomes for outcome in possible_outcomes}
    return probabilities

possible_outcomes = ['1', '2' , '3' , '4' , '5' , '6']

flip_result = flip_coin(possible_outcomes)

probabilities = calculate_probabilities(possible_outcomes)

print(f"Flip result: {flip_result}")
print("Probabilities:")
for outcome, probability in probabilities.items():
    print(f"{outcome}: {probability:.2f}")
