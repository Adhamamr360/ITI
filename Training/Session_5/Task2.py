from collections import defaultdict
import pandas as pd

def calculate_probabilities():
    # Initialize the counts for the events
    counts = defaultdict(int)
    total_outcomes = 0

    # Possible marbles in the bag
    marbles = ['Red'] * 5 + ['Green'] * 3

    # Calculate total number of ways to draw two marbles without replacement
    for i, first_draw in enumerate(marbles):
        remaining_marbles = marbles[:i] + marbles[i+1:]
        for second_draw in remaining_marbles:
            total_outcomes += 1
            counts[(first_draw, second_draw)] += 1

    # Total counts for conditional probabilities
    total_red_first = sum(count for (first, _), count in counts.items() if first == 'Red')
    total_green_first = sum(count for (first, _), count in counts.items() if first == 'Green')

    # Calculate probabilities
    prob_red_then_red = counts[('Red', 'Red')] / total_outcomes
    prob_green_then_red_given_green_first = counts[('Green', 'Red')] / total_green_first
    prob_red_then_green_given_red_first = counts[('Red', 'Green')] / total_red_first

    return prob_red_then_red, prob_green_then_red_given_green_first, prob_red_then_green_given_red_first

# Calculate probabilities
prob_red_then_red, prob_green_then_red_given_green_first, prob_red_then_green_given_red_first = calculate_probabilities()

# Print results
print(f"Probability that the first marble drawn is red and the second marble drawn is also red: {prob_red_then_red:.4f}")
print(f"Probability that the second marble drawn is red given the first marble drawn is green: {prob_green_then_red_given_green_first:.4f}")
print(f"Probability that the second marble drawn is green given the first marble drawn is red: {prob_red_then_green_given_red_first:.4f}")
